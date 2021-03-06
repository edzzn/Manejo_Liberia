import random
from CoreData import RegistroReserva, RegistroPrestamos, saveD, loadD
from CoreData import Estudiante, Libro, RegistroEstudiante, RegistroLibro
from CoreData import Categoria, RegistroCategoria

# Archivo para pruebas permite inicializar los distintos archivos necesarios para
# pruebas y ejecución de la aplicación

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


    print(type(reg_estudiantes.encontrar_estudiante('002')))



    cat1 = Categoria('011', 'Cat1')
    cat2 = Categoria('022', 'Cat2')
    cat3 = Categoria('033', 'Cat3')
    cat4 = Categoria('044', 'Cat4')

    reg_categoria = RegistroCategoria()
    reg_categoria.add(cat1)
    reg_categoria.add(cat2)
    reg_categoria.add(cat3)
    reg_categoria.add(cat4)

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

    reg_prestamos = RegistroPrestamos()

    for i in range(4):
        b = random.randrange(10)
        j = random.randrange(10)
        reg_reservas.add(reg_estudiantes.reg_estudiante[i], reg_libros.reg_libro[i], str(b), str(j), str(i+j))
        reg_prestamos.add(reg_estudiantes.reg_estudiante[i], reg_libros.reg_libro[i], str(b), str(j), str(i+j))

    saveD('l', reg_libros)
    saveD('e', reg_estudiantes)
    saveD('r', reg_reservas)
    saveD('c', reg_categoria)
    saveD('p', reg_prestamos)
