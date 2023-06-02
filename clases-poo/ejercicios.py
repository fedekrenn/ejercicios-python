# Clase Rectángulo: Crea una clase rectángulo que tenga atributos base y altura. Luego, define métodos para calcular el área y el perímetro del rectángulo

class Rectangulo:
    def __init__(self, base, altura):
        self.__base = base
        self.__altura = altura

    def area(self):
        return self.__base * self.__altura

    def perimetro(self):
        return (self.__base + self.__altura) * 2


mi_rectangulo = Rectangulo(5, 10)
print(mi_rectangulo.area())



# Clase Estudiante: Crea una clase Estudiante que tenga atributos nombre y edad. Luego, define un método para imprimir la información del estudiante. Realiza 3 instancias de la clase.

class Estudiante:
    def __init__(self, nombre, edad):
        self.__nombre = nombre
        self.__edad = edad

    def informar(self):
        print(f'El estudiante se llama {self.__nombre} y tiene {self.__edad}')


estudiante_luis = Estudiante('Luis', 25)
estudiante_juan = Estudiante('Juan', 30)
estudiante_maria = Estudiante('Maria', 20)

estudiante_luis.informar()
estudiante_juan.informar()
estudiante_maria.informar()



# Clase Libro: Crea una clase Libro quetenga atributos "título", "autor" y "anio" (año). Luego define un método para imprimir la información completa del libro.

class Libro:
    def __init__(self, titulo, autor, anio):
        self.__titulo = titulo
        self.__autor = autor
        self.__anio = anio

    def informacion(self):
        print(
            f'El libro {self.__titulo} fue escrito por {self.__autor} en {self.__anio}')


libro = Libro('El señor de los anillos', 'J.R.R. Tolkien', 1954)
libro.informacion()



# Clase Calculadora: Crea una clase Calculadora que tenga métodos para realizar operaciones matemáticas básicas como suma, resta, multiplicación y división.

class Calculadora:
    def __init__(self, num1, num2):
        self.__num1 = num1
        self.__num2 = num2

    def sumar(self):
        return self.__num1 + self.__num2

    def restar(self):
        return self.__num1 - self.__num2

    def multiplicar(self):
        return self.__num1 * self.__num2

    def dividir(self):
        return self.__num1 / self.__num2


calculadora = Calculadora(10, 5)

print(f'La suma es {calculadora.sumar()}')
print(f'La resta es {calculadora.restar()}')
print(f'La división es {calculadora.dividir()}')
print(f'La multiplicación es {calculadora.multiplicar()}')



# Clase círculo: Crea una clase Círculo que tenga un atributo radio. Luego, define métodos para calcular el área y la circunferencia del círculo

class Circulo:
    def __init__(self, radio):
        self.__radio = radio

    def calcular_area(self):
        return self.__radio ** 2 * 3.1416

    def calcular_circunferencia(self):
        return self.__radio * 3.1416 * 2


circulo = Circulo(40)
print(f'El área del círculo es {circulo.calcular_area()}')
print(f'La circunferencia del círculo es {circulo.calcular_circunferencia()}')
