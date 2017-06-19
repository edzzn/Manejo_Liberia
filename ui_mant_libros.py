from PyQt4 import QtGui
from ui_mant_libros_new import NewLibrosWindow
from ui_mant_libros_edit import EditLibrosWindow

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
        btn_new_libros = QtGui.QPushButton('Nuevo')
        btn_new_libros.clicked.connect(self.open_new_libros_window)

        btn_edit_libros = QtGui.QPushButton('Editar')
        btn_edit_libros.clicked.connect(self.open_edit_libros_window)

        btn_list_libros = QtGui.QPushButton('Listar')
        btn_list_libros.clicked.connect(self.close)

        btn_delete_libros = QtGui.QPushButton('Eliminar')
        btn_delete_libros.clicked.connect(self.close)


        hbox = QtGui.QHBoxLayout()
        hbox.addWidget(btn_new_libros)
        hbox.addWidget(btn_edit_libros)
        hbox.addWidget(btn_list_libros)
        hbox.addWidget(btn_delete_libros)
        vbox = QtGui.QVBoxLayout()
        vbox.addLayout(hbox)

        self.setLayout(vbox)

    def open_new_libros_window(self):
        self.new_libros_view = NewLibrosWindow()
        self.new_libros_view.show()
        print(inspect.stack()[0][3])

        self.close()

    def open_edit_libros_window(self):
        self.edit_libros_view = EditLibrosWindow()
        self.edit_libros_view.show()
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
