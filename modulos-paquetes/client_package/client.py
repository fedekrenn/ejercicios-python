class Client:
    def __init__(self, name, email, password, phone, address):
        self.__name = name
        self.__email = email
        self.__password = password
        self.__phone = phone
        self.__address = address
        self.__order = []

    def __str__(self):
        return f'Cliente {self.__name} creado con éxito bajo su correo {self.__email}'

    def get_data(self):
        return {
            'name': self.__name,
            'email': self.__email,
            'phone': self.__phone,
            'address': self.__address
        }
    
    def login(self, password):
        if self.__password == password:
            return 'Login exitoso!'
        return 'Email o contraseña incorrectos'
    
    def add_to_order(self, product):
        self.__order.append(product)
        return 'Producto agregado con éxito a la orden!'

    def get_order(self):
        return self.__order
