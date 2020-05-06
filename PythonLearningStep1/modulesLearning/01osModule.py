#os module

import os

# print(dir(os))   #list all the functions
os.chdir('D:\\pkworkspace\\100DaysDataScience\\PythonLearningStep1\\modulesLearning')

print(os.getcwd())      #path of ur current directory

print(os.listdir())      #list the files in current directory
# os.mkdir('OsDemoFolder1')  #create directory
# os.mkdirs is used to create the deep folders
'''
	os.mkdirs('osdemo2/ossubdir')   --> create osdemo2 and inside it
	create ossubdir
	'''

#to remove dir
# os.rmdir('OsDemoFolder1')

#print all infor

# print(os.stat('OsDemoFolder'))

'''os.walk() give all the info from top to bottom approach
'''
for dirPath, dirName, fileName in os.walk('D:\\pkworkspace'):
	print('Current Path: ', dirPath)
	print('Directories: ', dirName)
	print('Files', fileName)

