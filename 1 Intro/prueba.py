num = int(input())

def fib(n):
    if n < 2:
        return n
    else:
        # fn = fn-1 + fn-2
        return fib(n-1) + fib(n-2)
        
def fibonacci(n):
	#complete the recursive function
	acumprev=0
	acumact=1
	for i in range(n):
		print(fib(i))
			

fibonacci(num)
