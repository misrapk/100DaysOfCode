"""we can create our own error using exception class
"""

class myError(Exception):
	def __init__(self, value):
		self.value = value

	def __str__(self):
		return (repr(self.value))

try:
	raise(myError(3*2))


#value of exception is store in erro
except myError as error:
	print("My new exception occured: ", error.value)

print(help(Exception))    #to knwo more about Exception class
