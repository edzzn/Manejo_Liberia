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
    pp([l.id for l in reg_estudiantes.reg_estudiante])


def showCategoria():
    pp([l.codigo for l in reg_categorias.registro_categoria])

def showReserva():
    pp(reg_reservas.reg_reservas)



showCategoria()

# showReserva()