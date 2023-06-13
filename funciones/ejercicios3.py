# Realiza una función separar() que tome una lista de números enteros y devuelva dos listas ordenadas. La primera con los números pares, y la segunda con los números impares:

def separate(list):

    list.sort()

    odd = []
    even = []

    for i in list:
        if i % 2 == 0:
            odd.append(i)
        else:
            even.append(i)

    return { 'Pares': odd, 'Impares': even }


print(separate([100, -34, 3, 56, 88, -55, 99, 45, 4]))



# Realiza una función aplicando argumentos indeterminados que, dependiendo de los parámetros que reciba, convierta a milímetros o a metros.

# - Si recibe un argumento, supone que son milímetros y convierte a metros, centímetros y milímetros.
# - Si recibe 3 argumentos, supone que son metros, centímetros y milímetros y los convierte a milímetros.

def convert_units(*args):
    if len(args) == 1:
        print(f'Ingresaste {args[0]} milímetros, lo cual son {args[0] / 10} centrímetros y {args[0] / 1000} metros')
  elif len(args) == 3:
        print(f'Pasando esos valores tenemos {args[0] * 1000}, {args[1] * 10} y {args[2]} milímetros')
  else:
        print('Cantidad incorrecta de parámetros')

convert_units(234234, 32, 55)



# Función de factorial con recursividad

def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)

print(factorial(5))