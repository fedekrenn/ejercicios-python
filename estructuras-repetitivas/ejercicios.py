# Realice un programa que lea 4 números y diga cuántos son pares y cuantos impares y devuelva la sumatoria de los pares.

even_quantity = 0
odd_quantity = 0
even_sum = 0

for i in range(4):
    number = int(input("Ingrese un número: "))
    if number % 2 == 0:
        even_quantity += 1
        even_sum += number
    else:
        odd_quantity += 1

print("Cantidad de números pares:", even_quantity)
print("Cantidad de números impares:", odd_quantity)
print("Sumatoria de los números pares:", even_sum)


# Leer 10 números y obtener la cantidad de mayores y la cantidad de menores a 100, cuál es el número máximo y cuál es el número mínimo.

higger_100 = 0
lower_100 = 0
max_number = float('-inf')
min_number = float('inf')

for i in range(10):
    number = int(input("Ingrese un número: "))

    if number > 100:
        higger_100 += 1
    elif number < 100:
        lower_100 += 1
    if number > max_number:
        max_number = number
    if number < min_number:
        min_number = number

print("Cantidad de números mayores a 100:", higger_100)
print("Cantidad de números menores a 100:", lower_100)
print("Número máximo:", max_number)
print("Número mínimo:", min_number)


# Ingresar las edades y el sexo de 15 personas y determinar cuántas son mujeres, cuántos varones, cuántos mayores de edad y cuántos menores de edad.

male_quantity = 0
female_quantity = 0
adult_quantity = 0
minor_quantity = 0

for i in range(15):
    person_age = int(input(f'Ingrese la edad de la persona {(i + 1)}:\n'))

    while True:
        person_genre = int(
            input(f'Ingrese sexo de la persona {(i + 1)}: 1 para varón, 2 para mujer:\n'))
        if person_genre == 1:
            male_quantity += 1
            break
        elif person_genre == 2:
            female_quantity += 1
            break
        else:
            print(
                "Opción de género no válida. Por favor, ingrese 1 para varón o 2 para mujer.")
            
    if person_age >= 18:
        adult_quantity += 1
    else:
        minor_quantity += 1

print("Cantidad de mujeres:", female_quantity)
print("Cantidad de varones:", male_quantity)
print("Cantidad de personas mayores de edad:", adult_quantity)
print("Cantidad de personas menores de edad:", minor_quantity)


# Leer 10 números y mostrar solamente los números positivos, y su sumatoria.

total_sum = 0
positive_list = []

for i in range(10):
    num = int(input(f'Dime el {(i + 1)}° número:\n'))
    if num >= 0:
        positive_list.append(num)
        total_sum += num

print('Números positivos:')

for num in positive_list:
    print(num)
print(f'Sumatoria: {total_sum}')


# Leer 15 números negativos y convertirlos a positivos e imprimir dichos números.

number_list = []

for i in range(15):
    while True:
        num = int(input(f'Ingresa el {(i + 1)}° número NEGATIVO:\n'))

        if num < 0:
            number_list.append(-num)
            break
        else:
            print('No es un número negativo')

print('Los números convertidos a positivo son:')
for num in number_list:
    print(num)
