import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(host="amqp://guest:guest@localhost:5672"))
import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('amqp://guest:guest@localhost:5672'))
channel = connection.channel()