from PyQt4 import QtGui
from ui_mant_categorias_edit import EditCategoriaWindow
from ui_mant_categorias_new import NewCategoriaWindow


# Debug only
import inspect


class MenuCategorias(QtGui.QWidget):
    """
        Ventana-menu para editar Libros
    """
    def __init__(self):
        super(MenuCategorias, self).__init__()

        self.createButtons()

        self.setWindowTitle('Mantenimiento Categorias')

        self.setWindowIcon(QtGui.QIcon('images/user-plus.png'))
        self.setWindowTitle("Mantenimiento Categorias")
        self.setGeometry(650, 300, 150, 100)

    def createButtons(self):
        btn_new_categoria = QtGui.QPushButton('Nuevo')
        btn_new_categoria.clicked.connect(self.open_new_categoria_window)

        btn_edit_categoria = QtGui.QPushButton('Editar')
        btn_edit_categoria.clicked.connect(self.open_edit_categoria_window)

        btn_list_categoria = QtGui.QPushButton('Listar')
        btn_list_categoria.clicked.connect(self.close)

        btn_delete_categoria = QtGui.QPushButton('Eliminar')
        btn_delete_categoria.clicked.connect(self.close)


        hbox = QtGui.QHBoxLayout()
        hbox.addWidget(btn_new_categoria)
        hbox.addWidget(btn_edit_categoria)
        hbox.addWidget(btn_list_categoria)
        hbox.addWidget(btn_delete_categoria)
        vbox = QtGui.QVBoxLayout()
        vbox.addLayout(hbox)

        self.setLayout(vbox)

    def open_new_categoria_window(self):
        self.new_categoria_view = NewCategoriaWindow()
        self.new_categoria_view.show()
        print(inspect.stack()[0][3])

        self.close()

    def open_edit_categoria_window(self):
        self.new_categoria_view = EditCategoriaWindow()
        self.new_categoria_view.show()
        print(inspect.stack()[0][3])

        self.close()

    def open_list_categoria_window(self):
        # self.new_reserva_view = NewReserva()
        # self.new_reserva_view.show()
        print(inspect.stack()[0][3])

        self.close()

    def open_delete_categoria_window(self):
        # self.new_reserva_view = NewReserva()
        # self.new_reserva_view.show()
        print(inspect.stack()[0][3])

        self.close()

if __name__ == '__main__':

    import sys

    app = QtGui.QApplication(sys.argv)
    mainWin = MenuCategorias()
    mainWin.show()
    sys.exit(app.exec_())
