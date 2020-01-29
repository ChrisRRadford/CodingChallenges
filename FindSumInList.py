#Pair to sum
# Given
# - list of numbers
# - target sum
# - return True or False and print Numbers that sum

# ordered in ascending ordered
# must be a pair of numbers
# negatives possbile 

def findSum(givenList,target):
	leftIndex = 0
	rightIndex = len(givenList)-1
	print(leftIndex,rightIndex)
	sumCheck = None
	while(leftIndex <= rightIndex):
		sumCheck = givenList[leftIndex] + givenList[rightIndex]
		print(givenList[leftIndex],givenList[rightIndex],sumCheck)
		if( sumCheck == target):
			print("Match found",givenList[leftIndex], givenList[rightIndex])
			return(True)
		elif(sumCheck > target):
			rightIndex-=1
		else:
			leftIndex+=1
	print("No pair found to sum to target value")
	return(False)

list1 = [1,2,3,9]
list2 = [1,2,4,4]
target = 8
findSum(list2,target)