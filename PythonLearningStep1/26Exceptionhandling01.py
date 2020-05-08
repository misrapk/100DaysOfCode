# Exception Handling
"""Some of the standard exceptions which are most frequent include
 IndexError, ImportError, IOError, ZeroDivisionError, TypeError.

 """


a = [1,2,3]
try:  
    print ("Second element = %d" %(a[1]))
  
    # Throws error since there are only 3 elements in array 
    print ("Fourth element = %d" %(a[3]))  
  
except IndexError: 
    print ("An error occurred")



#multiple except clause

try:
	a=3
	if a<=4:
		b=a/(a-3)     #divide by zero

	print("Value of b: ", b)


except(ZeroDivisionError, NameError):
	print("Error here")



#Else clause
def fun(a,b):
	try:
		c= ((a+b) / (a - b))
	except ZeroDivisionError:
		print("a / b is 0")

	else:
		print(c)


fun(2.0, 3.0)
fun(3,3)




#Raising Exception
try: 
	raise NameError("HI")
except NameError:
	print("An exception")
	raise