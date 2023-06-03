# Transforma el texto dado en este otro:

# Gordon lanzó su curva...
# Strawberry ha fallado por un pie! -gritó Joe Castiglione.
# Dos pies le corrigió Troop.
# Strawberry menea la cabeza como disgustado… -agrega el comentarista.

text = 'gordon lanzó su curva&strawberry ha fallado por un pie! -gritó Joe Castiglione&dos pies -le corrigió Troop&strawberry menea la cabeza como disgustado… -agrega el comentarista'

text = text.capitalize().replace('curva', 'curva..').replace('-le', 'le').replace('strawberry', '- Strawberry').replace('dos', '- Dos').replace('joe castiglione', 'Joe Castiglione').replace('troop', 'Troop')
list1 = text.split('&')

for p in list1:
  print(p + '.')



# Escribir un programa que guarde en una variable en un diccionario {'Dolar':'$','Euro':'€', 'Libra':'£'}. Luego se le deberá solicitar al usuario que ingrese la divisa que desea visualizar. En el caso de ingresar una divisa no existente en nuestro diccionario, deberemos indicarle con un mensaje de notificación que la divisa no se encuentra disponible.

currencies = { 'dolar':'$', 'euro':'€', 'libra':'£' }

user_choice = input('Elige la divisa que quieres visualizar:\n')

if user_choice.lower() in currencies:
  print(f'La divisa {user_choice} tiene como signo {currencies[user_choice.lower()]}')
else:
  print('Esa moneda no se encuentra disponible')



# A partir de una lista realizar las siguientes tareas sin modificar la lista original:

# - Borrar los elementos duplicados
# - Ordenar la lista de mayor a menor
# - Eliminar todos los números impares ( for if (%2==1) pop, remove )
# - Realizar una suma de todos los números que quedan (sum(lista))
# - Añadir como primer elemento de la lista la suma realizada insert(0, suma)
# - Devolver la lista modificada
# - Finalmente, después de ejecutar la función, comprueba que la suma de todos los números a partir del segundo, concuerda con el primer número de la lista

my_list = [29, 5, 12, 17, 5, 24, 5, 12, 23, 16, 12, 5, 12, 17]

list_1 = set(my_list)
list_2 = list(list_1)
list_2.sort(reverse=True)

for num in list_2[:]: # Creo una copia de la lista para poder eliminar elementos, ya que si lo hago sobre la lista original, se desordena y trae inconsistencias
  if num % 2 != 0:
    list_2.remove(num)

my_suma = sum(list_2)
list_2.insert(0, my_suma)

print(list_2)
print('Ok, concuerda' if sum(list_2[1:]) == list_2[0] else 'No, algo salió mal')