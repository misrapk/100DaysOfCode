#Binary and Hexadecimal Convertor Program

print("Welcome to the Binary/Hexadecimal Converter App.")

#TODO: user input and generate list

maxValue = int(input("\nCompute Binary and hexadecimal upto the following decimal number: "))
decimal = list(range(1, maxValue+1))
binary = []
hexadecimal = []

for num in decimal:
	binary.append(bin(num))
	hexadecimal.append(hex(num))


print("Generating lists.... Complete!")

#TODO: get slicing index form user
print("\nUsing slicing we will now show a portion of each list.")
lowerRange = int(input("What decimal number would you like to start at: "))
upperRange = int(input("What decimal number would you like to sotp at: "))


#TODO: slice to each list individually
print("\nDecimal values from {} to {} :".format(lowerRange, upperRange))
for num in decimal[lowerRange-1 : upperRange]:
	print(num)

print("\nBinary values from {} to {} :".format(lowerRange, upperRange))
for num in binary[lowerRange-1 : upperRange]:
	print(num)


print("\nHexadecimal values from {} to {} :".format(lowerRange, upperRange))
for num in hexadecimal[lowerRange-1 : upperRange]:
	print(num)



#TODO: print entire list
input("\nPress Enter to see all values from 1 to {}.".format(maxValue))
print("Decimal----Binary----Hexadecimal")
print("--------------------------------------------")

for d, b, h in zip(decimal, binary, hexadecimal):
	print("{}----{}-----{}".format(str(d), str(b), str(h)))
	