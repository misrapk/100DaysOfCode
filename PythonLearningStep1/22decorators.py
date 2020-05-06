# #Decorators


# def outerFun():
# 	message = 'HI'

# 	def innerFun():
# 		print(message)
# 	# return innerFun()     #TYPE1
# 	return innerFun    #return without execution    #tYPE 2

# # outerFun()     #TYPE 1

# myFun = outerFun()     #tYPE 2
# myFun()  



#dECROATOR FUNCTION	
def decoratorFun(originalFun):
	def wrapperFun():
		print("wrapper exectued before".format(originalFun.__name__))
		return originalFun()
	return wrapperFun


"""syntax 1"""
# def display():
# 	print("here is display in decroator")

# decoratedDisplay = decoratorFun(display)
# decoratedDisplay()


"""syntax 2"""
@decoratorFun
def display():
	print("display using @")


display() 


#another expample

def helloDeco(func):

	#wrapper func
	def inner1():
		print("This is before func() execution")

		func()

		print("This is after func() execution")

	return inner1


def funToUsed():
	print("This is inside FUn()")

funVar = helloDeco(funToUsed)

funVar()




