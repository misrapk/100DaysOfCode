#multiplication/Exponent Table

print("Welcome to the Multiplication/Exponent Table App")

name = input("\nHello, what is your name: ").title().strip()
num = float(input("So, What number would you like to work with: "))
message = name + ", Math is cool"



print("\nMulitplication table for {}".format(num))

for i in range(1,10):
	print("{} * {} = {}".format(i, num, round(i*num, 4)))

print("\nExponent Table For {}".format(num))

for i in range(1,10):
	print("{} ** {} = {}".format(num, i, round(num**i,4)))


print("\n"+message)
print("\t"+message.lower())
print("\t\t" + message.upper())
print("\t\t\t" + message.lower())