import pickle

listaEstudiante=[]

class Estudiante():

    def __init__(self, cedula, name, lastname):
        self.id = cedula
        self.name = name
        self.lastname = lastname

    def add(self, cedula, name, lastname):
        listaEstudiante.append(cedula, name, lastname)




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

    def get_codigo(self):
        return self.codigo

    def get_descripcion(self):
        return self.descripcion

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

    def eliminar(self, estudiante):
        del self.reg_reservas[estudiante]

    def encontrar(self, id, isbn):
        tupla=()
        tupla2=()
        lista=[]
        for i in range(len(listaEstudiante)):
            tupla = (listaEstudiante[i])
            if (id == tupla[0]):
                if tupla in self.reg_reservas:
                    lista=self.reg_reservas[tupla]
                    for j in range(len(lista)):
                        tupla2=lista[j]
                        if (isbn==tupla2[0]):
                            return self.reg_reservas[tupla2]
                        else:
                            return None
            else:
                return None

    def validateUsuario(self,isbn,id):
        reg_estudiantes=loadD("e")
        reg_reservas=loadD("r")

        for estudiante in reg_estudiantes.reg_estudiante:
            if(estudiante.id==id):
                for registroReservas in reg_reservas:
                    if(registroReservas.isbn==isbn):
                        return registroReservas




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
