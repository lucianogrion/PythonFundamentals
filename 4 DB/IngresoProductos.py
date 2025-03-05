import sqlite3
conn = sqlite3.connect("productos.db")
cursor = conn.cursor()
#cursor.execute("create table productos (Id numeric primary key, Nombre text, Precio numeric)")  
while True:
    try:
        idp = float(input('Ingrese id producto '))
        nombre = str(input('Ingrese nombre del producto '))
        precio = float(input('Ingrese precio del producto '))
       
        pregunta = input('Son los datos correspondientes a id y precio correctos?, solo responda si o no: ').lower()
       
        if pregunta == 'si' or pregunta == 'yes':
            cursor.execute("INSERT INTO productos VALUES(?,?,?)", (idp, nombre, precio))
            break
        else:
            idp = float(input('Ingrese nuevamente id producto '))
            precio = float(input('Ingrese nuevamente precio del producto '))
            cursor.execute("INSERT INTO productos VALUES(?,?,?)", (idp, nombre, precio))
            break
           
   
    except ValueError:
        print('Por favor ingrese datos correctos, tipo numero para id, texto para nombre y numero para precio')
 
seleccion = cursor.execute("SELECT * from productos")
for a in seleccion:
    print("La base de datos productos contiene: \n" + str(a))
 
conn.commit()
conn.close()
