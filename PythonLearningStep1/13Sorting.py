#sorting list
li = [9,1,3,6,2,7,7,32,8,3,9]

sortList = sorted(li)  #original list remain unchange
print('Orginal LIst: ',li)
# print('Sorted list: ',sortList)

li.sort()   #change the original list
print('Original: ', li)



"""sorted is used in all ds ie. list, tuple and dict
but sort is use only in list.
so its better to use sorted"""

#for tuple
tu =(9,1,3,5,7,3,8)
sortedTu = sorted(tu)
print("Sorted tuple: ", sortedTu)

#for dict
myDict = {'Ajay': 'Ram', 'Goyal': 'Laxman','Rekha': 'Sita'}
sortedmyDict = sorted(myDict)   #it will sort only keys

print("Sorted dict is : ", myDict)




#example 
num = [-6,-5,2,-1,3]

# if i want to sort its absolute vlaue then
'''use 'key as abs' to sort absolute value'''
sNum = sorted(num, key= abs)

print("Absolute: ", sNum)
