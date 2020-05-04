nums = [1,2,3,4,5,6,7,8,9,10]


# #i want 'n' for each 'n' in nums 
# myList =[]
# for n in nums:
# 	myList.append(n)
# print(myList)



# #list comprehension
# myList1 = [n for n in nums]

# print(myList1)

#TODO: i want 'n*n' for each 'n' in nums
myList = []
for n in nums:
	myList.append(n*n)
print(myList)


#in list comprehension
myList2 = [n*n for n in nums]
print(myList2) 





#TODO : i want n for each n in nums if n is even
myList4  = []
for n in nums:
	if n%2 ==0:
		myList4.append(n)
print(myList4)


#using compre
myListC = [n for n in nums if n%2==0]
print(myListC)


#TODO: i want a (letter, num) pair for each letter in 'abcd' and each number in '0123'
myLetterNumList = []
for letter in 'abcd':
	for num in range(4):
		myLetterNumList.append((letter, num))

print(myLetterNumList)


myLetterNumList2 = [(l,n) for l in 'abcd' for n in range(4)]
print(myLetterNumList2)