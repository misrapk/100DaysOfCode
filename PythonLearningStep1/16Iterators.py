#iterator
"""iterator is an object that can be iterated upon and which will 
return data, one element at atime.

--> Iterable is an object, not necessarily a ds that can return
an iterator. Its primary purpose is to return all of its elements.


two methods:   __next__() --> returns iterator object itself
				used the 'for ' and 'in' keywords.
	__iter()__  ---> returns the next value.


Iterables are: list, tuples, strings dictionries and files

"""
courses = ['C++', 'Azure','Javascript', 'python']

iterator = iter(courses)
# print(iterator)
print(next(iterator))
print(next(iterator))
print(iterator.__next__())
print(next(iterator))
# print(next(iterator))   #it will throw StopIteration error



#TODO: enumerate
"""it will take any iterable and return (index,value) pair
"""

enObj = enumerate(courses)
print(list(enObj))


# iterate through enumerate

for i,v in enumerate(courses):
	print(i,v)


