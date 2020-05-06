#closure



#nested function
def outerFun(text):
	t = text;

	def innerFun():
		print(t)

	innerFun()

outerFun('Hey!')

"""here, innerFunction() is treated as nested Function 
which uses text as non-local variable. """

"""in clousre it is a fun object that remebers values in enclosing
even if they are not present in memory"""

def outerFun(text):
	t = text

	def innerFun():
		print(t)

	return innerFun   #we are returning innerFun not calling

outerFun("Hi clousre")   #it will not give anything

#assing to another variable
myFun = outerFun('Hi clousre')

#now myFUn is used as a function
myFun()






 # Python program to illustrate 
# closures 
import logging 
logging.basicConfig(filename='example.log', level=logging.INFO) 
  
  
def logger(func): 
	#inner function
    def log_func(*args): 
        logging.info( 
            'Running "{}" with arguments {}'.format(func.__name__, args)) 
        print(func(*args)) 
    # Necessary for closure to work (returning WITHOUT parenthesis) 
    return log_func               
  
def add(x, y): 
    return x+y 
  
def sub(x, y): 
    return x-y 
  
add_logger = logger(add) 
sub_logger = logger(sub) 
  
add_logger(3, 3) 
add_logger(4, 5) 
  
sub_logger(10, 5) 
sub_logger(20, 10) 



"""this can be done with original sub and add function 
but using clousre it created a logger file as example.py"""