#program to convert Farenhite into celsius, kelvin 

"""output
Welcome to the Temperature Conversion Program
What is the given temperature in degrees Fahrenheit: 121

Degrees Fahrenheit:     121.0
Degrees Celsius:        49.4444
Degrees Kelvin:         322.5944
"""



#welcome message
print("\nWelcome to the Temperature Conversion Program")

#user input
fahren = float(input("What is the given temperature in degrees Fahrenheit: "))

#converstion

cel = (fahren - 32) / 1.80
# kelv = ((5*(fahren-32))/9) + 273.15
kelv = cel + 273.15


#convert to 4 decimal places
fahren = round(fahren, 4)
cel = round(cel,4)
kelv = round(kelv, 4)


#output in aligned format
#summary table
print("\nDegrees Fahrenheit:\t" + str(fahren))
print("Degrees Celsius:\t" +  str(cel))
print("Degrees Kelvin:\t\t" + str(kelv))
