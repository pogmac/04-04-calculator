arguments = [1,2,3,4]
action = 3

def calculateList(arguments):
    if action == 1:
        result = 0
        for i in range (len(arguments)):
            result = result +arguments[i]
    elif action == 3:
            result = 1
            for argument in arguments:
                result = result * argument
    print("result =", result)
#print(dir(arguments))
calculateList(arguments)




"""    
try:
    number = int(number)
    print("Entered number is, ", number,"and it's hexadecimal number is:", hex(number))
except ValueError:
    try:
        number = float(number)
        print("Entered number is float and it's hexadecimal number is:", float.hex(number)) 
    except ValueError:
        print("You entered an invalid number")
"""

"""
import sys
import logging
#logging.basicConfig(level=logging.DEBUG)
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(message)s')

def print_maturity(age):
    if age >= 18:
        logging.info("You are an adult")
    else:
        logging.info("You are a kiddo!")

if __name__ == "__main__":
    
    logging.debug("The program was called with this parameters %s" % sys.argv[1:])
    logging.debug("First parameter is %s" % sys.argv[1])
    age = int(sys.argv[1])
    print_maturity(age)
"""
"""
def customized_hello(first_name, last_name, prefix):
    print("Hello %s %s %s!" % (prefix, first_name, last_name ))

if __name__ == "__main__":
    print(len(sys.argv))
    if len(sys.argv) < 3:
        exit(1)
    first_name = sys.argv[1]
    last_name = sys.argv[2]
    prefix = sys.argv[3]
    customized_hello(first_name, last_name, prefix)
"""
