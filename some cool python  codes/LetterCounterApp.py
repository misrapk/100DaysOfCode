
#count the letter in a message

"""OUTPUT
Welcome to the Letter Counter App

What is your name: peeysuh
Hello, Peeysuh!
I will count the number of times that a specific lettr occurs in a message.

Please enter a message: hello hw are u doing here
Which letter would you like to count the occurence of : e

Peeysuh, your message has 4 e's in it.
"""

print("Welcome to the Letter Counter App")

#get user input
name = input("\nWhat is your name: ").title().strip()

print("Hello, "+ name+"!")

print("I will count the number of times that a specific lettr occurs in a message.")
message = input("\nPlease enter a message: ")
letter = input("Which letter would you like to count the occurence of : ")

message = message.lower()

#lower the letetr
letter = letter.lower()

#get the count to display
letterCount = message.count(letter)
print("\n" + name + ", your message has " + str(letterCount) + " "+ letter + "'s in it.")
