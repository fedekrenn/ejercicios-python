from client_package.client import Client

client_one = Client('Juan', 'juan@gmail.com', 'miclave123', 3512506788, 'Calle falsa 123')

print(client_one)    # Datos que vienen del método __str__
print(client_one.get_data())    # Información del cliente instanciado
print(client_one.login('miclave123'))   # Prueba de login con datos correctos
print(client_one.login('1234567'))  # Prueba de login con datos incorrectos
print(client_one.add_to_order('iPhone 14'))     # Agregar una orden
print(client_one.get_order())   # Obtener las órdenes del cliente