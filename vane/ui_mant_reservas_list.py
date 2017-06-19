from PyQt4 import QtCore, QtGui
from CoreData import loadD

class ListReservasWindow(QtGui.QWidget):
    """
        Lista todos las Reservas
    """
    def __init__(self):
        super(ListReservasWindow, self).__init__()

        self.createForm()

        self.setWindowIcon(QtGui.QIcon('images/th-list.png'))
        self.setWindowTitle("Reservas - Agrega una Persona")
        self.setGeometry(650, 300, 440, 250)

    def createForm(self):
        lbl_registro = QtGui.QLabel('Reservas:', self)
        self.textBrowser = QtGui.QTextBrowser(self)

        lbl_registro.move(20, 20)
        self.textBrowser.move(20, 40)
        self.textBrowser.resize(400, 200)

        reg_reservas = loadD('r')
        dic_reg_reservas = reg_reservas.reg_reservas
        text = 'Nombre \t ISBN \t Fch Res \t Fch \t Hora'
        for estudiante in dic_reg_reservas:

            try:
                nombre_estudiante = estudiante.name
                isbn_libro = dic_reg_reservas[estudiante][0][0].isbn
                fch_out = dic_reg_reservas[estudiante][0][1]
                fch_ret = dic_reg_reservas[estudiante][0][2]
                hora = dic_reg_reservas[estudiante][0][3]

                text = text + '\n' + nombre_estudiante + ':\t' + isbn_libro + '\t' + fch_out + '\t' + fch_ret + '\t' + hora

            except Exception as e:
                pass

        self.textBrowser.setText(text)


if __name__ == '__main__':

    import sys

    app = QtGui.QApplication(sys.argv)
    mainWin = ListReservasWindow()
    mainWin.show()
    sys.exit(app.exec_())
