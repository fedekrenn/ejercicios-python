# Escribir un programa que permita validar el ingreso a un sistema. Se deberá solicitar el ingreso por teclado de nombre de usuario y contraseña. Será valido como nombre de usuario “admin” y como contraseña “1234”. Si el ingreso es correcto deberá mostrar por pantalla el mensaje “Ingreso exitoso”.

# Opcional 1: permitir como usuario valido también su propio nombre y su propia contraseña.

# Opcional 2: solamente permitir el ingreso incorrecto de los datos 3 veces, luego de ello, no permitir más ingresos y mostrar por pantalla “Cuenta bloqueada”.

counter = 0

while counter < 3:
    user = input('Ingrese el nombre de usuario:\n')
    password = input('Ingrese contraseña:\n')

    if user == 'admin' and password == '1234':
        print('Ingreso exitoso\n')
        break
    else:
        print('Usuario o contraseña incorrecto\n')
        counter += 1

if counter >= 3:
    print('Cuenta bloqueada')