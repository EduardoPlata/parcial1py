import mysql.connector

db = mysql.connector.connect(
    host='localhost',
    user='root',
    password='1234',
    database='blog',
    port=3306
)



def crearUsuario(nombre, email, contrasena):
    cursor = db.cursor()

    cursor.execute('''inser into
        usuarios(nombre, email, contrasena)
        values(%s, %s, %s)''', (
            nombre,
            email, contrasena
            ))

    #Creacion, modificaion, eliminacio de datos
    # => db.commit()

    cursor.close()




cursor = db.cursor()

cursor.execute('select * from usuarios')

print(cursor.fetchall())