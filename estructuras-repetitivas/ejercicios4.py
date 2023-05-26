# Escribir un programa que pida al usuario una palabra y luego muestre por pantalla una a una las letras de la palabra introducida empezando por la última.

import random
word = input('Ingrese una palabra:\n')

for i in range(len(word)-1, -1, -1):
    print(word[i])



# Pide al usuario una cadena de texto e indica si es un palíndromo o no. Palíndromo es una palabra o frase que se lee igual en un sentido que en otro. Por ejemplo: oso, ala, radar, etc. NO es necesario usar bucles.

paragraph = input('Ingrese una cadena de texto:\n')
turned = paragraph[::-1]

isPalindrome = paragraph == turned

print('Sí, es palíndromo!' if isPalindrome else 'No, no es palíndromo')



# Generaremos un número entre 1 y 10. Nuestro objetivo es adivinar el número. Si fallamos nos dirán si es mayor o menor que el número buscado. También poner el número de intentos requeridos.

number = random.randint(1, 10)
attemps = 1

while True:
    user_num = int(input('Ingresa un número:\n'))

    if number == user_num:
        print('Ganaste!!')
        break
    else:
        print('Mmm... no, el número es más alto' if number >
              user_num else 'Mmm... no, el número es más bajo')
        attemps += 1

print(f'Ganaste en {attemps} intentos')



# Supongamos que estamos creando una pagina web para un cliente. Es un cliente que vende cursos de programacion online. Los cursos que tiene a la venta son los que ven a continuacion en la lista (esta lista seria la base de datos)

# La terminal o consola sera nuestra pagina web. Tenemos que "mostrar" en nuestra pagina web (terminal o consola) todos los cursos, pero hay que mostrarlos desde el mas nuevo (ultimo de la lista) al mas viejo (primero de la lista)

# Una vez terminado el pedido anterior, ahora el cliente nos solicita que el usuario pueda realizar una busqueda de los cursos. Permitir al usuario ingresar el nombre de un curso y luego mostrar un mensaje si ese curso esta en venta, sino mostrar otro mensaje que diga que ese curso NO esta en venta.

# EXTRA: Aquellos que quieran pueden realizar un "menu" que pregunte al usuario si quiere buscar otro curso o si quiere abandonar la pagina.

courses_for_sale = ["JavaScript", "c++", "Python", "Java", "php", "Go", "Rust", "Dart"]

for index in range(len(courses_for_sale) - 1, -1, -1):
    print(courses_for_sale[index])

while True:
    user_course = input(
        '-------\nIntroduce el curso que te gustaría tomar, escribe "exit" para salir:\n')

    if user_course == 'exit':
        print('Gracias por su visita! Programa finalizado')
        break
    elif user_course in courses_for_sale:
        print('\t ✅ Sí, ese curso está en nuestra plataforma')
    else:
        print('\t ❌ Por el momento no tenemos esa propuesta')
