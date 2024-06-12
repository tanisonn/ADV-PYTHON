import logging
logging.basicConfig(filename="logExcpetion.txt",level=20,format='%(asctime)s:%(levelname)s:%(message)s',datefmt="%d/%m/%Y %I:%M:%S %p")
logging.info("A User used our application")
try:
    a=int(input("Enter the first number:"))
    b=int(input("Enter the second number:"))
    print("The result of a/b is",a/b)
except ZeroDivisionError as msg:
    print("The second number should not be zero")
    logging.exception(msg)
except ValueError as msg:
    print("The entered number should be in int")
    logging.exception(msg)
logging.info("The user successfully used our application")



