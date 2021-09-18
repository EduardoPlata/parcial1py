import mysql.connector
import hashlib
import re

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

     
        contactos.append({
            'nombre': nombre,
            'apellido': apellido,
            'correo': correo,
            'contrasena': contrasena,

        })
        input('Usuario guardado correctamente. Presione enter para continuar')

    elif opcion ==2:
        correo = input('Ingrese el correo del usuario: ')

        correos = [correo]
 
        for correo in correos:
        print("Probando si '{}' es válido...{}".format(correo, es_correo_valido(correo)))


        contrasena = input('Ingrese contraseña: ')        

        def validarContrasena(contrasena):
            if 8 <= len(contrasena) <= 16:
                if re.search('[a-z]', contrasena) and re.search('[A-Z]', contrasena):
                    if re.search('[0-9]', contrasena):
                        if re.search('[$@#]', contrasena):
                             return True    
            return False        

        print(validarContrasena(clave))
      


    



