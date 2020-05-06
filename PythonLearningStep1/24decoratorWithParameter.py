# def decorators(*args, **kwargs):
# 	def inner(func):
# 		'''
# 			do operations with func
# 		'''
# 		return func
# 	return inner   

# @decorators(params)
# def func():
# 	'''
# 		function implementation
# 	'''
# 	



def decorator_func(func):
	print("Insinde decorator")

	def inner(*args, **kwargs):
		print("Inside inner function")
		print("Decorated the function")

		func()

	return inner

'''decorator without parameter'''

# @decorator_func
# def func_to():
# 	print("Inside actual function")

# func_to()



'''decorator with parameter
''' 
def func_to():
	print("inside actual function")

decorator_func(func_to)()



#Example

def decorator(*args, **kwargs):
	print("inside decorator")

	def inner(func):
		print("inside inner function")
		print("i like", kwargs['l'])

		func()

	#return inner function
	return inner


@decorator(l = "Hello there")

def myFun():
	print("Inside actual function")