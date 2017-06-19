#! /urs/bin/python
# -*- coding: utf-8 -*-

"""
Descripcion: Aplicacion sencilla de manejo de prestamo de libros


"""

import sys
from PyQt4 import QtGui, QtCore
from ui_main import MainWindow
import data


def main():
    app = QtGui.QApplication(sys.argv)
    data.init()
    main_view = MainWindow()
    main_view.show()

    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
