#generator object is like list comprehension 
#but it does not store the list in memory.

numbers = (num for num in range(10))    #generator

numbers2 = [num for num in range(10)]    #list comprehension

print(type(numbers))
print(type(numbers2))

# for n in numbers:
	# print(n)

print(list(numbers))



#using function

def sqNumber(nums):
	for i in nums:
		yield (i + 1)


myNum = sqNumber([1,2,3,4,5])
print(next(myNum))

for num in myNum:
	print(num)


print(type(lambda x: x+1))