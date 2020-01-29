# Write an immutable function that merges the following inputs into a single list. 
# (Feel free to use the space below or submit a link to your work.)

# Inputs
# - Original list of strings
# - List of strings to be added
# - List of strings to be removed

# Return
# - List shall only contain unique values
# - List shall be ordered as follows
# --- Most character count to least character count
# --- In the event of a tie, reverse alphabetical

# Other Notes
# - You can use any programming language you like
# - The function you submit shall be runnable

# For example:

# Original List = ['one', 'two', 'three',]
# Add List = ['one', 'two', 'five', 'six]
# Delete List = ['two', 'five']
# Result List = ['three', 'six', 'one']*

def immutableFunction():
	origList = ("one","two","three")
	addList = ("one","two","five","six")
	delList = ("two","five")
	print("Before any modifications",origList)
	#Add list to Origional
	modifiedList = origList + addList
	dupFreeList = ("temp",)
	print("With added List",modifiedList)
	# Remove duplicate elements
	for index in modifiedList:
		if index not in dupFreeList:
			#create temporary tuple containing valid entry
			tupleIndex = (index,)
			dupFreeList+= tupleIndex
	dupFreeList = dupFreeList[1:]
	print("Removed Duplicates", dupFreeList)

	# Remove delete list elements
	finalList = ("temp",)
	for index in dupFreeList:
		if index not in delList:
			tupleIndex = (index,)
			finalList+= tupleIndex
	finalList= finalList[1:]
	print("Remove Deletion List",finalList)
	
	# Sort the final list
	if len(finalList) <= 0:
		print("Final List is Empty")
		return
	elif len(finalList) == 1:
		print("List equals one")
		return(finalList)
	# List must be sorted use bubble sort
	else:
		print("Sort List")
		finalSortedList = bubbleSortRevAlphabetical(finalList)
		print(finalSortedList)
		return finalSortedList



def bubbleSortRevAlphabetical(sortList):
	for i in range (0, len(sortList) -1):
		for j in range (0, len(sortList) - 1 - i):
			#set temporary list to check if reverse alphabetical
			reverseAlphaTemp = (sortList[j],sortList[j+1])
			sortedReverseAlphaTemp=(sorted(reverseAlphaTemp,reverse=True))
			#bubble sort
			if len(sortList[j]) < len(sortList[j+1]) or  (len(sortList[j]) == len(sortList[j+1]) and (tuple(sortedReverseAlphaTemp) != reverseAlphaTemp)):
				leftswap = (sortList[j+1],)
				rightswap = (sortList[j],)
				sortList = sortList[:j] + leftswap + rightswap + sortList[j+2:]
	return(sortList)



print(immutableFunction())

