num = int(input())


def fibonacci(n):
	#complete the recursive function
	acumprev=0
	acumact=1
	for i in range(n):
		if (i<2):
			print (i)
		else:
			print (acumact)
			acumprev = acumact
			acumact = acumprev+acumact
			

fibonacci(num)
