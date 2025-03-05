archivo=open("prueba","w")
archivo.write("popapaopaopaopaopaoapo\n")
archivo.close()
archivo=open("prueba","a")
archivo.write("1\n")
archivo.write("2\n")


lista = ["uno\n", "dos\n" ,"3\n"]
archivo.writelines(lista)
archivo.close()

archivo = open("prueba","r")
saludos =archivo.readlines()
print (saludos)
archivo.close()

tupla=[10,20,30]
t1,t2,t3=tupla #unpacking

print(t1)
print(t2)
print(t3)

print("hola" , "tengo" , 34,"anios",sep=".",end="!\n")

print("soy un string muy chulo de {0} x {1}".format(15,5))
print(f"epa soy placeholder {t1} y {t2}")	
