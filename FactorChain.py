# A factor chain is a list where each previous element is a factor 
# of the next consecutive element. The following is a factor chain:

# Create a function that determines whether or not a list is a factor chain.
# Input(s): [numbers]
# return: Boolean

def FactorChain(lst):
	for numbers in range(0,len(lst)-1):
		print(lst[numbers+1],lst[numbers])
		if(lst[numbers+1] % lst[numbers] != 0):
			return False
	return(True)

l1 = [1, 2, 4, 8, 16, 32]
l2 = [1, 1, 1, 1, 1, 1]
l3 = [2, 4, 6, 7, 12]
l4 = [10,1]
print(FactorChain(l4))