import sqlite3

conn = sqlite3.connect('alumnos.db')

cursor = conn.cursor()

cursor.execute('CREATE TABLE alumnos(id INT, nombre TEXT, apellido TEXT)')

cursor.execute("INSERT INTO alumnos VALUES(1,'MIGUEL', 'RODRIGUEZ')")
cursor.execute("INSERT INTO alumnos VALUES(2,'MARCOS', 'PEREZ')")
cursor.execute("INSERT INTO alumnos VALUES(3,'RAFAEL', 'SILVA')")
cursor.execute("INSERT INTO alumnos VALUES(4,'JOSE', 'PULIDO')")
cursor.execute("INSERT INTO alumnos VALUES(5,'CARLOS', 'ROJAS')")
cursor.execute("INSERT INTO alumnos VALUES(6,'EDUARDO', 'GONZALEZ')")
cursor.execute("INSERT INTO alumnos VALUES(7,'LUISA', 'RINCON')")
cursor.execute("INSERT INTO alumnos VALUES(8,'PAOLA', 'HURTADO')")

conn.commit()

cursor.execute("SELECT * FROM alumnos_list WHERE nombre = 'JOSE'")

datos = cursor.fetchall()

print(datos)


cursor.close()
conn.close()
