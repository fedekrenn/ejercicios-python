# Mostrar la lista de países de América del Sur y su población en millones de habitantes usando un bucle y el siguiente diccionario:

population = {
    "Argentina": 45,
    "Bolivia": 11,
    "Brasil": 211,
    "Chile": 19,
    "Colombia": 50,
    "Ecuador": 17,
    "Guyana": 0.8,
    "Paraguay": 7,
    "Perú": 32,
    "Suriname": 0.6,
    "Uruguay": 3.5,
    "Venezuela": 28
}

for country in population:
    print(f'{country} tiene {population[country]} millones de habitantes')


# Mostrar los nombres de los países que tienen una superficie mayor a 2 millones de km², usando una lista de tuplas y un bucle while:

countries = [
    ("Rusia", 17.1),
    ("Canadá", 9.9),
    ("Paraguay", 1.6),
    ("EE.UU.", 9.5),
    ("Brasil", 8.5),
    ("Australia", 7.7),
    ("India", 3.3),
    ("Argentina", 2.8),
    ("Kazajistán", 2.7),
    ("Argelia", 2.4)
]

counter = 0

while counter < len(countries):
    if countries[counter][1] > 2:
        print(countries[counter])
    counter += 1


# Mostrar los nombres de los países que empiezan con "M" o "N"

countries = ["Sudáfrica", "Malawi", "Malí", "Costa de Marfil", "Mauricio", "Argelia",
             "Mozambique", "Namibia", "Níger", "Nigeria"]

buffer = []

for country in countries:
    if country[0] == 'M' or country[0] == 'N':
        buffer.append(country)

print(f'Los países que comienzan con letra M o N son {buffer}')


# Mostrar los nombres de los animales en una lista, pero omitiendo los animales que tienen más de 7 letras, utilizando un bucle while:

animals = ["tigre", "oso", "cocodrilo", "mono", "jirafa", "puma", "pingüino", "elefante",
           "cebra", "ornitorrinco"]

buffer = []
counter = 0

while counter < len(animals):
    if len(animals[counter]) <= 7:
        buffer.append(animals[counter])
    counter += 1

print(f'Los animales con 7 o menos letras son {buffer}')


# Mostrar los nombres de los animales y su cantidad en una lista, utilizando un diccionario y un bucle for:

animals = ["león", "jirafa", "elefante", "cebra", "hipopótamo", "rinoceronte"]

quantities = {
    "león": 3,
    "jirafa": 5,
    "elefante": 2,
    "cebra": 7,
    "hipopótamo": 1,
    "rinoceronte": 4
}

for animal in animals:
    print(f'{animal} tiene {quantities[animal]} unidades')
