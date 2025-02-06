import logging


class Logger:
    LOG_LEVEL = logging.INFO
    FILENAME = "my_logging.log"
    ENCODING = "utf-8"
    FORMAT = "%(levelname)s (%(asctime)s): %(message)s"
    LOG_NAME = "log"

    logger = logging.getLogger(LOG_NAME)
    logger.setLevel(LOG_LEVEL)
    handler = logging.FileHandler(
        filename=FILENAME,
        encoding=ENCODING
    )
    handler.setLevel(LOG_LEVEL)
    formatter = logging.Formatter(FORMAT)
    handler.setFormatter(formatter)
    logger.addHandler(handler)

    @classmethod
    def info(cls, param):
        cls.logger.info(param)
