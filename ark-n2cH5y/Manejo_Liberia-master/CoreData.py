class Estudiante():

    def __init__(self, cedula, name, lastname):
        self.id = cedula
        self.name = name
        self.lastname = lastname

    def __str__(self):
        return (self.get_id() + " " + self.get_name() + " " + self.get_lastname())

    def print_estudiante(self):
        return (self.get_id() + " " + self.get_name() + " " + self.get_lastname())

    def edit(self, name, lastname):
        self.name = name
        self.lastname = lastname

    def get_id(self):
        return self.id

    def get_name(self):
        return self.name

    def get_lastname(self):
        return self.lastname

class RegistroEstudiante():
    def __init__(self):
        self.registro_estudiante = []

    def add(self, Estudiante):
        self.registro_estudiante.append(Estudiante)

    def mostrar(self):
        for estudiante in self.registro_estudiante:
            print(estudiante)

    def get_registro(self):
        return self.registro_estudiante

    def edit_estudiante(self, estudiante_id, estudiante):
        position_list = self.get_estudiante_loc(estudiante_id)
        self.__registro_estudiante[position_list] = estudiante

    def delete_estudiante(self, estudiante_id):
        position_list = self.get_estudiante_loc(estudiante_id)
        del self.__registro_estudiante[position_list]

    def get_estudiante_loc(self, id):
        for i, estudiante in enumerate(self.__registro_estudiante):
            if estudiante.get_id() == id:
                return i
        else:
            return None

    def encontrar_estudiante(self, estudiante_id):
        for estudiante in self.__registro_personas:
            if estudiante.get_id() == estudiante_id:
                return estudiante
        else:
            return None

class Libro():
    def __init__(self, isbn, numPag, idioma, autor, editorial, categoria):
        self.isbn = isbn
        self.numPag = numPag
        self.idioma = idioma
        self.autor=autor
        self.editorial=editorial
        self.categoria=categoria

    def __str__(self):
        return (self.get_isbn() + " " + self.get_numPag() + " " + self.get_idioma() + " " + self.get_autor() + " " + self.get_editorial() + " " + self.get_categoria())

    def print_libro(self):
        return (self.get_isbn() + " " + self.get_numPag() + " " + self.get_idioma() + " " + self.get_autor() + " " + self.get_editorial() + " " + self.get_categoria())

    def edit(self, numPag, idioma, autor, editorial, categoria):
        self.numPag = numPag
        self.idioma = idioma
        self.autor = autor
        self.editorial = editorial
        self.categoria = categoria

    def get_isbn(self):
        return self.isbn

    def get_numPag(self):
        return self.numPag

    def get_idioma(self):
        return self.idioma

    def get_autor(self):
        return self.autor

    def get_editorial(self):
        return self.editorial

    def get_categoria(self):
        return self.categoria

class RegistroLibro():
    def __init__(self):
        self.registro_libro = []

    def add(self, Libro):
        self.registro_libro.append(Libro)

    def mostrar(self):
        for libro in self.registro_libro:
            print(libro)

    def get_registro(self):
        return self.registro_libro

    def edit_libro(self, libro_isbn, libro):
        position_list = self.get_libro_loc(libro_isbn)
        self.__registro_libro[position_list] = libro

    def delete_libro(self, libro_isbn):
        position_list = self.get_libro_loc(libro_isbn)
        del self.registro_libro[position_list]

    def get_libro_loc(self, isbn):
        for i, libro in enumerate(self.registro_libro):
            if libro.get_isbn() == isbn:
                return i
        else:
            return None

    def encontrar_libro(self, libro_isbn):
        for libro in self.registro_libro:
            if libro.get_isbn() == libro_isbn:
                return libro
        else:
            return None


class categoria():
    def __init__(self, codigo, descripcion):
        self.codigo=codigo
        self.descripcion=descripcion

    def __str__(self):
        return (self.get_codigo() + " " + self.get_descripcion())

    def print_categoria(self):
        return (self.get_codigo() + " " + self.get_descripcion())

    def edit(self, descripcion):
        self.descripcion = descripcion

    def get_codigo(self):
        return self.codigo

    def get_descripcion(self):
        return self.descripcion

class RegistroCategoria():
    def __init__(self):
        self.registro_categoria = []

    def add(self, Categoria):
        self.registro_categoria.append(Categoria)

    def mostrar(self):
        for categoria in self.registro_categoria:
            print(categoria)

    def get_registro(self):
        return self.registro_categoria

    def edit_categoria(self, categoria_codigo, categoria):
        position_list = self.get_categoria_loc(categoria_codigo)
        self.__registro_categoria[position_list] = categoria

    def delete_categoria(self, categoria_codigo):
        position_list = self.get_categoria_loc(categoria_codigo)
        del self.__registro_categoria[position_list]

    def get_categoria_loc(self, codigo):
        for i, categoria in enumerate(self.__registro_categoria):
            if categoria.get_codigo() == codigo:
                return i
        else:
            return None

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

    def eliminar(self, estudiante,):
        del self.reg_reservas[estudiante]

    def encontrar_registro(self, estudiante):
        if estudiante in self.reg_reservas:
            return self.reg_reservas[estudiante]
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

