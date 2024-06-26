import logging
logger1=logging.getLogger("Tanishq")
logger2=logging.getLogger("Tanison")
logger1.setLevel(logging.DEBUG)
logger2.setLevel(logging.DEBUG)
consoleHandler=logging.StreamHandler()
FileHandler=logging.FileHandler("console_file.log",mode="a")
consoleHandler.setLevel(logging.WARNING)
FileHandler.setLevel(logging.INFO)
formatter=logging.Formatter("%(asctime)s:%(name)s:%(levelname)s:%(message)s",datefmt='%d/%m/%Y %H:%M:%S')
consoleHandler.setFormatter(formatter)
FileHandler.setFormatter(formatter)
logger1.addHandler(consoleHandler)
logger2.addHandler(FileHandler)
logger1.critical("tHIS IS CRITICAL MESSAGE from logger1")
logger1.error("this is error message from logger1")
logger1.warning("this is warning message from logger1")
logger1.info("this is info message from logger 1")
logger1.debug("this is debug message from logger 1")
logger2.critical("tHIS IS CRITICAL MESSAGE from logger 2")
logger2.error("this is error message from logger2")
logger2.warning("this is warning message form logger 2")
logger2.info("this is info message from logger 2")
logger2.debug("this is debug message from logger 2")