import logging
logging.basicConfig(filename="log1.txt",filemode="a",format='%(levelname)s:%(message)s')
logging.critical("This is Critical message:")
logging.error("This is error message")
logging.warning("This is warning message")
logging.info("This is info message")
logging.debug("This is debug message")
