import logging
logging.basicConfig(filename='arguments_LOG.txt',format='time:%(asctime)s:%(levelname)s:%(levelno)d:%(message)s:process-id:%(process)d:line-NO:%(lineno)d:Module:%(module)s')
logging.critical("This is Critical message:")
logging.error("This is error message")
logging.warning("This is warning message")
logging.info("This is info message")
logging.debug("This is debug message")
