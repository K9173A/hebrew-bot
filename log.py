import logging


def initialize_logger():
    logger = logging.getLogger('BotLogger')
    logger.setLevel(logging.INFO)

    logger_file_handler = logging.FileHandler('hebrew-bot.log')
    logger_file_handler.setLevel(logging.DEBUG)

    logger_stream_handler = logging.StreamHandler()
    logger_stream_handler.setLevel(logging.INFO)

    logger_formatter = logging.Formatter(
        '[%(levelname)s %(asctime)s %(filename)s:%(lineno)s @ %(funcName)s()] %(message)s'
    )
    logger_file_handler.setFormatter(logger_formatter)
    logger_stream_handler.setFormatter(logger_formatter)

    logger.addHandler(logger_file_handler)
    logger.addHandler(logger_stream_handler)
