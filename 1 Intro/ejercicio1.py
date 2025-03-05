print("hello")


b=200

a= int(input("ingrese valor a: "))

if a>b:
	print("a>200")
else:
	print("es menor a 200")
	
	
if a<b:
	print("a<200")

print ("fin if"	)


lista=[12,13,14,15]
lista[0]=11
lista.append(16)

valor= lista.pop(0)
print (lista)
print (valor)


print(list(range(5)))
print(list(range(0,5)))
print(list(range(0,5,1)))
