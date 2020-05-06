from datetime import date

class Person:
	def __init__(self, name , age):
		self.name = name
		self.age = age

	#class method
	@classmethod
	def fromBirthYear(cls, name, year):
		return cls(name, date.today().year -year)

	#static method
	@staticmethod
	def isAdult(age):
		return age>18


p1 = Person('Rahul',21)
p2 = Person.fromBirthYear('Rahul',1995)

print(p1.isAdult(19)) 
print(p1.age)
print(p2.age)