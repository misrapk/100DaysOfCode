# //writing in file
# with open('exampl2.txt','w') as f:
# 	f.write('Hello there')
# 	f.seek(0)
# 	f.write("t")

"""create copy of existing file"""
with open('example.txt','r') as rf:   #for reading original file
	with open('exampleCopy.txt','w') as wf:
		for line in rf:
			wf.write(line)
