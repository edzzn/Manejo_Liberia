from PyQt4 import QtGui
import sys
from ui_mant_reservas import MenuMaintReservas
from ui_mant_libros import MenuLibros
from ui_mant_estudiantes import MenuEstudiantes
from ui_mant_categorias import MenuCategorias
from CoreData import saveD, loadD

# for test Only
import inspect

class MainWindow(QtGui.QMainWindow):
    """
        Main Window de la aplicación 
    """
    def __init__(self):
        super(MainWindow, self).__init__()

        self.create_actions()
        self.create_menus()
        self.create_toolBars()
        self.create_statusBar()
        # self.create_list_prestamos()

        # self.setWindowIcon(QtGui.QIcon('images/logo.png'))
        self.setWindowTitle('Gestión Biblioteca')
        self.setGeometry(300, 300, 450, 300)

    # Acciones
    def open_reserva_window(self):
        print(inspect.stack()[0][3])

    def open_mantenimiento_libro_window(self):
        self.main_libros_view = MenuLibros()
        self.main_libros_view.show()
        print(inspect.stack()[0][3])

    def open_mantenimiento_estudiante_window(self):
        self.main_estudiantes_view = MenuEstudiantes()
        self.main_estudiantes_view.show()
        print(inspect.stack()[0][3])

    def open_mantenimiento_categoria_window(self):
        self.main_categorias_view = MenuCategorias()
        self.main_categorias_view.show()
        print(inspect.stack()[0][3])

    def open_mantenimiento_reserva_window(self):
        self.maint_reservas_view = MenuMaintReservas()
        self.maint_reservas_view.show()
        print(inspect.stack()[0][3])

    def about(self):
        QtGui.QMessageBox.about(self, "Acerca de **** - Sistema de Gestion de Prestamos de Libros",
                "<b>*****</b> es una aplicacion realizada por <b>----</b>."  )

    def create_actions(self):
        self.maintLibrosAct = QtGui.QAction(QtGui.QIcon('images/user-plus.png'),
                "&Mantenimiento Libros", self,
                                            # shortcut=QtGui.QKeySequence.New,
                                           statusTip="Mantenimiento Registro Libros",
                                            triggered=self.open_mantenimiento_libro_window)

        self.maintEstudiantesAct = QtGui.QAction(QtGui.QIcon('images/user-plus.png'),
                "&Mantenimiento Estudiantes", self,
                                            # shortcut=QtGui.QKeySequence.New,
                                           statusTip="Mantenimiento Registro Estudiantes",
                                            triggered=self.open_mantenimiento_estudiante_window)

        self.maintCategoriasAct = QtGui.QAction(QtGui.QIcon('images/user-plus.png'),
                "&Mantenimiento Categorias", self,
                                            # shortcut=QtGui.QKeySequence.New,
                                            statusTip="Mantenimiento Registro Categorias",
                                            triggered=self.open_mantenimiento_categoria_window)

        self.maintReservasAct = QtGui.QAction(QtGui.QIcon('images/user-plus.png'),
                "&Mantenimiento Reservas", self,
                                            # shortcut=QtGui.QKeySequence.New,
                                           statusTip="Mantenimiento Registro Reservas",
                                            triggered=self.open_mantenimiento_reserva_window)

        # self.maintCategoriasAct = QtGui.QAction(QtGui.QIcon('images/user-plus.png'),
        #         "&Mantenimiento Libros", self,
        #                                     # shortcut=QtGui.QKeySequence.New,
        #                                    statusTip="Mantenimiento Registro Reservas",
        #                                     triggered=self.open_mantenimiento_categoria_window)

        self.aboutAct = QtGui.QAction(QtGui.QIcon('images/info.png'),
                                      "Acerca de", self,
                                      statusTip = "Acerca de  ****",
                                      triggered= self.about)

    def create_menus(self):
        self.fileMenu = self.menuBar().addMenu("&Archivo")

        self.maintenanceMenu = self.menuBar().addMenu("&Mantenimiento")
        self.maintenanceMenu.addAction(self.maintLibrosAct)
        self.maintenanceMenu.addAction(self.maintEstudiantesAct)
        self.maintenanceMenu.addAction(self.maintCategoriasAct)
        self.maintenanceMenu.addAction(self.maintReservasAct)

        self.helpMenu = self.menuBar().addMenu("&Ayuda")
        self.helpMenu.addAction(self.aboutAct)

    def create_statusBar(self):
        self.statusBar().showMessage("Ready")

    def create_toolBars(self):
        self.fileToolBar = self.addToolBar("Archivo")
        self.fileToolBar.addAction(self.maintLibrosAct)
        self.fileToolBar.addAction(self.maintEstudiantesAct)
        self.fileToolBar.addAction(self.maintCategoriasAct)
        self.fileToolBar.addAction(self.maintReservasAct)



if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec_())
