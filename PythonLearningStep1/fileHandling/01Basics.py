# 01 baiscs
# f = open('example.txt')   #open file in current directory 
''' also 
f = open('example.txt','r')

'''
# print('Name of file : ',f.name)
# print('Mode of file : ', f.mode)


# #also close the file
# f.close()


'''we can also open file using 
with open('filename', mode) as var:
	operation inside the file

after this the file will automatially close
'''

with open('example.txt', 'r') as f:
	# fContents = f.read()
	# print(fContents)
	fLines = f.readlines()
	print(fLines)