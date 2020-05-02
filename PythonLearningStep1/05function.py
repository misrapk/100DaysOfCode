#function
# def helloFun():
# 	# print('Hello Function!')
# 	# print('Hi')
# 	return 'Hello Funciton'

# def fun2(greeting, name ='You'):
# 	return '{}, {}'.format(greeting, name)

# print(helloFun())
# print(fun2('Hi'))


#allowing us to accept an arbitary number of positional keyword arguments # def fun3(*args, **kwargs):
# 	print(args)   #tuple
# 	print(kwargs)  #dictionary

# # fun3('Math', 'art', name='John', age = 22)


# courses = ['math','art']
# info = {'name':'Pk', 'age':22}
# # fun3(courses, info)

# fun3(*courses, **info)  #unpack the tuple and dict



monthDays = [0,31,28,31,30,31,30,31,31,30,31,30,31]

def isLeap(year):
	"""Return true for leap years,
	flase for non leap years"""
	return year % 4 ==0 and(year%100 !=0 or year % 400 ==0)

def daysInMonth(year, month):
	"""return number of days in a month"""
	if not 1 <=month <=12:
		return 'invalid month'
 
	if month ==2 and isLeap(year):
		return 29

	return monthDays[month]


# print(isLeap(2020))
print(daysInMonth(2016,2))