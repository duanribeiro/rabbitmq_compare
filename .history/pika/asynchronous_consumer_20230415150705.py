import functools

import pika
from pika.exchange_type import ExchangeType



class AsynchronousConsumer(object):
    EXCHANGE: str = None
    EXCHANGE_TYPE: ExchangeType = None
    QUEUE: str = None
    ROUTING_KEY: str = None
    DEAD_LETTER_EXCHANGE: str = None
    DEAD_LETTER_EXCHANGE_TYPE: ExchangeType = None
    DEAD_LETTER_QUEUE: str = None
    DEAD_LETTER_ROUTING_KEY: str = None
    MESSAGE_TTL: int = 10000

    def __init__(self):
        """Create a new instance of the consumer class, passing in the AMQP
        URL used to connect to RabbitMQ.
        """
        self.should_reconnect = False
        self.was_consuming = False

        self._connection = None
        self._channel = None
        self._closing = False
        self._consumer_tag = None
        self._url = settings.BROKER_URL
        self._consuming = False
        self._prefetch_count = 1

    def connect(self):
        """This method connects to RabbitMQ, returning the connection handle.
        When the connection is established, the on_connection_open method
        will be invoked by pika.

        """
        LOGGER.info(origin="connect", message=f"Connecting to {self._url}")
        return pika.SelectConnection(
            parameters=pika.URLParameters(self._url),
            on_open_callback=self.on_connection_open,
            on_open_error_callback=self.on_connection_open_error,
            on_close_callback=self.on_connection_closed,
        )

    def close_connection(self):
        self._consuming = False
        if self._connection.is_closing or self._connection.is_closed:
            LOGGER.info(
                origin="close_connection",
                message="Connection is closing or already closed",
            )
        else:
            LOGGER.info(origin="close_connection", message="Closing connection")
            self._connection.close()

    def on_connection_open(self, _unused_connection):
        """This method is called by pika once the connection to RabbitMQ has
        been established. It passes the handle to the connection object in
        case we need it, but in this case, we'll just mark it unused.

        :param pika.SelectConnection _unused_connection: The connection
        """
        LOGGER.info(origin="on_connection_open", message="Connection opened")
        self.open_channel()

    def on_connection_open_error(self, _unused_connection, err):
        """This method is called by pika if the connection to RabbitMQ
        can't be established.

        :param pika.SelectConnection _unused_connection: The connection
        :param Exception err: The error
        """
        LOGGER.error(origin="on_connection_open_error", message=f"Connection open failed: {err}")

        self.reconnect()

    def on_connection_closed(self, _unused_connection, reason):
        """This method is invoked by pika when the connection to RabbitMQ is
        closed unexpectedly. Since it is unexpected, we will reconnect to
        RabbitMQ if it disconnects.

        :param pika.connection.Connection connection: The closed connection obj
        :param Exception reason: exception representing reason for loss of
            connection.
        """
        self._channel = None
        if self._closing:
            self._connection.ioloop.stop()
        else:
            LOGGER.warning(
                origin="on_connection_closed",
                message=f"Connection closed, reconnect necessary: {reason}",
            )
            self.reconnect()

    def reconnect(self):
        """Will be invoked if the connection can't be opened or is
        closed. Indicates that a reconnect is necessary then stops the
        ioloop.
        """
        self.should_reconnect = True
        self.stop()

    def open_channel(self):
        """Open a new channel with RabbitMQ by issuing the Channel.Open RPC
        command. When RabbitMQ responds that the channel is open, the
        on_channel_open callback will be invoked by pika.
        """
        LOGGER.info(origin="open_channel", message="Creating a new channel")
        self._connection.channel(on_open_callback=self.on_channel_open)

    def on_channel_open(self, channel):
        """This method is invoked by pika when the channel has been opened.
        The channel object is passed in so we can make use of it.

        Since the channel is now open, we'll declare the exchange to use.

        :param pika.channel.Channel channel: The channel object
        """
        LOGGER.info(origin="on_channel_open", message="Channel opened")
        self._channel = channel
        self.add_on_channel_close_callback()
        self.setup_exchange()
        self.setup_dead_letter_exchange()

    def add_on_channel_close_callback(self):
        """This method tells pika to call the on_channel_closed method if
        RabbitMQ unexpectedly closes the channel.
        """
        LOGGER.info(
            origin="add_on_channel_close_callback",
            message="Adding channel close callback",
        )

        self._channel.add_on_close_callback(self.on_channel_closed)

    def on_channel_closed(self, channel, reason):
        """Invoked by pika when RabbitMQ unexpectedly closes the channel.
        Channels are usually closed if you attempt to do something that
        violates the protocol, such as re-declare an exchange or queue with
        different parameters. In this case, we'll close the connection
        to shutdown the object.

        :param pika.channel.Channel: The closed channel
        :param Exception reason: why the channel was closed
        """
        LOGGER.warning(
            origin="on_channel_closed",
            message=f"Channel {channel} was closed: {reason}",
        )
        self.close_connection()

    def setup_dead_letter_exchange(self):
        """Setup the exchange on RabbitMQ by invoking the Exchange.Declare RPC
        command. When it is complete, the on_exchange_declareok method will
        be invoked by pika.

        :param str|unicode exchange_name: The name of the exchange to declare
        """
        LOGGER.info(
            origin="setup_dead_letter_exchange",
            message=f"Declaring dead letter exchange: {self.DEAD_LETTER_EXCHANGE}",
        )

        self._channel.exchange_declare(
            exchange=self.DEAD_LETTER_EXCHANGE,
            exchange_type=self.DEAD_LETTER_EXCHANGE_TYPE,
            callback=self.on_dlx_declareok,
        )

    def on_dlx_declareok(self, _unused_frame):
        """Invoked by pika when RabbitMQ has finished the Exchange.Declare RPC
        command.

        :param pika.Frame.Method unused_frame: Exchange.DeclareOk response frame
        """
        LOGGER.info(
            origin="setup_dead_letter_exchange",
            message=f"Dead letter exchange declared: {self.DEAD_LETTER_EXCHANGE}",
        )
        self.setup_dead_letter_queue()

    def setup_dead_letter_queue(self):
        """Setup the queue on RabbitMQ by invoking the Queue.Declare RPC
        command. When it is complete, the on_queue_declareok method will
        be invoked by pika.
        """
        LOGGER.info(
            origin="setup_dead_letter_exchange",
            message=f"Declaring queue: {self.DEAD_LETTER_QUEUE}",
        )
        self._channel.queue_declare(queue=self.DEAD_LETTER_QUEUE, callback=self.on_dlq_declareok)

    def on_dlq_declareok(self, _unused_frame):
        """Method invoked by pika when the Queue.Declare RPC call made in
        setup_queue has completed. In this method we will bind the queue
        and exchange together with the routing key by issuing the Queue.Bind
        RPC command. When this command is complete, the on_bindok method will
        be invoked by pika.

        :param pika.frame.Method _unused_frame: The Queue.DeclareOk frame
        """
        LOGGER.info(
            origin="on_dlq_declareok",
            message=f"Binding {self.DEAD_LETTER_EXCHANGE} "
            + f"to {self.DEAD_LETTER_QUEUE} "
            + f"with routing key {self.DEAD_LETTER_ROUTING_KEY}",
        )

        cb = functools.partial(self.on_bindok, queue=self.DEAD_LETTER_QUEUE)
        self._channel.queue_bind(
            queue=self.DEAD_LETTER_QUEUE,
            exchange=self.DEAD_LETTER_EXCHANGE,
            routing_key=self.DEAD_LETTER_ROUTING_KEY,
            callback=cb,
        )

    def setup_exchange(self):
        """Setup the exchange on RabbitMQ by invoking the Exchange.Declare RPC
        command. When it is complete, the on_exchange_declareok method will
        be invoked by pika.

        :param str|unicode exchange_name: The name of the exchange to declare
        """
        LOGGER.info(origin="setup_exchange", message=f"Declaring exchange: {self.EXCHANGE}")

        self._channel.exchange_declare(
            exchange=self.EXCHANGE,
            exchange_type=self.EXCHANGE_TYPE,
            callback=self.on_exchange_declareok,
        )

    def on_exchange_declareok(self, _unused_frame):
        """Invoked by pika when RabbitMQ has finished the Exchange.Declare RPC
        command.

        :param pika.Frame.Method unused_frame: Exchange.DeclareOk response frame
        """
        LOGGER.info(
            origin="on_exchange_declareok",
            message=f"Exchange declared: {self.EXCHANGE}",
        )
        self.setup_queue()

    def setup_queue(self):
        """Setup the queue on RabbitMQ by invoking the Queue.Declare RPC
        command. When it is complete, the on_queue_declareok method will
        be invoked by pika.
        """
        LOGGER.info(origin="setup_queue", message=f"Declaring queue {self.QUEUE}")
        self._channel.queue_declare(
            queue=self.QUEUE,
            callback=self.on_queue_declareok,
            arguments={
                "x-message-ttl": self.MESSAGE_TTL,
                "x-dead-letter-exchange": self.DEAD_LETTER_EXCHANGE,
                "x-dead-letter-routing-key": self.DEAD_LETTER_ROUTING_KEY,
            },
        )

    def on_queue_declareok(self, _unused_frame):
        """Method invoked by pika when the Queue.Declare RPC call made in
        setup_queue has completed. In this method we will bind the queue
        and exchange together with the routing key by issuing the Queue.Bind
        RPC command. When this command is complete, the on_bindok method will
        be invoked by pika.

        :param pika.frame.Method _unused_frame: The Queue.DeclareOk frame
        """
        LOGGER.info(
            origin="on_queue_declareok",
            message=f"Binding {self.DEAD_LETTER_EXCHANGE} "
            + f"to {self.DEAD_LETTER_QUEUE} "
            + f"with routing key {self.DEAD_LETTER_ROUTING_KEY}",
        )

        cb = functools.partial(self.on_bindok, queue=self.QUEUE)
        self._channel.queue_bind(self.QUEUE, self.EXCHANGE, routing_key=self.ROUTING_KEY, callback=cb)

    def on_bindok(self, _unused_frame, queue):
        """Invoked by pika when the Queue.Bind method has completed. At this
        point we will set the prefetch count for the channel.

        :param pika.frame.Method _unused_frame: The Queue.BindOk response frame
        :param str|unicode userdata: Extra user data (queue name)
        """
        LOGGER.info(origin="on_bindok", message=f"Queue bound: {queue}")
        self.set_qos()

    def set_qos(self):
        """This method sets up the consumer prefetch to only be delivered
        one message at a time. The consumer must acknowledge this message
        before RabbitMQ will deliver another one. You should experiment
        with different prefetch values to achieve desired performance.
        """
        self._channel.basic_qos(prefetch_count=self._prefetch_count, callback=self.on_basic_qos_ok)

    def on_basic_qos_ok(self, _unused_frame):
        """Invoked by pika when the Basic.QoS method has completed. At this
        point we will start consuming messages by calling start_consuming
        which will invoke the needed RPC commands to start the process.

        :param pika.frame.Method _unused_frame: The Basic.QosOk response frame
        """
        LOGGER.info(origin="on_basic_qos_ok", message=f"QOS set to: {self._prefetch_count}")
        self.start_consuming()

    def start_consuming(self):
        """This method sets up the consumer by first calling
        add_on_cancel_callback so that the object is notified if RabbitMQ
        cancels the consumer. It then issues the Basic.Consume RPC command
        which returns the consumer tag that is used to uniquely identify the
        consumer with RabbitMQ. We keep the value to use it when we want to
        cancel consuming. The on_message method is passed in as a callback pika
        will invoke when a message is fully received.
        """
        LOGGER.info(origin="start_consuming", message="Issuing consumer related RPC commands")
        self.add_on_cancel_callback()
        self._consumer_tag = self._channel.basic_consume(self.QUEUE, self.on_message)
        self.was_consuming = True
        self._consuming = True

    def add_on_cancel_callback(self):
        """Add a callback that will be invoked if RabbitMQ cancels the consumer
        for some reason. If RabbitMQ does cancel the consumer,
        on_consumer_cancelled will be invoked by pika.
        """
        LOGGER.info(
            origin="add_on_cancel_callback",
            message="Adding consumer cancellation callback",
        )
        self._channel.add_on_cancel_callback(self.on_consumer_cancelled)

    def on_consumer_cancelled(self, method_frame):
        """Invoked by pika when RabbitMQ sends a Basic.Cancel for a consumer
        receiving messages.

        :param pika.frame.Method method_frame: The Basic.Cancel frame
        """
        LOGGER.info(
            origin="on_consumer_cancelled",
            message=f"Consumer was cancelled remotely, shutting down: {method_frame}",
        )
        if self._channel:
            self._channel.close()

    def on_message(self, _unused_channel, basic_deliver, properties, body):
        """Invoked by pika when a message is delivered from RabbitMQ. The
        channel is passed for your convenience. The basic_deliver object that
        is passed in carries the exchange, routing key, delivery tag and
        a redelivered flag for the message. The properties passed in is an
        instance of BasicProperties with the message properties and the body
        is the message that was sent.

        :param pika.channel.Channel _unused_channel: The channel object
        :param pika.Spec.Basic.Deliver: basic_deliver method
        :param pika.Spec.BasicProperties: properties
        :param bytes body: The message body
        """
        LOGGER.info(
            origin="on_message",
            message=f"Received message #{basic_deliver.delivery_tag}" + "from {properties.app_id}: {body}",
        )
        self.acknowledge_message(basic_deliver.delivery_tag)

    def acknowledge_message(self, delivery_tag):
        """Acknowledge the message delivery from RabbitMQ by sending a
        Basic.Ack RPC method for the delivery tag.

        :param int delivery_tag: The delivery tag from the Basic.Deliver frame
        """
        LOGGER.info(
            origin="acknowledge_message",
            message=f"Acknowledging message {delivery_tag}",
        )
        self._channel.basic_ack(delivery_tag)

    def stop_consuming(self):
        """Tell RabbitMQ that you would like to stop consuming by sending the
        Basic.Cancel RPC command.
        """
        if self._channel:
            LOGGER.info(
                origin="stop_consuming",
                message="Sending a Basic.Cancel RPC command to RabbitMQ",
            )
            cb = functools.partial(self.on_cancelok, userdata=self._consumer_tag)
            self._channel.basic_cancel(self._consumer_tag, cb)

    def on_cancelok(self, _unused_frame, userdata):
        """This method is invoked by pika when RabbitMQ acknowledges the
        cancellation of a consumer. At this point we will close the channel.
        This will invoke the on_channel_closed method once the channel has been
        closed, which will in-turn close the connection.

        :param pika.frame.Method _unused_frame: The Basic.CancelOk frame
        :param str|unicode userdata: Extra user data (consumer tag)
        """
        self._consuming = False
        LOGGER.info(
            origin="on_cancelok",
            message=f"RabbitMQ acknowledged the cancellation of the consumer: {userdata}",
        )
        self.close_channel()

    def close_channel(self):
        """Call to close the channel with RabbitMQ cleanly by issuing the
        Channel.Close RPC command.
        """
        LOGGER.info(origin="close_channel", message="Closing the channel")
        self._channel.close()

    def run(self):
        """Run the example consumer by connecting to RabbitMQ and then
        starting the IOLoop to block and allow the SelectConnection to operate.
        """
        self._connection = self.connect()
        self._connection.ioloop.start()

    def stop(self):
        """Cleanly shutdown the connection to RabbitMQ by stopping the consumer
        with RabbitMQ. When RabbitMQ confirms the cancellation, on_cancelok
        will be invoked by pika, which will then closing the channel and
        connection. The IOLoop is started again because this method is invoked
        when CTRL-C is pressed raising a KeyboardInterrupt exception. This
        exception stops the IOLoop which needs to be running for pika to
        communicate with RabbitMQ. All of the commands issued prior to starting
        the IOLoop will be buffered but not processed.
        """
        if not self._closing:
            self._closing = True
            LOGGER.info(origin="stop", message="Stopping")
            if self._consuming:
                self.stop_consuming()
                self._connection.ioloop.start()
            else:
                self._connection.ioloop.stop()
            LOGGER.info(origin="stop", message="Stopped")
