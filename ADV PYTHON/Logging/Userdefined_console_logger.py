import logging
logger=logging.getLogger("Tanison")
"""logger.setLevel(logging.ERROR)
"""
ConsoleHandler=logging.StreamHandler()
ConsoleHandler.setLevel(logging.WARNING)
formatter=logging.Formatter("%(asctime)s:%(levelname)s:%(name)s:%(message)s",datefmt="%d/%m/%Y %H:%M:%S")
ConsoleHandler.setFormatter(formatter)
logger.addHandler(ConsoleHandler)
logger.critical("tHIS IS CRITICAL MESSAGE")
logger.error("this is error message")
logger.warning("this is warning message")
logger.info("this is info message")
logger.debug("this is debug message")
