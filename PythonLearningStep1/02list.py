# #list

courses = ['JS', 'C++', 'Python','DataScience']

# print(courses)

# print(len(courses))

# #printspecific element
# print(courses[3])
# print(courses[-1])  #lastItem

# #print the elements in range[x:y] -->not including y
# #slicing
# print(courses[0:2])
# print(courses[2:])

# #add element in list
# courses.append('Art')

# courses.insert(2,'Science')  #add at index 2

# courses2 = ['Hindi','English']

# #we want to add courses2 to courses
# # courses.insert(0,courses2)   #add the list at begining

# courses.extend(courses2) #add the element of list2 in list1 at the end

# print(courses)
# print(courses[0])

# courses.pop()
# courses.sort()

# print(courses)

nums =[1,4,6,2,5,3]
# nums.sort()
# nums.sort(reverse=True)
print(nums)

# for i in nums:
	# print(i)

for couse,index in enumerate(nums, start=1):
	print(couse,index)

course_str = ', '.join(courses)
print(course_str)


