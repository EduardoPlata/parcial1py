import mysql.connector
import hashlib

db = mysql.connector.connect(
    host='localhost',
    user='root',
    password='1234',
    database='blog',
    port=3306
)


def registrarUsuario(usuario):
  
    cursor=db.cursor()
    cursor.execute('''
        insert into usuarios(nombre,email,contrasena)
        values (%s,%s,%s)''',
        (usuario['nombre'],
        usuario['email'],
        usuario['contrasena']))
    ''' cursor.execute('        insert into usuarios(nombre,email,contrasena)        values (%s,%s,%s)',        (dato)) '''
    db.commit()
    cursor.close()


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


opcion = 1

usuarios = []

while opcion !=0:

    print('Selecciona una opción:')
    print('1. Registrar usuario')
    print('2. Inicio de sesión') 
    print('0. Salir') 

    opcion = int(input())

    if opcion == 1:
        nombre = input('Ingrese nombres del usuario: ')
        apellido = input('Ingrese apellidos del usuario: ')
        correo = input('Ingrese el correo del usuario: 
        contrasena = input('Ingrese contraseña, mínimo 8 caracteres, una mayúscula y un carácter especial: ')
        ')

        #.append es para agresar en lo ultimo de la lista
        contactos.append({
            'nombre': nombre,
            'apellido': apellido,
            'correo': correo,
            'contrasena': contrasena,

        })

        input('Usuario guardado correctamente. Presione enter para continuar')
    elif opcion ==2:
        correo = input('Ingrese el correo del usuario: ')
        contrasena = input('Ingrese contraseña: ')
        print(usuarios)


        h = hashlib.new("sha512",b"Unipython")

    




CREATE TABLE usuarios(  
    id int NOT NULL primary key AUTO_INCREMENT comment 'primary key',
    nombre VARCHAR(255) not NULL,
    email VARCHAR(255) NOT NULL,
    contrasenaa VARCHAR(50) not NULL
) ;