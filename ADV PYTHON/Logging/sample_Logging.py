import logging
logging.basicConfig(filename="Log.txt",level=logging.WARNING)
logging.critical("This is Critical message:")
logging.error("This is error message")
logging.warning("This is warning message")
logging.info("This is info message")
logging.debug("This is debug message")
#By default overwritting is happening inorder to append there are other modes
