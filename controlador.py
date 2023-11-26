#Juan Sebastian Daza Betancourt - Sebastian Alzate Sierra
#No nos copiló en jupyter :(
from modelo import BaseDato, Modelo
from vistas import Vistaingreso, vistappal
import sys
from PyQt5.QtWidgets import QApplication, QMessageBox

class Coordinador:
    def __init__(self, vistas, modelo):
        self.__mivista = vistas[0]
        self.__mimodelo = modelo
        self.__mivista2 = vistas[1]
        self.__mimodelo2 = Modelo()

    def validarUsuario(self, l, p):
        return self.__mimodelo.validarusuario(l, p)

    def img_conextion(self):
        self.__mimodelo2.picture_creator()

    def seleccionar_carpeta(self):
        self.__mimodelo2.seleccionar_carpeta()

    def procesar_slider(self):
        self.__mivista2.procesarslider()

    def obtener_carpeta(self):
        return self.__mimodelo2.carpeta
    
    def mostrar_info_dicom(self, info):
        self.__mivista2.mostrar_info_dicom(info)
        
    def mostrar_primera_vista(self):
        self.__mivista.show()

def main():
    app = QApplication(sys.argv)
    mivista = Vistaingreso()
    mimodelo = BaseDato()
    mivista2 = vistappal()
    mimodelo2 = Modelo()
    micoordinador = Coordinador([mivista, mivista2], mimodelo)
    mivista.setControlador(micoordinador)
    mivista2.addControler(micoordinador)
    mivista.show()

    sys.exit(app.exec_())

if __name__ == "__main__":
    main()