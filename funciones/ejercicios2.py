# 1. Realice una función para calcular el costo total recaudado en entradas de un recital.

def calculate_total(tickets_q):
    ticket_price = 500
    return ticket_price * tickets_q

print(f'El total recaudado es: {calculate_total(10)}')


# 2. Función para comprobar si una canción está en la lista de reproducción de un recital.

playlist = [
    'Hotel California',
    'Bohemian Rhapsody',
    'Stairway to Heaven',
    'Sweet Child O Mine',
    'Imagine',
    'Smells Like Teen Spirit',
    'One',
    'Billie Jean',
    'Bohemian Rhapsody',
    'Hey Jude',
    'Like A Rolling Stone',
    'Another Brick In The Wall',
    'Yesterday'
]

def is_in_playlist(song):
    return song in playlist

print(
    f'La canción está en la lista de reproducción: {is_in_playlist("Yesterday")}')


# 3. Función para calcular el tiempo total de duración de un recital, considerando la duración de x cantidad de canciones.

def calculate_total_time(songs):
    song_avg_time = 3
    return song_avg_time * songs

print(f'El tiempo total de duración es de {calculate_total_time(10)} minutos')

# 4. Crear una función que calcule la velocidad promedio de un auto, dada la distancia recorrida y el tiempo empleado (en minutos).

def calculate_avg_speed(distance, time):
    return f'El auto va a {distance / (time / 60)} km/h'

print(calculate_avg_speed(100, 30))


# 5. Crear una función que determine si un auto está en marcha o detenido, dada su velocidad.

def is_moving(speed):
    return speed > 0

print(f'El auto está en movimiento: {is_moving(0)}')


# 6. Crear una función que convierta kilómetros por hora a millas por hora.

def convert_kmh_to_mph(kmh):
    return f'{kmh} km/h son {kmh * 0.621371} mph'

print(convert_kmh_to_mph(100))


# 7. Crear una función que calcule el consumo de combustible de un auto por kilómetro, dada la distancia recorrida y la cantidad de combustible utilizada.

def calculate_fuel_consumption(distance, fuel):
    return f'El consumo de combustible es de {distance / fuel} km por litro'

print(calculate_fuel_consumption(1200, 57))


# 8. Crear una función que determine el costo de un viaje en auto, dada la distancia recorrida, el consumo de combustible (kilómetros por litro) y el precio del combustible.

def calculate_trip_cost(distance, fuel_consumption, fuel_price):
    return f'El costo del viaje es de ${distance / fuel_consumption * fuel_price}'

print(calculate_trip_cost(4000, 15, 215))
