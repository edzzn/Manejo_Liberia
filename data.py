from CoreData import RegistroReserva, RegistroPrestamos

def init():
    """
        Permite llevar los datos de los Registros en las distintas ventanas
    """
    global reg_reservas
    global reg_prestamos
    reg_reservas = RegistroReserva()
    reg_prestamos = RegistroPrestamos()


if __name__ == '__main__':
    # init()
    reg_reservas = RegistroReserva()
    reg_reservas.add('edz', 'lib', 12, 15)
    reg_reservas.add('edd', 'lib2', '41', '5')
    reg_reservas.add('edd', 'lib3', '42', '7')
    print(reg_reservas.reg_reservas)