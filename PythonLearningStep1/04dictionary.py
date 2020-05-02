#dictionary
#dictionary are like HashMap

student = {'name': 'Pk', 
			'age': 20,
			'courses': ['Math', 'DP']} 



# print(student['courses'])

#we can acess in another way
# print(student.get('abc', 'NotFound'))

# student['phone'] = '34322344' #update the dict
# print(student.get('phone'))
# print(student)


#update
student.update({'name': 'John'})


# delete student age
# del student['age']
# print(student)

# print(student.keys())
# print(student.values())
# print(student.items())

for key,value in student.items():
	print(key, value)