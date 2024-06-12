import logging
from generic_logging_module import create
def f1():
    logger=create(logging.WARNING,"Tanishq","abc.txt")
    logger.critical("This is critical from f1")
    logger.error("This is error from f1")
    logger.warning("This is warning from f1")
    logger.info("this is info from f1")
    logger.debug("This is debug from f1")
def f2():
    logger=create(logging.ERROR,"Tanison")
    logger.critical("This is critical from f2")
    logger.error("This is error from f2")
    logger.warning("This is warning from f2")
    logger.info("this is info from f2")
    logger.debug("This is debug from f2")
f1()
f2()