# Realice un programa que solicite dos letras ingresadas por el usuario y verifique si son iguales o no, mostrando un mensaje.

letter1 = input("Ingrese una letra: ")
letter2 = input("Ingrese otra letra: ")

if letter1 == letter2:
    print("Las letras son iguales")
else:
    print("Las letras son diferentes")


# Hacer un programa que permita decidir si dos palabras son iguales o  diferentes. Mostrar mensaje por pantalla.

word1 = input("Ingrese una palabra: ")
word2 = input("Ingrese otra palabra: ")

if word1 == word2:
    print("Las palabras son iguales")
else:
    print("Las palabras son diferentes")


# Realizar un programa que permita ingresar “f” o “m” y determinar si vota en mesa femenina o masculina.

vote = input("Ingrese su genero (f/m): ")

if vote == "f":
    print("Vota en mesa femenina")
elif vote == "m":
    print("Vota en mesa masculina")
else:
    print("Genero no valido")


# Realice un programa que lea dos números y diga cuál es el mayor.

num1 = int(input("Ingrese un numero: "))
num2 = int(input("Ingrese otro numero: "))

if num1 > num2:
    print("El numero mayor es: ", num1)
elif num2 > num1:
    print("El numero mayor es: ", num2)
else:
    print("Los numeros son iguales")


# Realice un programa que cambie pesos a dólares. Mejórelo, añadiendo el cambio de dólares a pesos y que sea el usuario quién decida qué tipo de cambio quiere, si de dólares a pesos o viceversa.

print("1. Cambiar pesos a dolares")
print("2. Cambiar dolares a pesos")

option = int(input("Ingrese una opcion: "))
amount = float(input("Ingrese el monto: "))

VALOR_DOLAR = 465

if option == 1:
    print("El monto en dolares es: ", amount / VALOR_DOLAR)
elif option == 2:
    print("El monto en pesos es: ", amount * VALOR_DOLAR)
else:
    print("Opcion no valida")


# Realice un programa donde el usuario ingrese su edad. Si es mayor de 16 años, muestre un mensaje diciendo “puede votar”, sino “no vota”.

age = int(input("Ingrese su edad: "))

if age >= 18:
    print("Puede votar")
else:
    print("No puede votar")


# Introducir los lados de un triángulo y visualizar por pantalla si dicho triángulo es equilátero, isósceles o escaleno.

side1 = int(input("Ingrese el primer lado: "))
side2 = int(input("Ingrese el segundo lado: "))
side3 = int(input("Ingrese el tercer lado: "))

if side1 == side2 and side2 == side3:
    print("El triangulo es equilatero")
elif side1 == side2 or side2 == side3 or side1 == side3:
    print("El triangulo es isosceles")
else:
    print("El triangulo es escaleno")


# Realice un programa que le permita al usuario simular el pago ingresando el importe y la forma de pago:
# • Contado (1): se aplica un descuento del 10% al importe
# • Tarjeta (2): se aplica un interés de 10%
# • Débito (3): se aplica un descuento del 5%

amount = float(input("Ingrese el importe: "))
payment = int(
    input("Ingrese la forma de pago (1: Contado, 2: Tarjeta, 3: Debito): "))

if payment == 1:
    print("El importe a pagar es: ", amount * 0.9)
elif payment == 2:
    print("El importe a pagar es: ", amount * 1.1)
elif payment == 3:
    print("El importe a pagar es: ", amount * 0.95)
else:
    print("Opcion no valida")


# Realice un programa que lea tres números, muestre cuál es el mayor y determine si es par o impar.

num1 = int(input("Ingrese un numero: "))
num2 = int(input("Ingrese otro numero: "))
num3 = int(input("Ingrese otro numero: "))

if num1 > num2 and num1 > num3:
    isEven = num1 % 2 == 0

    if isEven:
        print("El numero mayor es: ", num1, " y es par")
    else:
        print("El numero mayor es: ", num1, " y es impar")

elif num2 > num1 and num2 > num3:
    isEven = num2 % 2 == 0

    if isEven:
        print("El numero mayor es: ", num2, " y es par")
    else:
        print("El numero mayor es: ", num2, " y es impar")

elif num3 > num1 and num3 > num2:
    isEven = num3 % 2 == 0

    if isEven:
        print("El numero mayor es: ", num3, " y es par")
    else:
        print("El numero mayor es: ", num3, " y es impar")
else:
    print("Los numeros son iguales")


# Confeccione un programa que pida un número del 1 al 7 y diga el día de la semana correspondiente.

day = int(input("Ingrese un numero del 1 al 7: "))

if day == 1:
    print("El dia es Lunes")
elif day == 2:
    print("El dia es Martes")
elif day == 3:
    print("El dia es Miercoles")
elif day == 4:
    print("El dia es Jueves")
elif day == 5:
    print("El dia es Viernes")
elif day == 6:
    print("El dia es Sabado")
elif day == 7:
    print("El dia es Domingo")
else:
    print("Numero no valido")


# Realice un programa que pida un número del 1 al 12 y diga el nombre del mes correspondiente.

month = int(input("Ingrese un numero del 1 al 12: "))

if month == 1:
    print("El mes es Enero")
elif month == 2:
    print("El mes es Febrero")
elif month == 3:
    print("El mes es Marzo")
elif month == 4:
    print("El mes es Abril")
elif month == 5:
    print("El mes es Mayo")
elif month == 6:
    print("El mes es Junio")
elif month == 7:
    print("El mes es Julio")
elif month == 8:
    print("El mes es Agosto")
elif month == 9:
    print("El mes es Septiembre")
elif month == 10:
    print("El mes es Octubre")
elif month == 11:
    print("El mes es Noviembre")
elif month == 12:
    print("El mes es Diciembre")
else:
    print("Numero no valido")
