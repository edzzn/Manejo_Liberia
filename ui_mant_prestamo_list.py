from PyQt4 import QtCore, QtGui
from CoreData import loadD

class ListPrestamosWindow(QtGui.QWidget):
    """
        Lista todos las Reservas
    """
    def __init__(self):
        super(ListPrestamosWindow, self).__init__()

        self.createForm()

        self.setWindowIcon(QtGui.QIcon('images/th-list.png'))
        self.setWindowTitle("Prestamos - Agrega una Persona")
        self.setGeometry(650, 300, 440, 250)

    def createForm(self):
        lbl_registro = QtGui.QLabel('Prestamo:', self)
        self.textBrowser = QtGui.QTextBrowser(self)

        lbl_registro.move(20, 20)
        self.textBrowser.move(20, 40)
        self.textBrowser.resize(400, 200)

        reg_presatmo = loadD('p')
        dic_reg_prestamo = reg_presatmo.reg_prestamos
        text = 'Nombre \t ISBN \t Fch Res \t Fch \t Hora'
        for estudiante in dic_reg_prestamo:
            try:
                nombre_estudiante = estudiante.name
                isbn_libro = dic_reg_prestamo[estudiante][0].isbn
                fch_out = dic_reg_prestamo[estudiante][1]
                fch_ret = dic_reg_prestamo[estudiante][2]
                hora = dic_reg_prestamo[estudiante][3]

                text = text + '\n' + nombre_estudiante + ':\t' + isbn_libro + '\t' + fch_out + '\t' + fch_ret + '\t' + hora

            except Exception as e:
                pass

        self.textBrowser.setText(text)


if __name__ == '__main__':

    import sys

    app = QtGui.QApplication(sys.argv)
    mainWin = ListPrestamosWindow()
    mainWin.show()
    sys.exit(app.exec_())
