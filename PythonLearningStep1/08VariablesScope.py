""" variables scope
	local, enclosing, Gloabl , built-in

"""

x = 'global x'    #global variable

def test(z):    #local
	x = 'local x' #local variable
	print(x)    #print local x
	print(z)

# print(y)   #throw error
test('local z')

print(x)


#built in
# import builtins
# print(dir(builtins))    #give all min functions


#enclosing
def outer ():
	x = 'outer x'
	def inner():
		nonlocal x
		x = 'inner x'
		print(x)

	inner()
	print(x)

outer()


