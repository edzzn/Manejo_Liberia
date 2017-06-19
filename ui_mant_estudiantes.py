from PyQt4 import QtGui
from ui_mant_reservas_new import NewReservaWindow
from ui_mant_estudiantes_new import NewEstudianteWindow
from ui_mant_estudiantes_edit import EditEstudianteWindow

# Debug only
import inspect


class MenuEstudiantes(QtGui.QWidget):
    """
        Ventana-menu para editar Estudiantes
    """
    def __init__(self):
        super(MenuEstudiantes, self).__init__()

        self.createButtons()

        self.setWindowTitle('Mantenimiento Estudiantes')

        self.setWindowIcon(QtGui.QIcon('images/user-plus.png'))
        self.setWindowTitle("Mantenimiento Estudiantes")
        self.setGeometry(650, 300, 150, 100)

    def createButtons(self):
        btn_new_estudiante = QtGui.QPushButton('Nuevo')
        btn_new_estudiante.clicked.connect(self.open_new_estudiante_window)

        btn_edit_estudiante = QtGui.QPushButton('Editar')
        btn_edit_estudiante.clicked.connect(self.open_edit_estudiante_window)

        btn_list_estudiante = QtGui.QPushButton('Listar')
        btn_list_estudiante.clicked.connect(self.close)

        btn_delete_estudiante = QtGui.QPushButton('Eliminar')
        btn_delete_estudiante.clicked.connect(self.close)


        hbox = QtGui.QHBoxLayout()
        hbox.addWidget(btn_new_estudiante)
        hbox.addWidget(btn_edit_estudiante)
        hbox.addWidget(btn_list_estudiante)
        hbox.addWidget(btn_delete_estudiante)
        vbox = QtGui.QVBoxLayout()
        vbox.addLayout(hbox)

        self.setLayout(vbox)

    def open_new_estudiante_window(self):
        self.new_estudiante_view = NewEstudianteWindow()
        self.new_estudiante_view.show()
        print(inspect.stack()[0][3])

        self.close()

    def open_edit_estudiante_window(self):
        self.edit_estudiante_view = EditEstudianteWindow()
        self.edit_estudiante_view.show()
        print(inspect.stack()[0][3])

        self.close()

    def open_list_estudiante_window(self):
        # self.new_reserva_view = NewReserva()
        # self.new_reserva_view.show()
        print(inspect.stack()[0][3])

        self.close()

    def open_delete_estudiante_window(self):
        # self.new_reserva_view = NewReserva()
        # self.new_reserva_view.show()
        print(inspect.stack()[0][3])

        self.close()

if __name__ == '__main__':

    import sys

    app = QtGui.QApplication(sys.argv)
    mainWin = MenuEstudiantes()
    mainWin.show()
    sys.exit(app.exec_())
