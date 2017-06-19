from PyQt4 import QtCore, QtGui
from CoreData import RegistroReserva, saveD, loadD, validateLibro, validateEstudiante

class EditReservaWindow(QtGui.QWidget):
    """
    Ventana para agregar reservas
    
    Not DONE
    """
    def __init__(self, estudiante_id, isbn):
        super(EditReservaWindow, self).__init__()

        self.estudiante_id = estudiante_id
        self.isbn = isbn

        self.createForm()
        self.createButtons()

        self.setWindowIcon(QtGui.QIcon('images/user-plus.png'))
        self.setWindowTitle("Editar una Reserva")
        self.setGeometry(650, 300, 400, 330)

    def editReserva(self):

        id_estudiante = str(self.txt_id_estudiante.text())
        libro_isbn = str(self.txt_nombre_libro.text())
        fch_a_reservar = str(self.txt_fch_a_reservar.text())
        fch_reserva = str(self.txt_fch_reserva.text())
        hora_reserva=str(self.txt_hora_reserva.text())

        if id_estudiante == '' or libro_isbn == '' or fch_a_reservar == '' or fch_reserva == '' or hora_reserva == '':
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

            reg_reservas.add(estudiante, libro, fch_a_reservar, fch_reserva, hora_reserva)

            saveD('r', reg_reservas)

            self.lbl_info.setText('Reserva Modificada')
            self.clear_campos()

    def clear_campos(self):
        self.txt_id_estudiante.clear()
        self.txt_nombre_libro.clear()
        self.txt_fch_a_reservar.clear()
        self.txt_fch_reserva.clear()
        self.txt_hora_reserva.clear()

    def update_campos(self):
        reg_reservas = loadD('r')
        estudiante, reserva = reg_reservas.registro_id_isbn(self.estudiante_id, self.isbn)
        print(reserva)
        libro = reserva[0]
        fecha_a_reservas = reserva[1]
        fecha_reserva = reserva[2]
        hora = reserva[3]

        # libro, fecha_a_reservas, fecha_reserva, hora = lista_reservas[0]
        self.txt_id_estudiante.setText(estudiante.name)
        self.txt_nombre_libro.setText(libro.isbn)
        self.txt_fch_a_reservar.setText(fecha_a_reservas)
        self.txt_fch_reserva.setText(fecha_reserva)
        self.txt_hora_reserva.setText(hora)

    def createForm(self):

        lbl_id_estudiante = QtGui.QLabel('Id Estudiante', self)
        lbl_nombre_libro = QtGui.QLabel('Libro', self)
        lbl_fch_a_reservar = QtGui.QLabel('Fecha a reservar', self)
        lbl_fch_reserva = QtGui.QLabel('Fecha de reserva', self)
        lbl_hora_reserva = QtGui.QLabel('Hora de reserva', self)
        self.txt_id_estudiante = QtGui.QLineEdit(self)
        self.txt_nombre_libro = QtGui.QLineEdit(self)
        self.txt_fch_a_reservar = QtGui.QLineEdit(self)
        self.txt_fch_reserva = QtGui.QLineEdit(self)
        self.txt_hora_reserva = QtGui.QLineEdit(self)

        self.lbl_info = QtGui.QLabel(self)

        lbl_id_estudiante.move(50, 25)
        self.txt_id_estudiante.setReadOnly(True)
        self.txt_id_estudiante.move(200, 25)

        lbl_nombre_libro.move(50, 75)
        self.txt_nombre_libro.move(200, 75)

        lbl_fch_a_reservar.move(50, 125)
        self.txt_fch_a_reservar.move(200, 125)

        lbl_fch_reserva.move(50, 175)
        self.txt_fch_reserva.move(200, 175)

        lbl_hora_reserva.move(50, 225)
        self.txt_hora_reserva.move(200, 225)

        self.lbl_info.move(200, 220)
        self.lbl_info.resize(200, 20)

        self.update_campos()

    def createButtons(self):
        okBtn = QtGui.QPushButton('OK')
        okBtn.clicked.connect(self.editReserva)
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
    mainWin = EditReservaWindow()
    mainWin.show()
    sys.exit(app.exec_())
