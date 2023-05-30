# Crear un conjunto en Python que posea los siguientes elementos: "Rojo", "Blanco", "Azul". Posteriormente, agrega nuestro set de colores los valores de "Violeta" y "Dorado". Elimina a los colores: "Celeste", "Blanco" y "Dorado". Pregunta: ¿Qué pasa si queremos eliminar el color Celeste utilizando el método discard?

colors = {"Rojo", "Blanco", "Azul"}

colors.update(["Violeta", "Dorado"])

print(colors)

colors.discard("Celeste")
colors.discard("Blanco")
colors.discard("Dorado")

print(colors)



# Crear un conjunto en Python que posea los siguientes elementos: "Inglaterra", "USA", "México".  Posteriormente agrega nuestro set de países los elementos de: "Islandia", "Italia", "Argentina", "Portugal" y "USA". Elimina a los países: "Chile" e "Italia". Pregunta: ¿Qué pasa si queremos eliminar al país Chile utilizando el método remove ?, ¿Qué pasó con el element de USA?

countries = { 'Inglaterra', 'USA', 'México' }

countries.update([ 'Islandia', 'Italia', 'Argentina', 'Portugal', 'USA'])
print(countries)

countries.discard('Chile')
countries.discard('Italia')
print(countries)



# Escribir un programa que le solicite al usuario su nombre, edad, dirección y que, posteriormente, lo muestre por pantalla. Ejemplo del output solicitado: "Juan tiene 25 años, y vive en Carrera 7 Bogotá"

user = {
    'name': input('Dime tu nombre:\n'),
    'age': int(input('Cuál es tu edad?:\n')),
    'addres': input('Dime tu dirección donde vives:\n')
}

print(user)
print(f"{user['name']} tiene {user['age']} años y vive en {user['addres']}")