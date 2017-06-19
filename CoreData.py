import pickle

class Estudiante():

    def __init__(self, cedula, name, lastname):
        self.id = cedula
        self.name = name
        self.lastname = lastname

    def __str__(self):
        return (self.id + " " + self.name + " " + self.lastname)

    def print_estudiante(self):
        return (self.id + " " + self.name + " " + self.lastname)

    def edit(self, name, lastname):
        self.name = name
        self.lastname = lastname

class RegistroEstudiante():
    def __init__(self):
        self.reg_estudiante = []

    def add(self, Estudiante):
        self.reg_estudiante.append(Estudiante)

    def mostrar(self):
        for estudiante in self.reg_estudiante:
            print(estudiante)

    def edit_estudiante(self, estudiante_id, estudiante):
        position_list = self.get_estudiante_loc(estudiante_id)
        self.registro_estudiante[position_list] = estudiante

    def delete_estudiante(self, estudiante_id):
        position_list = self.get_estudiante_loc(estudiante_id)
        del self.registro_estudiante[position_list]

    def encontrar_estudiante(self, estudiante_id):
        for estudiante in self.reg_estudiante:
            if estudiante.id == estudiante_id:
                # print(True)
                return estudiante
        else:
            return None

    def valida_estudiante(self, cedula):
        for estudiante in self.reg_estudiante:
            if estudiante.id == cedula:
                return True
        else:
            return False

class Libro():
    def __init__(self, isbn, numPag, idioma, autor, editorial, categoria):
        self.isbn = isbn
        self.numPag = numPag
        self.idioma = idioma
        self.autor=autor
        self.editorial=editorial
        self.categoria=categoria

    def __str__(self):
        return (self.isbn + " " + self.numPag + " " + self.idioma + " " + self.autor + " " + self.editorial + " " + self.categoria)

    def print_libro(self):
        return (self.isbn + " " + self.numPag + " " + self.idioma + " " + self.autor + " " + self.editorial + " " + self.get_categoria())

    def edit(self, numPag, idioma, autor, editorial, categoria):
        self.numPag = numPag
        self.idioma = idioma
        self.autor = autor
        self.editorial = editorial
        self.categoria = categoria


class RegistroLibro():
    def __init__(self):
        self.reg_libro = []

    def add(self, Libro):
        self.reg_libro.append(Libro)

    def mostrar(self):
        for libro in self.reg_libro:
            print(libro)

    def get_registro(self):
        return self.reg_libro

    def edit_libro(self, libro_isbn, libro):
        position_list = self.get_libro_loc(libro_isbn)
        self.__registro_libro[position_list] = libro

    def delete_libro(self, libro_isbn):
        position_list = self.get_libro_loc(libro_isbn)
        del self.reg_libro[position_list]

    def encontrar_libro(self, libro_isbn):
        for libro in self.reg_libro:
            if libro.isbn == libro_isbn:
                return libro
        else:
            return None


class Categoria():
    def __init__(self, codigo, descripcion):
        self.codigo=codigo
        self.descripcion=descripcion

    def __str__(self):
        return (self.get_codigo() + " " + self.get_descripcion())

    def print_categoria(self):
        return (self.get_codigo() + " " + self.get_descripcion())

    def edit(self, descripcion):
        self.descripcion = descripcion


class RegistroCategoria():
    def __init__(self):
        self.registro_categoria = []

    def add(self, Categoria):
        self.registro_categoria.append(Categoria)

    def mostrar(self):
        for categoria in self.registro_categoria:
            print(categoria)

    def edit_categoria(self, categoria_codigo, categoria):
        position_list = self.get_categoria_loc(categoria_codigo)
        self.__registro_categoria[position_list] = categoria

    def delete_categoria(self, categoria_codigo):
        position_list = self.get_categoria_loc(categoria_codigo)
        del self.__registro_categoria[position_list]

    def encontrar_categoria(self, categoria_codigo):
        for categoria in self.__registro_categoria:
            if categoria.get_codigo() == categoria_codigo:
                return categoria
        else:
            return None


class RegistroReserva():

    def __init__(self):
        # Registro de reserva: Dicitonary {Estudiante, [(Libro, fecha_o, fecha_final),],}
        self.reg_reservas = {}
        self.num_reservaciones = 0

    def add(self, estudiante, libro, fechaAReservar, fechaReserva, HoraReserva):
        nuevo_registro = (libro, fechaAReservar, fechaReserva, HoraReserva)
        self.num_reservaciones += 1

        if estudiante in self.reg_reservas:
            self.reg_reservas[estudiante].append(nuevo_registro)

        else:
            self.reg_reservas[estudiante] = [nuevo_registro]

    def editar(self, estudiante, libro, fechaAReservar, fechaReserva, HoraReserva):
        if estudiante in self.reg_reservas:
            self.reg_reservas[estudiante]=(libro, fechaAReservar, fechaReserva, HoraReserva)

    def listar(self):
        for key in self.reg_reservas:
            print(key + ": " +str(self.reg_reservas[key]))

    def eliminar(self, estudiante, isbn):
        """
        Elimina un registro, dado un objeto estudiante y un isbn
        Este metodo no valida.
        :param estudiante_id: 
        :return: 
        """
        registro = self.reg_reservas[estudiante]
        for reserva in registro:
            print(reserva)
            if reserva[0].isbn == isbn:
                print(isbn)
                self.reg_reservas[estudiante].remove(reserva)


    def encontrar_registro(self, estudiante):
        if estudiante in self.reg_reservas:
            return self.reg_reservas[estudiante]
        else:
            return None

    def registro_id_isbn(self, id_estudiante, isbn):
        reg_estudiantes = loadD("e")
        reg_reservas = loadD("r")

        for estudiante in reg_estudiantes.reg_estudiante:
            if estudiante.id == id_estudiante:
                for estudiante in reg_reservas.reg_reservas:
                    # print(reg_reservas.reg_reservas[estudiante])

                    # vemos cada reserva de cada usuario
                    for reserva in reg_reservas.reg_reservas[estudiante]:
                        # print(reserva)
                        # print(reserva[0].isbn)
                        if reserva[0].isbn == isbn:
                            return estudiante, reserva
        else:
            return None

class RegistroPrestamos():

    def __init__(self):
        # Registro de prestamo: Dicitonary {Estudiante, [(Libro, fecha_o, fecha_final),],}
        self.reg_prestamos = {}
        self.num_prestamo = 0

    def add(self, estudiante, libro,fecha_a_reservar, fecha_reserva, hora_reserva):
        nuevo_registro = (libro, fecha_a_reservar, fecha_reserva, hora_reserva)


        self.num_prestamo =+ 1
        if estudiante in self.reg_prestamos:
            self.reg_prestamos[estudiante].append(nuevo_registro)
        else:
            self.reg_prestamos[estudiante] = nuevo_registro

    def editar(self, estudiante, libro, fecha_a_reservar, fecha_reserva, hora_reserva):
        if estudiante in self.reg_reservas:
            self.reg_reservas[estudiante] = (libro, fecha_a_reservar,fecha_reserva, hora_reserva )

    def listar(self):
        for key in self.reg_reservas:
            print(key + ": " + str(self.reg_reservas[key]))

    def eliminar(self, estudiante ):
        del self.reg_reservas[estudiante]


# General Funciones

# Serialización de archivos

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

def validateLibro(isbn):
    """
    Valida que un libro exista en el registro de libros
    :param isbn:
    :return: Boolean
    """
    reg_libros = loadD('l')

    for libro in reg_libros.reg_libro:

        if libro.isbn == isbn:
            return True
    else:
        return False

def validateEstudiante(cedula):
    """
    Valida que un usuario se encuentre en el registro de usuarios
    :param cedula:
    :return: Boolean
    """
    reg_estudiantes = loadD('e')
    for estudiante in reg_estudiantes.reg_estudiante:
        if estudiante.id == cedula:
            return True
    else:
        return False
