# bitwise operator
'''use to compare and perform logical operations on binary
numbers


Number    	Binary
201 		1100 1001
15 			0000 1111
'''

""" & operator: return 1 if both are 1
	| operator : return 1 if one of the input is 1
	^  operator: (XOR) return one if any  one input is 1
					if both is one then return 0;


	201 & 45 == 9

	Input 1 	201 	1100 1001
	Input 2     15 		0000 1111
	& Output 	9 		0000 1001


"""
print(201 & 15)
print(201 | 15)
print(201 ^ 15)
print(15 >> 2)
print(15 << 2)

