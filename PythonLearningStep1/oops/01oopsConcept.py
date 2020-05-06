# OOPs1
#classes and instances

class Employee:

	def __init__(self,first, last, pay):
		self.first = first
		self.last = last
		self.pay = pay
		self.email = first + '_' + last + '@comapny.com'

	#display the full name
	def fullName(self):
		return '{} {}'.format(self.first, self.last)


emp1= Employee('Ram', 'singh', 200)
emp2 = Employee('Sita', "maa", 342)

print(emp1)
print(emp2)	
print(emp2.email)
#print full name without method
# print('{} {}'.format(emp1.first, emp1.last))

#using function
print(emp1.fullName())