#nested functions
def outer():
	#inner
	def inner():
		print("inner functions i'm")

	print("I am outer functions")

	inner()

# inner()    #not in scope
outer()



#Lambda funcitons

# lambda arguments: expression

def square(n):
	return n*n


#lambda is
sqLambda = lambda n : n * n

print(square(23))
print(sqLambda(23))



#map function

num = [1,2,3,4,5]
squares = map(lambda n: n**2, num)

print(list(squares))

