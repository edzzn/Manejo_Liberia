import pickle

class Estudiante():

    def __init__(self, cedula, name, lastname):
        self.id = cedula
        self.name = name
        self.lastname = lastname


class Libro():
    def __init__(self, ident, name, author, cat, year):
        self.id = ident
        self.name = name
        self.author = author
        self.category = cat
        self.year = year

    def edit(self, name, author, cat, year):
        self.name = name
        self.author = author
        self.category = cat
        self.year = year


class RegistroReserva():

    def __init__(self):
        # Registro de reserva: Dicitonary {Estudiante, [(Libro, fecha_o, fecha_final),],}
        self.reg_reservas = {}
        self.num_reservaciones = 0

    def add(self, estudiante, libro, fecha_prestamo, fecha_devolucion):
        nuevo_registro = (libro, fecha_prestamo, fecha_devolucion)
        self.num_reservaciones += 1
        if estudiante in self.reg_reservas:
            self.reg_reservas[estudiante].append(nuevo_registro)
        else:
            self.reg_reservas[estudiante] = [nuevo_registro]

class RegistroPrestamos():

    def __init__(self):
        # Registro de prestamo: Dicitonary {Estudiante, [(Libro, fecha_o, fecha_final),],}
        self.reg_prestamos = {}
        self.num_prestamo = 0

    def show_persona(self):
        return self.reg_prestamos

    def add(self, estudiante, libro, fecha_prestamo, fecha_devolucion=""):
        nuevo_registro = (libro, fecha_prestamo, fecha_devolucion)

        self.num_prestamo =+ 1
        if estudiante in self.reg_prestamos:
            self.reg_prestamos[estudiante].append(nuevo_registro)
        else:
            self.reg_prestamos[estudiante] = nuevo_registro


def saveD(tipo, objeto):

    file_name = get_file_name(tipo)
    pickle.dump(objeto, open(file_name, "wb"))


def loadD(tipo):
    file_name = get_file_name(tipo)
    # Objetiene la información serializada
    data = pickle.load(open(file_name, "rb"))
    return data


def get_file_name(tipo):
    # l -> libros
    # p -> prestamos
    # r -> reservas
    # e -> estudiantes
    # c -> categoria

    if tipo == 'l':
        return 'data_libros.dat'
    elif tipo == 'p':
        return 'data_prestamos.dat'
    elif tipo == 'r':
        return 'data_reservas.dat'
    elif tipo == 'e':
        return 'data_estudiantes.dat'
    elif tipo == 'c':
        return 'data_categorias.dat'
    else:
        print('No se puede guardar el archivo')
