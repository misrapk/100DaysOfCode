# """
# a programming languages is said to have first-class
# functions if it treats funcitons as first-class citizens.


# we need to assigne a function to a vairable

# """

# def square (n):
# 	return n*n

# f = square     #assign 

# print(f)    #first class

# #now we can use f as a functions
# print(f(5))



# #pass function as an argument in another function
# """use map"""

# """we will build our own map funciton"""
# def myMap(func, argList):
# 	result = []
# 	for i in argList:
# 		result.append(func(i))
# 	return result

# squares = myMap(square , [1,2,3,4,5])

# print(squares)



def logger(msg):

	def logMessage():
		print('log', msg)

	return logMessage   #returning function


logHi = logger('HI')
logHi()


 

