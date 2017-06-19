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
    pp([l.descripcion for l in reg_categorias.registro_categoria])


def showReserva():
    pp(reg_reservas.reg_reservas)

def showPrestamo():
    # pp(reg_prestamos.reg_prestamos)
    # pp([p for p in reg_prestamos.reg_prestamos])
    text = 'Nombre \t ISBN \t Fch Res \t Fch \t Hora'
    dic_reg_prestamo = reg_prestamos.reg_prestamos
    for estudiante in reg_prestamos.reg_prestamos:
        print(dic_reg_prestamo[estudiante])
        nombre_estudiante = estudiante.name
        isbn_libro = dic_reg_prestamo[estudiante][0].isbn
        fch_out = dic_reg_prestamo[estudiante][1]
        fch_ret = dic_reg_prestamo[estudiante][2]
        hora = dic_reg_prestamo[estudiante][3]

        text = text + '\n' + nombre_estudiante + ':\t' + 's' + '\t' + fch_out + '\t' + fch_ret + '\t' + hora

    pp(text)

showPrestamo()

# showReserva()