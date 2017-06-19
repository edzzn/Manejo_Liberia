from PyQt4 import QtCore, QtGui
from CoreData import Categoria, saveD, loadD
import data


class EditCategoriaWindow(QtGui.QWidget):
    """
    Ventana para editar una categoria

    Not DONE
    """

    def __init__(self, codigo):
        super(EditCategoriaWindow, self).__init__()

        self.codigo = codigo
        self.createForm()
        self.createButtons()

        self.setWindowIcon(QtGui.QIcon('images/user-plus.png'))
        self.setWindowTitle("Editar una categoria")
        self.setGeometry(650, 300, 400, 200)

    def addEstudiante(self):

        codigo = str(self.txt_codigo.text())
        descripcion = str(self.txt_descripcion.text())


        if codigo == '' or descripcion== '':
            self.lbl_info.setText('Datos incorrectos')

        else:
            # Agregar un Categoria
            reg_categorias = loadD('c')
            for cat in reg_cat.registro_categoria:
                if cat.codigo == codigo:
                    cat.edit(descripcion)

            saveD('c', reg_categorias)

            self.lbl_info.setText('Categoria Editada')
            self.clear_campos()


    def clear_campos(self):
        self.txt_codigo.clear()
        self.txt_descripcion.clear()

    def update_campos(self):
        reg_categoria = loadD('c')
        categoria = reg_categoria.encontrar_categoria(self.codigo)

        self.txt_codigo.setText(self.codigo)
        self.txt_descripcion.setText(categoria.descripcion)

    def createForm(self):

        lbl_codigo = QtGui.QLabel('Código', self)
        lbl_descripcion = QtGui.QLabel('Descipción', self)
        self.txt_codigo = QtGui.QLineEdit(self)
        self.txt_descripcion = QtGui.QLineEdit(self)

        self.lbl_info = QtGui.QLabel(self)

        lbl_codigo.move(50, 25)
        self.txt_codigo.setReadOnly(True)
        self.txt_codigo.move(200, 25)

        lbl_descripcion.move(50, 75)
        self.txt_descripcion.move(200, 75)

        self.lbl_info.move(200, 220)
        self.lbl_info.resize(200, 20)

        self.update_campos()

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
    mainWin = EditCategoriaWindow('012')
    mainWin.show()
    sys.exit(app.exec_())
