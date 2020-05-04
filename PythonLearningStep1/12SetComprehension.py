#set comprehension

nums = [1,1,1,1,1,22,2,2,2,23,4,5,6,7,8,9,6,4]
mySet1 = set()
for n in nums:
	mySet1.add(n)

print(mySet1)    #return all unique values


#comprehesnion

mySet2 = (n for n in nums)
print(mySet2)