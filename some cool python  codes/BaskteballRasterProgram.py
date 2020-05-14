#Basketball ROster Program

print("Welcome to the Basketball Raster Program")

point = input("Who is your point guard: ").title()
shooting = input("Who is your shooting guard: ").title()
small = input("Who is you small forward: ").title()
power = input("Who is your power forward: ").title()
center = input("Who is your center: ").title()

print("\n\t\tYour starting 5 for the upcoming basketball season")
print("\t\t\tPoint Guard: \t\t{}".format(point))
print("\t\t\tShooting Guard: \t{}".format(shooting))
print("\t\t\tSmall Forward: \t\t{}".format(small))
print("\t\t\tPower Forward: \t\t{}".format(power))
print("\t\t\tCenter: \t\t{}".format(center))

print("\nOh no! {} is injured.".format(small))
print("Your roster only has 4 players.")
small = input("Who will take {}'s spot? ".format(small)).title()
print("\n\t\tYour updated starting 5 for the upcoming basketball season")
print("\t\t\tPoint Guard: \t\t{}".format(point))
print("\t\t\tShooting Guard: \t{}".format(shooting))
print("\t\t\tSmall Forward: \t\t{}".format(small))
print("\t\t\tPower Forward: \t\t{}".format(power))
print("\t\t\tCenter: \t\t{}".format(center))

print("\nGood Luck {} you will do great!".format(small))
print("Your roster now has 5 players.")
