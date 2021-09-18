import mysql.connector
print('Iniciando')
db = mysql.connector.connect(
    host='localhost',
    user='root',
    password='1234',
    database='blog',
    port=3306
)
def registrarUsuario(nombre,email,contrasenna):
    cursor=db.cursor()
    cursor.execute('''
        insert into usuarios(nombre,email,contrasena)
        values (%s,%s,%s)''',
        (nombre,
        email,
        contrasenna))

    # Creacion, Modificacion, eliminacion de datos
    db.commit()

    #cerrar cursor
    cursor.close()


registrarUsuario('eduardo','eduardplatt77@gmail.com','3142051954')

cursor =db.cursor()

cursor.execute('select *from usuarios')
usuarios = cursor.fetchall() 
print(usuarios)
