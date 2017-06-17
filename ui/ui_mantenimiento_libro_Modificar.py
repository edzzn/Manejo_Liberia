# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MantenimientoLibrosModificar.ui'
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
        Form.resize(552, 569)
        self.pushButton = QtGui.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(60, 30, 161, 31))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.label_7 = QtGui.QLabel(Form)
        self.label_7.setGeometry(QtCore.QRect(70, 190, 261, 41))
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.buttonBox = QtGui.QDialogButtonBox(Form)
        self.buttonBox.setGeometry(QtCore.QRect(190, 510, 176, 27))
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.widget = QtGui.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(60, 90, 411, 71))
        self.widget.setObjectName(_fromUtf8("widget"))
        self.gridLayout = QtGui.QGridLayout(self.widget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label = QtGui.QLabel(self.widget)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.textBrowser = QtGui.QTextBrowser(self.widget)
        self.textBrowser.setObjectName(_fromUtf8("textBrowser"))
        self.gridLayout.addWidget(self.textBrowser, 1, 0, 1, 1)
        self.widget1 = QtGui.QWidget(Form)
        self.widget1.setGeometry(QtCore.QRect(70, 250, 431, 221))
        self.widget1.setObjectName(_fromUtf8("widget1"))
        self.formLayout = QtGui.QFormLayout(self.widget1)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.label_2 = QtGui.QLabel(self.widget1)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.label_2)
        self.lineEdit = QtGui.QLineEdit(self.widget1)
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.lineEdit)
        self.label_3 = QtGui.QLabel(self.widget1)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_3)
        self.lineEdit_2 = QtGui.QLineEdit(self.widget1)
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.lineEdit_2)
        self.label_4 = QtGui.QLabel(self.widget1)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.LabelRole, self.label_4)
        self.lineEdit_3 = QtGui.QLineEdit(self.widget1)
        self.lineEdit_3.setObjectName(_fromUtf8("lineEdit_3"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.FieldRole, self.lineEdit_3)
        self.label_5 = QtGui.QLabel(self.widget1)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.formLayout.setWidget(3, QtGui.QFormLayout.LabelRole, self.label_5)
        self.lineEdit_4 = QtGui.QLineEdit(self.widget1)
        self.lineEdit_4.setObjectName(_fromUtf8("lineEdit_4"))
        self.formLayout.setWidget(3, QtGui.QFormLayout.FieldRole, self.lineEdit_4)
        self.label_6 = QtGui.QLabel(self.widget1)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.formLayout.setWidget(4, QtGui.QFormLayout.LabelRole, self.label_6)
        self.lineEdit_5 = QtGui.QLineEdit(self.widget1)
        self.lineEdit_5.setObjectName(_fromUtf8("lineEdit_5"))
        self.formLayout.setWidget(4, QtGui.QFormLayout.FieldRole, self.lineEdit_5)
        self.label_8 = QtGui.QLabel(self.widget1)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.formLayout.setWidget(5, QtGui.QFormLayout.LabelRole, self.label_8)
        self.lineEdit_6 = QtGui.QLineEdit(self.widget1)
        self.lineEdit_6.setObjectName(_fromUtf8("lineEdit_6"))
        self.formLayout.setWidget(5, QtGui.QFormLayout.FieldRole, self.lineEdit_6)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.pushButton.setText(_translate("Form", "Buscar Libro", None))
        self.label_7.setText(_translate("Form", "Introduzca los siguientes campos", None))
        self.label.setText(_translate("Form", "Libro seleccionado", None))
        self.label_2.setText(_translate("Form", "ISBN", None))
        self.label_3.setText(_translate("Form", "Nº páginas", None))
        self.label_4.setText(_translate("Form", "Idioma", None))
        self.label_5.setText(_translate("Form", "Autor", None))
        self.label_6.setText(_translate("Form", "Editorial", None))
        self.label_8.setText(_translate("Form", "Categoria", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Form = QtGui.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

