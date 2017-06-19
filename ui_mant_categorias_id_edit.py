from PyQt4 import QtCore, QtGui
from CoreData import validateEstudiante, validateLibro, loadD
from ui_mant_categorias_edit import EditCategoriaWindow


class GetIdEditWindow(QtGui.QWidget):
    def __init__(self):
        super(GetIdEditWindow, self).__init__()

        self.createForm()
        self.createButtons()

        self.setWindowIcon(QtGui.QIcon('images/edit.png'))
        self.setWindowTitle("Editar una Categoria")
        self.setGeometry(650, 300, 350, 130)

    def createForm(self):
        lbl_id = QtGui.QLabel('Codigo', self)
        self.txt_id = QtGui.QLineEdit(self)

        self.lbl_info = QtGui.QLabel('', self)

        lbl_id.move(50, 25)
        self.txt_id.move(150, 25)

        self.lbl_info.move(150, 55)
        self.lbl_info.resize(200,25)

    def check(self):
        codigo = self.txt_id.text()

        reg_categoria = loadD('c')

        if codigo == '':
            self.lbl_info.setText('Datos incorrectos')

        elif reg_categoria.encontrar_categoria(codigo) is None:
            self.lbl_info.setText('Categoria no Registada')

        else:
            self.open_edit_window()

    def open_edit_window(self):
        codigo = self.txt_id.text()
        self.edit_view = EditCategoriaWindow(codigo)
        self.edit_view.show()
        self.close()

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
    mainWin = GetIdEditWindow()
    mainWin.show()
    sys.exit(app.exec_())
