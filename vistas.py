from PyQt5.QtWidgets import QMainWindow, QDialog, QApplication, QMessageBox, QWidget, QPushButton, QVBoxLayout, QFileDialog
import pydicom
from PyQt5.QtGui import QPixmap
from PyQt5.uic import loadUi
import os

class Vistaingreso(QDialog):
    def __init__(self):
        super().__init__()
        loadUi('inicio.ui', self)
        self.setup()

    def setup(self):
        self.buttonBox.accepted.connect(self.opcion_aceptar)
        self.buttonBox.rejected.connect(self.opcion_rechazar)

    def opcion_aceptar(self):
        login = self.lineuser.text()
        password = self.linecontra.text()

        if self.__micontrolador.validarUsuario(login, password):
            QMessageBox.information(self, 'Login Successful', 'Welcome, {}'.format(login))
            self.accept()

            ventana2 = vistappal()
            ventana2.addControler(self.__micontrolador)
            self.hide()
            ventana2.show()

            self.__micontrolador.seleccionar_carpeta()
            self.__micontrolador.img_conextion()

            index = 0  
            info_dicom = self.__micontrolador.mostrar_info_dicom(index)
            ventana2.mostrar_info_dicom(info_dicom)

        else:
            QMessageBox.warning(self, 'Login Failed', 'Usuario o contraseña invalidos. Vuelva a intentarlo')
            self.lineuser.clear()
            self.linecontra.clear()
            self.lineuser.setFocus()
            self.show()
 
    def opcion_rechazar(self):
        self.lineuser.setText("")
        self.linecontra.setText("")

    def setControlador(self, c):
        self.__micontrolador = c;

class vistappal(QWidget):
    def __init__(self):
        super().__init__()
        loadUi('wid.ui', self)
        self.setup()

    def setup(self):
        self.carga.clicked.connect(self.cargar_carpeta)
        self.sld.valueChanged.connect(self.cargar)
        self.carpeta = ""
        self.lista = []
        self.Cerrar_sesion.clicked.connect(self.cerrar_sesion)  

    def mostrar_info_dicom(self, info):
        self.tx.setText(info)

    def addControler(self, c):
        self.__mi_coordinador = c

    def cargar_carpeta(self):
        self.__mi_coordinador.seleccionar_carpeta()
        self.carpeta = self.__mi_coordinador.obtener_carpeta()
        self.lista = os.listdir(self.carpeta)
        for i in self.lista:
            self.sld.addItem(i)

    def cargar(self):
        index = self.sld.value()  
        if index >= 0 and index < len(self.lista):
            imagen = self.lista[index]
            self.__mi_coordinador.img_conextion()
            pixmap = QPixmap("temp_image.png")
            self.img.setPixmap(pixmap)
            os.remove('temp_image.png')

    def cerrar_sesion(self):
        self.hide()
        self.__mi_coordinador.mostrar_primera_vista()
