import sqlite3
conn = sqlite3.connect('example.db')

c = conn.cursor()

# Create table
c.execute("SELECT * FROM personas")

resultado = c.fetchone()
print(resultado)
print(type(resultado))


resultado = c.fetchall()
print(resultado)
print(type(resultado))
print("AHORA CON EL FOR:")
for nombre,edad in resultado:
	print ( f"Nombre:{0} Edad:{1}",nombre, edad)


# Save (commit) the changes
conn.commit()

# We can also close the connection if we are done with it.
# Just be sure any changes have been committed or they will be lost.
conn.close()
