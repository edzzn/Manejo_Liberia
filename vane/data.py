from CoreData import RegistroReserva, RegistroPrestamos, saveD, loadD, Estudiante, Libro, Categoria


def init():
    """
        Permite llevar los datos de los Registros en las distintas ventanas
    """
    global reg_reservas
    global reg_prestamos
    global reg_libros
    global reg_estudiantes
    global reg_categoria
    reg_reservas = RegistroReserva()
    reg_prestamos = RegistroPrestamos()
    reg_libros = []
    reg_estudiantes = []
    reg_categoria=[]


if __name__ == '__main__':
    estudiante1 = Estudiante('001', 'Edisson', 'Reinozo')
    estudiante2 = Estudiante('002', 'Ediss', 'Reino')
    estudiante3 = Estudiante('003', 'Edi', 'Rei')
    estudiante4 = Estudiante('004', 'Ed', 'R')

    reg_estudiantes = [estudiante1, estudiante2, estudiante3, estudiante4]

    #            (isbn, numPag, idioma, autor, editorial, categoria):
    libro1 = Libro('001', 'N1', 'es', 'Aut1', 'cat1', '1991')
    libro2 = Libro('002', 'N2', 'es', 'Aut2', 'cat2', '1992')
    libro3 = Libro('003', 'N3', 'es', 'Aut3', 'cat3', '1993')
    libro4 = Libro('004', 'N4', 'es', 'Aut4', 'cat4', '1994')

    reg_libros = [libro1, libro2, libro3, libro4]

    reg_reservas = RegistroReserva()

    import random

    for e, l in zip(reg_estudiantes, reg_libros):
        i = random.randrange(10)
        j = random.randrange(10)
        reg_reservas.add(e, l, str(i), str(j), str(i+j))

    saveD('l', reg_libros)
    saveD('e', reg_estudiantes)
    saveD('r', reg_reservas)