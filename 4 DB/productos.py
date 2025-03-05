import sqlite3
conn = sqlite3.connect('example.db')

c = conn.cursor()

# Create table
c.execute('''CREATE TABLE productos
             (id int, nombre text, precio float)''')


productos=((1,"teclado",150),(2,"mouse",500),(3,"monitor",5500),(4,"Parlantes",float("1500.5")))

for id,nombre,precio in productos:
	c.execute("insert into productos values (?,?,?)", (id,nombre,precio))


# Save (commit) the changes
conn.commit()


conn.close()
