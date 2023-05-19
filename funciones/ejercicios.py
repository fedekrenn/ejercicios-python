# Escribir un programa que permita validar el ingreso a un sistema. Se deberá solicitar el ingreso por teclado de nombre de usuario y contraseña. Será valido como nombre de usuario “admin” y como contraseña “1234”. Si el ingreso es correcto deberá mostrar por pantalla el mensaje “Ingreso exitoso”.

# Opcional 1: permitir como usuario valido también su propio nombre y su propia contraseña.

# Opcional 2: solamente permitir el ingreso incorrecto de los datos 3 veces, luego de ello, no permitir más ingresos y mostrar por pantalla “Cuenta bloqueada”.

# 2) Mostrar por pantalla el siguiente menú:

# CAJERO AUTOMATICO ISPC Listado de opciones:
#   1) Ingreso de dinero
#   2) Extracción de dinero
#   3) Consulta de saldo
#   4) Salir
#  Ingrese su selección:
#
# El programa deberá mostrar luego del ingreso de cada opción “Usted ha seleccionado la opción x”, por ejemplo, en el caso de ingresar un 1, deberá mostrar por pantalla “Usted ha seleccionado la opción 1” y así sucesivamente. Al seleccionar la opción 4 se debe terminar la ejecución del programa.

# Opcional: Validar que solamente se pueda ingresar un número del 1 al 4. En caso de ingresar un número fuera de ese rango, mostrar por pantalla “Opción incorrecta”.

# 3) Deberá continuar con el ejercicio 2 y escribir la lógica del cajero automático de la siguiente manera.

# a. Su saldo inicial será de $10000.
# b. Al seleccionar la opción 1 se pedirá al usuario que ingrese un importe por teclado el cual se sumará a su saldo inicial.
# c. De la misma manera al seleccionar la opción 2, se solicitará un importe por teclado el cual se restará al saldo inicial.
# d. Con la opción 3 se consultará su saldo actual.
# e. En todo momento se deberá contralar que no se pueda extraer dinero, si no se cuentan con fondos suficientes.

def isLogged():
    counter = 0

    default_user = "federico"
    default_password = "admin"

    while counter < 3:
        user = input('Ingrese el nombre de usuario:\n')
        password = input('Ingrese contraseña:\n')

        if (user == 'admin' and password == '1234') or (user == default_user and password == default_password):

            print('-----\nIngreso exitoso\n-----')
            return True
        else:
            print('-----\nUsuario o contraseña incorrecto\n-----')
            counter += 1

    if counter >= 3:
        print('-----\nCuenta bloqueada\n-----')
        return False


if isLogged():
    print('-----------')
    print('CAJERO AUTOMATICO ISPC\n Listado de opciones:\n1) Ingreso de dinero\n2) Extracción de dinero\n3) Consulta de saldo\n4) Salir ')

    initial_amount = 1000

    while True:
        option = int(input('Ingrese su selección:\n'))

        if option == 1:

            amount_to_add = int(input('Ingrese el monto a agregar:\n'))
            initial_amount += amount_to_add

            print(
                f'Operación realizada con éxito! El total de su cuenta es {initial_amount}')
        elif option == 2:

            amount_to_subtract = int(input('Ingrese el monto a retirar:\n'))
            if amount_to_subtract > initial_amount:

                print('No cuentas con fondos suficientes')
            else:
                initial_amount -= amount_to_subtract

                print(
                    f'Realizado! Extrajiste correctamente {amount_to_subtract}, el total de tu cuenta es:   {initial_amount}')
        elif option == 3:
            print(f'El saldo de su cuenta es: {initial_amount}')
        elif option == 4:
            print('Ha salido correctamente')
            break
        else:
            print('-----------\nOpción no válida\n-----------')
