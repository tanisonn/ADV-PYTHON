import logging
'''logging.basicConfig(filename="timestamp_Log.txt",format='%(asctime)s:%(levelname)s:%(message)s')  
logging.critical("This is Critical message:")
logging.error("This is error message")
logging.warning("This is warning message")
logging.info("This is info message")
logging.debug("This is debug message")'''
# default the time format is   YYYY-MM-DD HH:MM:SS:MSMSMS
#Inorder to change the time format we could change by datefmt()
import logging
logging.basicConfig(filename="timestamp_Log.txt",level=logging.WARNING,format='%(asctime)s:%(levelname)s:%(message)s',datefmt='%d/%m/%Y %H:%M:%S')
logging.critical("This is Critical message:")
logging.error("This is error message")
logging.warning("This is warning message")
logging.info("This is info message")
logging.debug("This is debug message")

