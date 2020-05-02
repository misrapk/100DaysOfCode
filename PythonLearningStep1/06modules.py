"""if module is in same dir then directoly
import the module"""


# import mymodule 
# import mymodule as mm
# from mymodule import findIndex,test
from mymodule import *   #import everything 

courses = ['history', 'math', 'physics','cse']

# index = mymodule.findIndex(courses, 'math')
# index = mm.findIndex(courses, 'physics')
index = findIndex(courses, 'physics')

print(index)
print(test)



""" when we import it checks multiple location

locations are sys.path
we can see using import sys   print(sys.path)


order of dire: 
dir in which the code is writtend--> python path env variable
-->> standard library dir(DLLs) -->>> sitePackages
"""
import sys
print(sys.path)


"""to add the path in sys use:
import sys
sys.path.append('path of module')
"""