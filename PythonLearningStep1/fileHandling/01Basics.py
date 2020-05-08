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

# with open('example.txt', 'r') as f:
# 	# fContents = f.read()
# 	# print(fContents)
# 	for lin in f:
# 		print(lin, end='')
# 	# fLines = f.readlines()   #print out all th lines as a list
# 	# print(fLines)


'''reading file'''

with open('example.txt','r') as f:
	#read the 10 characters at a time
	sizeTOread= 10
	fContent = f.read(sizeTOread)
	while(len(fContent) >0):
		print(fContent, end ='*')
		fContent = f.read(sizeTOread)