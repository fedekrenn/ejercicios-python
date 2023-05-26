# Calcular la suma de una cantidad de números enteros ingresados por el usuario directamente utilizando la función input. Para finalizar la ejecución del programa, el usuario debe escribir la palabra exit() El programa debe validar dicha acción. Finalmente, el algoritmo debe mostrar la suma parcial y total obtenida

total = 0

while True:
  user_input = input('Ingresa un número, pasa salir escribe "exit":\n')
  if user_input == 'exit':
    break
  else:
    total += int(user_input)

print(f'El total es {total}')



# Escribir la letra de la canción Me gusta de Manu Chao, utilizando la sentencia de iteración for https://www.letras.com/manu-chao/7352

paragraph = ['los aviones', 'viajar', 'la mañana', 'el viento', 'soñar', 'la mar', 'la moto', 'correr', 'la lluvia', 'volver', 'marihuana', 'colombiana', 'montaña', 'la noche']

for word in paragraph:
  print(f'Me gusta {word}, me gustas tú')



#Escribe un programa que lea dos números por teclado y permita elegir entre 4 opciones en un menú:

#- Mostrar una suma de los dos números
#- Mostrar una resta de los dos números (el primero menos el segundo)
#- Mostrar una multiplicación de los dos números
#- Si elige esta opción se interrumpirá la impresión del menú y el programa finalizará
#- En caso de no introducir una opción válida, el programa informará de que no es correcta.

num1 = int(input('Introduce el primer número:\n'))
num2 = int(input('Introduce el segundo número:\n'))
print('----------')

while True:
  print(' 1) Mostrar una suma de los dos números.\n 2) Mostrar una resta de los dos números (el primero menos el segundo) \n 3) Mostrar una multiplicación de los dos números \n 4) Finalizar programa')
  option = input('-------\nElije una opción:\n')

  if option == '1':
    print(f'{num1} + {num2} es igual a {num1 + num2}')
  elif option == '2':
    print(f'{num1} - {num2} es igual a {num1 - num2}')
  elif option == '3':
    print(f'{num1} x {num2} es igual a {num1 * num2}')
  elif option == '4':
    print('Programa finalizado')
    break
  else:
    print('Opción no válida')



# Escribe un programa que lea un número impar por teclado. Si el usuario no introduce un número impar, debe repetirse el proceso hasta que lo introduzca correctamente.

while True:
  number = int(input('Ingresa un número impar:\n'))
  if number % 2 != 0:
    print(f'Gracias! ingresaste el: {number}')
    break
  else:
    print('Debes ingresar un número impar:\n')



# Escribe un programa que sume todos los números enteros impares desde el 0 hasta el 100.

sum = 0

for i in range(1, 101, 2):
  sum += i

print(sum)



# Escribe un programa que pida al usuario cuantos números quiere introducir. Luego lee todos los números y realiza una media aritmética.

quantity = int(input('Cuántos números quieres introducir?\n'))
counter = 1
acc = 0

while counter <= quantity:
  number = int(input(f'Introduce el {counter}° número:\n'))
  acc += number
  counter += 1

print(f'El promedio es {acc / quantity}')



#Escribe un programa que pida al usuario un número entero del 0 al 9, y que mientras el número no sea correcto se repita el proceso. Luego debe comprobar si el número se encuentra en la lista de números y notificarlo.

list_of_numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

while True:
  number = int(input('Ingresa un número entero del 0 al 9:\n'))
  if number in list_of_numbers:
    print(f'Gracias! elegiste el {number}')
    break
  else:
    print('El número es inválido')



# Utilizando la función range() y la conversión a listas, genera las siguientes listas dinámicamente:

# - Todos los números del 0 al 10 [0, 1, 2, ..., 10]
# - Todos los números del -10 al 0 [-10, -9, -8, ..., 0]
# - Todos los números pares del 0 al 20 [0, 2, 4, ..., 20]
# - Todos los números impares entre -20 y 0 [-19, -17, -15, ..., -1]
# - Todos los números múltiples de 5 del 0 al 50 [0, 5, 10, ..., 50]

first_list = list(range(0, 101))
second_list = list(range(-10, 1))
third_list = list(range(0, 21, 2))
fourth_list = list(range(-19, 0, 2))
fifth_list = list(range(0, 51, 5))

print(first_list)
print(second_list)
print(third_list)
print(fourth_list)
print(fifth_list)