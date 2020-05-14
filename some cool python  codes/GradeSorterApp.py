#Grade sorter app

print("Welcome to the Grade Sorter App")
print("---------------------------------------")

#input of grades
grades = []
grade = int(input("\nWhat is your first grade (0-100): "))
grades.append(grade)
grade = int(input("What is your second grade (0-100): "))
grades.append(grade)
grade = int(input("What is your third grade (0-100): "))
grades.append(grade)
grade = int(input("What is your fourth grade (0-100): "))
grades.append(grade)

print("\nYour grades are: "  + str(grades))

#sort the list:
grades.sort(reverse=True)
print("\nSorted Order of Grades(Highest to Lowest): {}".format(grades))

#remove lowest grades

print("\nThe lowest two grades will now be dropped.")
removedGrade = grades.pop()
print("Removed grade: "+ str(removedGrade))
removedGrade = grades.pop()
print("Removed grade: {}".format(removedGrade))


print("\nYour remaining grades are: {}".format(grades))
print("Nice Work! Your highest grade is : {}.".format(grades[0]))