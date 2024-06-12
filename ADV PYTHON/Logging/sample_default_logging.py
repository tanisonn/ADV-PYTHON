import logging
logging.basicConfig()
logging.critical("This is Critical message:")
logging.error("This is error message")
logging.warning("This is warning message")
logging.info("This is info message")
logging.debug("This is debug message")
#This ouput is printed to console since no filename is provided and the default level for logging is 30 or logging.WARINING