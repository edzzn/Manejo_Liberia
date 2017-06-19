from PyQt4 import QtCore, QtGui
from CoreData import loadD, saveD, Libro
import data

class NewLibrosWindow(QtGui.QWidget):
    """
    Ventana para agregar reservas
    """
    def __init__(self):
        super(NewLibrosWindow, self).__init__()

        self.createForm()
        self.createButtons()

        self.setWindowIcon(QtGui.QIcon('images/user-plus.png'))
        self.setWindowTitle("Agrega un libro")
        self.setGeometry(650, 300, 400, 400)

    def addLibro(self):

        isbn = str(self.txt_isbn.text())
        numPag = str(self.txt_numPag.text())
        idioma = str(self.txt_idioma.text())
        autor = str(self.txt_autor.text())
        editorial=str(self.txt_editorial.text())
        categoria=str(self.txt_categoria.text())

        reg_libros = loadD('l')

        if isbn == '' or numPag == '' or idioma == '' or autor == '' or editorial == '' or categoria == '':
            self.lbl_info.setText('Datos incorrectos')

        elif reg_libros.encontrar_libro(isbn) is not None:
            self.lbl_info.setText('Datos duplicados')

        else:
            # Agregar un Libro
            libro = Libro(isbn, numPag, idioma, autor, editorial, categoria)

            reg_libros.add(libro)

            saveD('l', reg_libros)

            self.lbl_info.setText('Reserva Agregada')
            self.clear_campos()


    def clear_campos(self):
        self.txt_isbn.clear()
        self.txt_numPag.clear()
        self.txt_idioma.clear()
        self.txt_autor.clear()
        self.txt_editorial.clear()
        self.txt_categoria.clear()

    def createForm(self):
        lbl_isbn = QtGui.QLabel('ISBN', self)
        lbl_numPag = QtGui.QLabel('Número de páginas', self)
        lbl_idioma = QtGui.QLabel('Idioma', self)
        lbl_autor = QtGui.QLabel('Autor', self)
        lbl_editorial = QtGui.QLabel('Editorial', self)
        lbl_categoria = QtGui.QLabel('Categoría', self)
        self.txt_isbn = QtGui.QLineEdit(self)
        self.txt_numPag = QtGui.QLineEdit(self)
        self.txt_idioma = QtGui.QLineEdit(self)
        self.txt_autor = QtGui.QLineEdit(self)
        self.txt_editorial=QtGui.QLineEdit(self)
        self.txt_categoria=QtGui.QLineEdit(self)

        self.lbl_info = QtGui.QLabel(self)

        lbl_isbn.move(50, 25)
        self.txt_isbn.move(200, 25)

        lbl_numPag.move(50, 75)
        self.txt_numPag.move(200, 75)

        lbl_idioma.move(50, 125)
        self.txt_idioma.move(200, 125)

        lbl_autor.move(50, 175)
        self.txt_autor.move(200, 175)

        lbl_editorial.move(50, 225)
        self.txt_editorial.move(200, 225)

        lbl_categoria.move(50, 275)
        self.txt_categoria.move(200, 275)

        self.lbl_info.move(200, 320)
        self.lbl_info.resize(200, 20)

    def createButtons(self):
        okBtn = QtGui.QPushButton('OK')
        okBtn.clicked.connect(self.addLibro)
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
    mainWin = NewLibrosWindow()
    mainWin.show()
    sys.exit(app.exec_())
