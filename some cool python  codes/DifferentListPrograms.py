#Different List Programs

numStrings = ['15','34','12','100','120']
numInts = [15,34,12,100,120]
numFloats = [2.2, 4.0,4.6, 0.2322,1.332]
numLists = [[1,2,3],
			[4,5,6],
			[7,8,9]]


print("\n\t\tSummary Table")

print("\nThe variable numStrings is a {}.".format(type(numStrings)))
print("It contains the elements: {}".format(numStrings))
print("The element {} is a {}.".format(numStrings[0], type(numStrings)))

print("\nThe variable numInts is a {}.".format(type(numInts)))
print("It contains the elements: {}".format(numInts))
print("The element {} is a {}.".format(numInts[0], type(numInts)))

print("\nThe variable numFloats is a {}.".format(type(numFloats)))
print("It contains the elements: {}".format(numFloats))
print("The element {} is a {}.".format(numFloats[0], type(numFloats)))

print("\nThe variable numLists is a {}.".format(type(numLists)))
print("It contains the elements: {}".format(numLists))
print("The element {} is a {}.".format(numLists[0], type(numLists)))

#sorting the list
numStrings.sort()
numInts.sort()

print("\nNow Sorting numStrings and numInts...")
print("Sorted numStrings: {}".format(numStrings))
print("Sorted numInts: {}".format(numInts))

print("\nStrings are sorted alphabetically while Integers are according Numbers!!!")