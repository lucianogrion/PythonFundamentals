
# Crear un bucle que almacene en una variable la suma de todos los elementos numéricos de una lista, con excepción del último

lista=[10,20,30,40,50]
i=0
acum=0;
for elem in lista:
	
	if i<len(lista)-1:
		acum=acum+elem
	i=i+1
print(acum)	
		
