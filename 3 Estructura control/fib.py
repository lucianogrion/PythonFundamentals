#def multiplos(maximo)
def fib(cant):
	l=[0,1]
	for numero in range(1,cant+1,1):
		acumulador=0
		for acum in range(1,numero,1):
			acumulador=acumulador+acum
		l.append(acumulador)	
	return l



print(fib(10))
