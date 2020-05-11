#convert any speed to MPS rounded to 2 decimal points

""" output
Welcome to the MPH to MPS Conversion App

What is your speed in miles per hour: 10

Your speed in meters per second (MPS) is 4.47 mps.
"""



print("\nWelcome to the MPH to MPS Conversion App")

#user Input
mph = float(input("\nWhat is your speed in miles per hour: ") )


"""to convert in mps 
 			x mph = x(1609.34)/3600 mps
"""

mps = (mph * 1609.34)/3600

#round the answer
mps = round(mps,2)  #2 decimal places

print("\nYour speed in meters per second (MPS) is " + str(mps) + " mps.")