# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MantenimientoLibroBuscar.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(440, 555)
        self.igbgi = QtGui.QDialogButtonBox(Form)
        self.igbgi.setEnabled(True)
        self.igbgi.setGeometry(QtCore.QRect(120, 510, 176, 27))
        self.igbgi.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.igbgi.setObjectName(_fromUtf8("igbgi"))
        self.pushButton = QtGui.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(80, 220, 99, 27))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.checkBox_2 = QtGui.QCheckBox(Form)
        self.checkBox_2.setGeometry(QtCore.QRect(80, 70, 99, 22))
        self.checkBox_2.setObjectName(_fromUtf8("checkBox_2"))
        self.lineEdit = QtGui.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(80, 190, 181, 27))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.listWidget = QtGui.QListWidget(Form)
        self.listWidget.setGeometry(QtCore.QRect(80, 300, 291, 31))
        self.listWidget.setObjectName(_fromUtf8("listWidget"))
        self.label_2 = QtGui.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(80, 267, 261, 20))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.checkBox_3 = QtGui.QCheckBox(Form)
        self.checkBox_3.setGeometry(QtCore.QRect(80, 100, 99, 22))
        self.checkBox_3.setObjectName(_fromUtf8("checkBox_3"))
        self.checkBox = QtGui.QCheckBox(Form)
        self.checkBox.setGeometry(QtCore.QRect(80, 40, 99, 22))
        self.checkBox.setObjectName(_fromUtf8("checkBox"))
        self.label = QtGui.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(80, 170, 191, 17))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_5 = QtGui.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(80, 10, 201, 31))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.checkBox_4 = QtGui.QCheckBox(Form)
        self.checkBox_4.setGeometry(QtCore.QRect(80, 130, 99, 22))
        self.checkBox_4.setObjectName(_fromUtf8("checkBox_4"))
        self.label_3 = QtGui.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(80, 350, 261, 20))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.listWidget_2 = QtGui.QListWidget(Form)
        self.listWidget_2.setGeometry(QtCore.QRect(80, 380, 291, 101))
        self.listWidget_2.setObjectName(_fromUtf8("listWidget_2"))

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.pushButton.setText(_translate("Form", "Buscar", None))
        self.checkBox_2.setText(_translate("Form", "CheckBox", None))
        self.label_2.setText(_translate("Form", "Libro relacionados con la busqueda", None))
        self.checkBox_3.setText(_translate("Form", "CheckBox", None))
        self.checkBox.setText(_translate("Form", "CheckBox", None))
        self.label.setText(_translate("Form", "Introducir nombre del libro", None))
        self.label_5.setText(_translate("Form", "Seleccionar la categoria", None))
        self.checkBox_4.setText(_translate("Form", "CheckBox", None))
        self.label_3.setText(_translate("Form", "Información del libro", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Form = QtGui.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

