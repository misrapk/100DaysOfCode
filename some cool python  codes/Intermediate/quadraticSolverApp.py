# quadratic solver app
import cmath
#TODO: print welcom message
print("Welcome to Quadratic Solver App")
print("\nA quadratic equation is of the form ax^2 + bx + c = 0")
print("Your solution can be real or complex number")
print("A complex number has two parts: a + bj")
print("Where a is the real portion and bj is the imaginary")

n = int(input("\nHow many equations would you like to solve today? "))

#take inputs
for i in range(n):

	print("\n Solving equation #{}".format(i+1))
	print("------------------------------------------------")
	a = float(input("Enter the coefficient of x^2: "))
	b = float(input("Enter the coeeficient of x: "))
	c = float(input("Enter the constant: "))

#solve theequation 
	s1 = (-b + cmath.sqrt((b**2 - 4 * a * c))/(2 * a))
	s2 = (-b - cmath.sqrt((b**2 - 4 * a * c))/(2 * a))

	print("\nThe solution to {}x^2 + {}x + {} = 0 are: ".format(a,b,c))
	print("\n\t x1 = {}".format(s1))
	print("\n\t x2 = {}".format(s2))

print("\nThank You for using the Quadratic Equation Solver App.")