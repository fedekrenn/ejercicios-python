# Diseña un algoritmo que introduzca por teclado el nombre de 3 países, se almacenen en una lista y los muestre por pantalla.

first_country = input("Introduce el nombre de un país: ")
second_country = input("Introduce el nombre de otro país: ")
third_country = input("Introduce el nombre de otro país: ")

countries = [first_country, second_country, third_country]
print(countries)


# Diseña un algoritmo que almacene los precios de 4 productos que compré en una lista y luego me muestre el total en pantalla.

productsPrices = [200, 150, 300, 100]

total = productsPrices[0] + productsPrices[1] + \
    productsPrices[2] + productsPrices[3]
print("El total de la compra es de", total, "$")


# Diseña un algoritmo que almacene las letra de tu nombre en una lista y luego muestre el nombre.

name = ["F", "e", "d", "e", "r", "i", "c", "o"]

print(name[0] + name[1] + name[2] + name[3] +
      name[4] + name[5] + name[6] + name[7])


# Diseña un algoritmo que introduzca por teclado el nombre, materia, profesor y nota. Se almacene en una tupla y luego muestre los datos en pantalla.

name = input("Introduce tu nombre: ")
subject = input("Introduce la materia: ")
teacher = input("Introduce el profesor: ")
grade = int(input("Introduce la nota: "))

data = (name, subject, teacher, grade)

print(data)


# Diseña un algoritmo que introduzca por teclado el nombre de 3 materias y sus notas correspondientes. Deben almacenarse las materias en una tupla y las notas en otra. Luego muestre en pantalla la materia con su nota correspondiente.

subject_one = input('Ingrese el nombre de la primer materia: ')
grade_one = int(input('Ingrese la nota recibida: '))

subject_two = input('Ingrese el nombre de la segunda materia: ')
grade_two = int(input('Ingrese la nota recibida: '))

subject_three = input('Ingrese el nombre de la tercer materia: ')
grade_three = int(input('Ingrese la nota recibida: '))

subjects = (subject_one, subject_two, subject_three)
grades = (grade_one, grade_two, grade_three)

print(subjects[0], ':', grades[0])
print(subjects[1], ':', grades[1])
print(subjects[2], ':', grades[2])


# Diseña un algoritmo con un diccionario que contenga como clave 3 materias que estás cursando y como valores uses tuplas para almacenar 2 notas por materia. Luego por pantalla muestres las notas de cada materia.

subjects = {
    'Matemáticas': (10, 9),
    'Física': (8, 7),
    'Química': (10, 10)
}

print('Matemáticas :', subjects['Matemáticas'])
print('Física :', subjects['Física'])
print('Química :', subjects['Química'])


# Diseña un algoritmo creando una tupla que almacene 3 categorías de música y luego crea un diccionario donde utilices como clave la tupla y almacenes 2 músicos por categoría de música. Luego mostrar en pantalla los artistas.

categoria_musica = ('Rock', 'Pop', 'Cuarteto')

diccionario = {
    categoria_musica[0]: ['Freddie Mercury', 'John Lennon'],
    categoria_musica[1]: ['Maddona', 'Britney Spears'],
    categoria_musica[2]: ['La Mona Jimenez', 'Rodrigo']
}

print(diccionario['Rock'])
print(diccionario['Pop'])
print(diccionario['Cuarteto'])
