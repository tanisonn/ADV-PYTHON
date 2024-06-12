import logging
import inspect
def create(level,loggername,filename="",):
    #func=inspect.stack[0][3]
    #loggername=func+"logger
    logger=logging.getLogger(loggername)
    if filename=="":
        Handler=logging.StreamHandler()
        Handler.setLevel(level)
    else:
        Handler=logging.FileHandler(filename,mode="a")
        Handler.setLevel(level)
    formatter=logging.Formatter("%(asctime)s:%(name)s:%(levelname)s:%(message)s")
    Handler.setFormatter(formatter)
    logger.addHandler(Handler)
    return logger

    