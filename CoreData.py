class Persona():

    def __init__(self, cedula, name, lastname):
        self.id = cedula
        self.name = name
        self.lastname = lastname

class Estudiante(Persona):
    def __init__(self, id, name, lastname):
        super.__init__(id, name, lastname)


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

    def add(self, persona, libro, fecha_prestamo, fecha_devolucion):
        nuevo_registro = (libro, fecha_prestamo, fecha_devolucion)
        self.num_reservaciones += 1
        if persona in self.reg_reservas:
            self.reg_reservas[persona].append(nuevo_registro)
        else:
            self.reg_reservas[persona] = [nuevo_registro]

class RegistroPrestamos():

    def __init__(self):
        # Registro de prestamo: Dicitonary {Estudiante, [(Libro, fecha_o, fecha_final),],}
        self.reg_prestamos = {}
        self.num_prestamo = 0

    def add(self, persona, libro, fecha_prestamo, fecha_devolucion=""):
        nuevo_registro = (libro, fecha_prestamo, fecha_devolucion)

        self.num_prestamo =+ 1
        if persona in self.reg_prestamos:
            self.reg_prestamos[persona].append(nuevo_registro)
        else:
            self.reg_prestamos[persona] = nuevo_registro
