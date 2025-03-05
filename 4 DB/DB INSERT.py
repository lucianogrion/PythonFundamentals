import sqlite3
conn = sqlite3.connect('example.db')

c = conn.cursor()

# Create table
c.execute("SELECT * FROM stocks")


personas=(("pedro",31),("Aldo",77),("pablo",14))

for nombre,edad in personas:
	c.execute("insert into personas values (?,?)", (nombre,edad))


# Save (commit) the changes
conn.commit()

# We can also close the connection if we are done with it.
# Just be sure any changes have been committed or they will be lost.
conn.close()
