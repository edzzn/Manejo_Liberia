from CoreData import RegistroReserva, RegistroPrestamos, saveD, loadD
from CoreData import Estudiante, Libro, RegistroEstudiante, RegistroLibro


def init():
    """
        Permite llevar los datos de los Registros en las distintas ventanas
    """
    global reg_reservas
    global reg_prestamos
    global reg_libros
    global reg_estudiantes
    reg_reservas = RegistroReserva()
    reg_prestamos = RegistroPrestamos()
    reg_libros = []
    reg_estudiantes = []


if __name__ == '__main__':
    estudiante1 = Estudiante('001', 'Edisson', 'Reinozo')
    estudiante2 = Estudiante('002', 'Ediss', 'Reino')
    estudiante3 = Estudiante('003', 'Edi', 'Rei')
    estudiante4 = Estudiante('004', 'Ed', 'R')

    reg_estudiantes = RegistroEstudiante()
    reg_estudiantes.add(estudiante1)
    reg_estudiantes.add(estudiante2)
    reg_estudiantes.add(estudiante3)
    reg_estudiantes.add(estudiante4)


    print(reg_estudiantes.reg_estudiante[0])

    #            (isbn, numPag, idioma, autor, editorial, categoria):
    libro1 = Libro('001', 'N1', 'es', 'Aut1', 'cat1', '1991')
    libro2 = Libro('002', 'N2', 'es', 'Aut2', 'cat2', '1992')
    libro3 = Libro('003', 'N3', 'es', 'Aut3', 'cat3', '1993')
    libro4 = Libro('004', 'N4', 'es', 'Aut4', 'cat4', '1994')

    reg_libros = RegistroLibro()
    reg_libros.add(libro1)
    reg_libros.add(libro2)
    reg_libros.add(libro3)
    reg_libros.add(libro4)

    reg_reservas = RegistroReserva()


    import random

    for i in range(4):
        b = random.randrange(10)
        j = random.randrange(10)
        reg_reservas.add(reg_estudiantes.reg_estudiante[i], reg_libros.reg_libro[i], str(b), str(j), str(i+j))

    saveD('l', reg_libros)
    saveD('e', reg_estudiantes)
    saveD('r', reg_reservas)