#my module
print('Imported my module...')
test = 'test string'

def findIndex(toSearch, target):
	for i, value in enumerate(toSearch):
		if value == target:
			return i

	return -1