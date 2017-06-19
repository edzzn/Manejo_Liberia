from PyQt4 import QtCore, QtGui
from CoreData import validateLibro, validateEstudiante, loadD, saveD, RegistroEstudiante, RegistroLibro

class MenuPrestamo(QtGui.QWidget):
    """
    Ventana para agregar reservas
    """
    def __init__(self):
        super(MenuPrestamo, self).__init__()

        self.createForm()
        self.createButtons()

        self.setWindowIcon(QtGui.QIcon('images/user-plus.png'))
        self.setWindowTitle("Agrega una Reserva")
        self.setGeometry(650, 300, 400, 330)

    def addReserva(self):

        id_estudiante = str(self.txt_id_estudiante.text())
        libro_isbn = str(self.txt_nombre_libro.text())
        fch_reserva = str(self.txt_fch_reserva.text())
        hora_reserva=str(self.txt_hora_reserva.text())

        if id_estudiante == '' or libro_isbn == ''or fch_reserva == '' or hora_reserva == '':
            self.lbl_info.setText('Datos incorrectos')

        elif not validateEstudiante(id_estudiante):
            self.lbl_info.setText('Estudiante no Registado')

        elif not validateLibro(libro_isbn):
            self.lbl_info.setText('Libro no Registado')
        else:
            # Agregar la reserva
            reg_estudiantes = loadD('e')
            estudiante = reg_estudiantes.encontrar_estudiante(id_estudiante)

            reg_libro = loadD('l')

            libro = reg_libro.encontrar_libro(libro_isbn)

            reg_reservas = loadD('r')

            reg_reservas.add(estudiante, libro, fch_reserva, hora_reserva)

            saveD('r', reg_reservas)

            self.lbl_info.setText('Reserva Agregada')
            self.clear_campos()


    def clear_campos(self):
        self.txt_id_estudiante.clear()
        self.txt_nombre_libro.clear()
        self.txt_fch_reserva.clear()
        self.txt_hora_reserva.clear()

    def createForm(self):
        lbl_id_estudiante = QtGui.QLabel('Id Estudiante', self)
        lbl_nombre_libro = QtGui.QLabel('Libro', self)
        lbl_fch_reserva = QtGui.QLabel('Fecha de reserva', self)
        lbl_hora_reserva = QtGui.QLabel('Hora de reserva', self)
        self.txt_id_estudiante = QtGui.QLineEdit(self)
        self.txt_nombre_libro = QtGui.QLineEdit(self)
        self.txt_fch_reserva = QtGui.QLineEdit(self)
        self.txt_hora_reserva=QtGui.QLineEdit(self)

        self.lbl_info = QtGui.QLabel(self)

        lbl_id_estudiante.move(50, 25)
        self.txt_id_estudiante.move(200, 25)

        lbl_nombre_libro.move(50, 75)
        self.txt_nombre_libro.move(200, 75)

        lbl_fch_reserva.move(50, 125)
        self.txt_fch_reserva.move(200, 125)

        lbl_hora_reserva.move(50, 175)
        self.txt_hora_reserva.move(200, 175)

        self.lbl_info.move(200, 255)
        self.lbl_info.resize(200, 20)

    def createButtons(self):
        okBtn = QtGui.QPushButton('OK')
        okBtn.clicked.connect(self.addReserva)
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
    mainWin = MenuPrestamo()
    mainWin.show()
    sys.exit(app.exec_())