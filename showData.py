from pprint import pprint as pp
from CoreData import loadD

reg_libros = loadD('l')
reg_reservas = loadD('r')
reg_estudiantes = loadD('e')
reg_categorias = loadD('c')
reg_prestamos = loadD('p')

def showLibros():
    pp([l.isbn for l in reg_libros.reg_libro])

def showEstudiantes():
    pp(reg_estudiantes.reg_estudiante)

def showCategoria():
    pp(reg_libros.reg_libro)

def showReserva():
    pp(reg_reservas.reg_reservas)



showLibros()

# showReserva()