from PyQt4 import QtCore, QtGui
from CoreData import Estudiante
import data

class NewEstudianteWindow(QtGui.QWidget):
    """
    Ventana para agregar reservas
    """
    def __init__(self):
        super(NewEstudianteWindow, self).__init__()

        self.createForm()
        self.createButtons()

        self.setWindowIcon(QtGui.QIcon('images/user-plus.png'))
        self.setWindowTitle("Agrega un estudiante")
        self.setGeometry(650, 300, 400, 330)

    def addEstudiante(self):

        id_estudiante = str(self.txt_id_estudiante.text())
        nombre = str(self.txt_nombre.text())
        apellido = str(self.txt_apellido.text())


        if id_estudiante == '' or nombre == '' or apellido == '':
            self.lbl_info.setText('Datos incorrectos')

        # elif id_estudiante in data.reg_estudiantes:
        #     self.lbl_info.setText('Datos duplicados')
        else:
            data.reg_estuantes.add(id_estudiante, nombre, apellido)
            self.lbl_info.setText('Reserva Agregada')
            self.clear_campos()


    def clear_campos(self):
        self.txt_id_estudiante.clear()
        self.txt_nombre.clear()
        self.txt_apellido.clear()


    def createForm(self):
        lbl_id_estudiante = QtGui.QLabel('Id', self)
        lbl_nombre = QtGui.QLabel('Nombre', self)
        lbl_apellido = QtGui.QLabel('Apellido', self)

        self.txt_id_estudiante = QtGui.QLineEdit(self)
        self.txt_nombre = QtGui.QLineEdit(self)
        self.txt_apellido = QtGui.QLineEdit(self)


        self.lbl_info = QtGui.QLabel(self)

        lbl_id_estudiante.move(50, 25)
        self.txt_id_estudiante.move(200, 25)

        lbl_nombre.move(50, 75)
        self.txt_nombre.move(200, 75)

        lbl_apellido.move(50, 125)
        self.txt_apellido.move(200, 125)

        self.lbl_info.move(200, 220)
        self.lbl_info.resize(200, 20)

    def createButtons(self):
        okBtn = QtGui.QPushButton('OK')
        okBtn.clicked.connect(self.addEstudiante)
        cancelBtn = QtGui.QPushButton('Cancelar')
        cancelBtn.clicked.connect(self.close)
        hbox = QtGui.QHBoxLayout()
        hbox.addStretch(1)
        hbox.addWidget(okBtn)
        hbox.addWidget(cancelBtn)

        vbox = QtGui.QVBoxLayout()
        vbox.addStretch(1)
        vbox.addLayout(hbox)

        self.setLayout(vbox)

if __name__ == '__main__':

    import sys

    app = QtGui.QApplication(sys.argv)
    mainWin = NewEstudianteWindow()
    mainWin.show()
    sys.exit(app.exec_())
