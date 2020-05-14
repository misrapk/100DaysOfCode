# //Favourite Teacher List

print("Welcome to the Favourite Teachers Program")

#input
print("\nEnter the name of favourtie teachers (highest to lowest):")
favTeacher = []
favTeacher.append(input("Who is your first favorite teacher: ").title())
favTeacher.append(input("Who is your second favorite teacher: ").title())
favTeacher.append(input("Who is your third favorite teacher: ").title())
favTeacher.append(input("Who is your fourthS favorite teacher: ").title())
#sorting of list
print("\nYour favourite teachers ranked are: {}".format(favTeacher))
print("Your favorite teachers alphabetically are: ")
alpha = sorted(favTeacher)
print(alpha)
print("Your favorite teachers in reverse aplhabetical order are: ")
alpha = sorted(favTeacher, reverse=True)
print(alpha)

#top teachers
print('\nYour top two teachers are: {} and {}'.format(favTeacher[0], favTeacher[1]))
print("Your next two favorite teachers are: {} and {}.".format(favTeacher[2],favTeacher[3]))
print("Your last favorite teacher is {}".format(favTeacher[-1]))
print("You have total of {} favorite teachers.".format(len(favTeacher)))

#TODO : operations
print("\nOOPS!!! {} is no longer your first favorite teacher.".format(favTeacher[0]))
teacher = input("Who is your new FAVORITE teacher: ")
favTeacher.insert(0,teacher)

#again sort and print
print("\nYour favourite teachers ranked are: {}".format(favTeacher))
print("Your favorite teachers alphabetically are: ")
alpha = sorted(favTeacher)
print(alpha)
print("Your favorite teachers in reverse aplhabetical order are: ")
alpha = sorted(favTeacher, reverse=True)
print(alpha)

#top teachers
print('\nYour top two teachers are: {} and {}'.format(favTeacher[0], favTeacher[1]))
print("Your next two favorite teachers are: {} and {}.".format(favTeacher[2],favTeacher[3]))
print("Your last favorite teacher is {}".format(favTeacher[-1]))
print("You have total of {} favorite teachers.".format(len(favTeacher)))

#remvoe teahcer

teacher = input("\nWhich teacher would you like to remove from your list: ").title()
favTeacher.remove(teacher)

#again sort and print
print("\nYour favourite teachers ranked are: {}".format(favTeacher))
print("Your favorite teachers alphabetically are: ")
alpha = sorted(favTeacher)
print(alpha)
print("Your favorite teachers in reverse aplhabetical order are: ")
alpha = sorted(favTeacher, reverse=True)
print(alpha)

#top teachers
print('\nYour top two teachers are: {} and {}'.format(favTeacher[0], favTeacher[1]))
print("Your next two favorite teachers are: {} and {}.".format(favTeacher[2],favTeacher[3]))
print("Your last favorite teacher is {}".format(favTeacher[-1]))
print("You have total of {} favorite teachers.".format(len(favTeacher)))
