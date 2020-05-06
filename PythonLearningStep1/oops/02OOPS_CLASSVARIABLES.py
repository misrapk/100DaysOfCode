class Student:
	#class variable
	stream = 'cse'

	#constructor
	def __init__(self,roll):
		
		#instance variable
		self.roll = roll

#objects

a = Student(101)
b = Student(102)

print(a.stream)
print(b.stream)
print(a.roll)

#accesing class elements using class name
print(Student.stream)



'''Data hiding
In Python, we use double underscore (Or __) before
 the attributes name and 
those attributes will not be directly visible outside.
'''

class MyClass:
	__hiddenVar = 0

	def add(self, incre):
		self.__hiddenVar += incre
		print(self.__hiddenVar)


myOb = MyClass()
myOb.add(2)
myOb.add(4)

print(myOb.__hiddenVar)