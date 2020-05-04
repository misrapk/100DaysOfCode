#creating custom iterator

class counter(object):
	def __init__(self, start, end):
		#initialize the obje
		self.current = start
		self.end = end

	def __iter__(self):
		#return itself as an iterator objec
		return self

	def __next__(self):
		#return next element
		if self.current > self.end:
			return StopIteration

		else: 
			self.current += 1
			return self.current -1


#create new instance of class and initialse value
c = counter(1,5)

for element in c:
	print(element)