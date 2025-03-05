meses=("enero","febrero","marzo","abril","mayo","junio",
       "julio","agosto","septiembre","octubre","noviembre","diciembre")
try:
    nromes=int(input("Ingrese un número de mes [1-12]:"))
    print(meses[nromes-1])
except IndexError:
    print("En número de mes debe ir entre 1 y 12")
