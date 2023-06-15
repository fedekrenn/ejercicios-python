# Crear un programa que permita emular el registro y almacenamiento de usuarios en una base de datos. Crear el programa utilizando el concepto de funciones, diccionarios, bucles y condicionales.

# El formato de registro es: Nombre de usuario y Contraseña.
# Utilizar una función para almacenar la información y otra función para mostrar la información.
# Utilizar un diccionario para almacenar dicha información, con el par usuario contraseña (clave valor).
# Utilizar otra función para el login de usuarios, comprobando que la contraseña coincida con el usuario.


db = []


def save_user(user, password):
    data = {user: password}
    db.append(data)
    return '------\n Usuario guardado!'


def show_users():
    return db


def login_user(user, password):
    if {user: password} in db:
        return 'Acceso ok'
    else:
        return 'Usuario o contraseña incorrecto'


while True:
    option = input(
        '-----\nSelecciona una opción:\n1)Registrar usuario\n2)Ver lista de usuarios\n3)Acceder con tus datos\n4)Salir\n')
    if option == '1':
        new_user = input('Introduce el usuario:\n')
        new_pass = input('Introduce la contraseña:\n')
        print(save_user(new_user, new_pass))
    elif option == '2':
        print(f'Lista de usuarios registrados:\n {show_users()}')
    elif option == '3':
        log_user = input('Introduce el usuario:\n')
        log_pass = input('Introduce la contraseña:\n')
        print('------\n', login_user(log_user, log_pass))
    elif option == '4':
        print('Programa finalizado!')
        break
    else:
        print('------\nOpción no válida')
