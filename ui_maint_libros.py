from PyQt4 import QtGui
from ui_mantenimiento_reservas_new import NewReservaWindow

# Debug only
import inspect


class MenuLibros(QtGui.QWidget):
    """
        Ventana-menu para editar Libros
    """
    def __init__(self):
        super(MenuLibros, self).__init__()

        self.createButtons()

        self.setWindowTitle('Mantenimiento Libros')

        self.setWindowIcon(QtGui.QIcon('images/user-plus.png'))
        self.setWindowTitle("Mantenimiento Libros")
        self.setGeometry(650, 300, 150, 100)

    def createButtons(self):
        btn_new_reserva = QtGui.QPushButton('Nuevo')
        btn_new_reserva.clicked.connect(self.close)

        btn_edit_reserva = QtGui.QPushButton('Editar')
        btn_edit_reserva.clicked.connect(self.close)

        btn_list_reserva = QtGui.QPushButton('Listar')
        btn_list_reserva.clicked.connect(self.close)

        btn_delete_reserva = QtGui.QPushButton('Eliminar')
        btn_delete_reserva.clicked.connect(self.close)


        hbox = QtGui.QHBoxLayout()
        hbox.addWidget(btn_new_reserva)
        hbox.addWidget(btn_edit_reserva)
        hbox.addWidget(btn_list_reserva)
        hbox.addWidget(btn_delete_reserva)
        vbox = QtGui.QVBoxLayout()
        vbox.addLayout(hbox)

        self.setLayout(vbox)

    def open_new_reserva_window(self):
        self.new_reserva_view = NewReservaWindow()
        self.new_reserva_view.show()
        print(inspect.stack()[0][3])

        self.close()

    def open_edit_reserva_window(self):
        # self.edit_reserva_view = EditReserva()
        # self.edit_reserva_view.show()
        print(inspect.stack()[0][3])

        self.close()

    def open_list_reserva_window(self):
        # self.new_reserva_view = NewReserva()
        # self.new_reserva_view.show()
        print(inspect.stack()[0][3])

        self.close()

    def open_delete_reserva_window(self):
        # self.new_reserva_view = NewReserva()
        # self.new_reserva_view.show()
        print(inspect.stack()[0][3])

        self.close()

if __name__ == '__main__':

    import sys

    app = QtGui.QApplication(sys.argv)
    mainWin = MenuLibros()
    mainWin.show()
    sys.exit(app.exec_())
