from PyQt4 import QtCore, QtGui
from CoreData import Categoria, loadD, saveD

class NewCategoriaWindow(QtGui.QWidget):
    """
    Ventana para agregar reservas
    """
    def __init__(self):
        super(NewCategoriaWindow, self).__init__()

        self.createForm()
        self.createButtons()

        self.setWindowIcon(QtGui.QIcon('images/user-plus.png'))
        self.setWindowTitle("Agrega una Categoria")
        self.setGeometry(650, 300, 400, 200)

    def addEstudiante(self):

        codigo = str(self.txt_codigo.text())
        descripcion = str(self.txt_descripcion.text())

        reg_categorias = loadD('c')

        if codigo == '' or descripcion == '' :
            self.lbl_info.setText('Datos incorrectos')

        elif reg_categorias.encontrar_categoria(codigo) is not None:
            self.lbl_info.setText('Datos duplicados')

        else:
            # Agregar un Categoria
            categoria = Categoria(codigo, descripcion)

            reg_categorias.add(categoria)

            saveD('c', reg_categorias)

            self.lbl_info.setText('Categoria Agregada')
            self.clear_campos()


    def clear_campos(self):
        self.txt_codigo.clear()
        self.txt_descripcion.clear()


    def createForm(self):
        lbl_codigo = QtGui.QLabel('Código', self)
        lbl_descripcion = QtGui.QLabel('Descripción', self)

        self.txt_codigo = QtGui.QLineEdit(self)
        self.txt_descripcion = QtGui.QLineEdit(self)

        self.lbl_info = QtGui.QLabel(self)

        lbl_codigo.move(50, 25)
        self.txt_codigo.move(200, 25)

        lbl_descripcion.move(50, 75)
        self.txt_descripcion.move(200, 75)

        self.lbl_info.move(200, 120)
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
    mainWin = NewCategoriaWindow()
    mainWin.show()
    sys.exit(app.exec_())
