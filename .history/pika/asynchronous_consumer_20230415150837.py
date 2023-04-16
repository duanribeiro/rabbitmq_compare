        LOGGER.info(
            origin="setup_dead_letter_exchange",
            message=f"Declaring queue: {self.DEAD_LETTER_QUEUE}",
        )