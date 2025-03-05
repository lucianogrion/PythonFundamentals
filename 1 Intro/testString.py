txt = input()
#tu código va aquí
spliteado = txt.split(' ')
mayor=0
palab=""
for i in spliteado :
    if (mayor<len(i)):
        mayor=len(i)
        palab=i
print(palab)
