def fibonacci(value):
	#python inital fib sequences
	if(value < 0):
		return -1
	elif(value == 0):
		return 0
	elif(value == 1 or value == 2):
		return 1
	else:
		return(fibonacci(value-1)+fibonacci(value-2))


def main():
	for i in range(0,14):
		print(fibonacci(i))

main()