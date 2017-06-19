from PyQt4 import QtCore, QtGui
from CoreData import saveD, loadD, validateEstudiante, validateLibro

class DeleteReservaWindow(QtGui.QWidget):
    """
        Pide un id, y un isbn para eliminar el registro
    """
    def __init__(self):
        super(DeleteReservaWindow, self).__init__()

        self.createForm()
        self.createButtons()

        self.setWindowIcon(QtGui.QIcon('images/edit.png'))
        self.setWindowTitle("Eliminar una Reserva")
        self.setGeometry(650, 300, 350, 175 )

    def createForm(self):
        lbl_id = QtGui.QLabel('Id', self)
        self.txt_id = QtGui.QLineEdit(self)

        lbl_isbn = QtGui.QLabel('isbn', self)
        self.txt_isbn = QtGui.QLineEdit(self)

        self.lbl_info = QtGui.QLabel('', self)

        lbl_id.move(50, 25)
        self.txt_id.move(150, 25)

        lbl_isbn.move(50, 60)
        self.txt_isbn.move(150, 60)

        self.lbl_info.move(150, 85)
        self.lbl_info.resize(200,25)

    def check(self):
        estudiante_id = self.txt_id.text()
        isbn = self.txt_isbn.text()

        if estudiante_id == '' or isbn == '':
            self.lbl_info.setText('Datos incorrectos')

        elif not validateEstudiante(estudiante_id):
            self.lbl_info.setText('Estudiante no Registado')

        elif not validateLibro(isbn):
            self.lbl_info.setText('Libro no Registado')
        else:
            # Eliminamos el reigstro
            self.eliminar()
            QtGui.QMessageBox.about(self, "Reserva Eliminada",
                                    "El registro fue <b>eliminado</b>")
            self.close()

    def eliminar(self):
        estudiante_id = self.txt_id.text()
        isbn = self.txt_isbn.text()

        reg_reservas = loadD('r')

        for estudiante in reg_reservas.reg_reservas:
            if estudiante.id == estudiante_id:
                reg_reservas.eliminar(estudiante, isbn)

        saveD('r', reg_reservas)

    def createButtons(self):
        okBtn = QtGui.QPushButton('OK')
        okBtn.clicked.connect(self.check)
        cancelBtn = QtGui.QPushButton('Cancel')
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
    mainWin = DeleteReservaWindow()
    mainWin.show()
    sys.exit(app.exec_())
