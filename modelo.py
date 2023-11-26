from PyQt5.QtCore import QObject
from PyQt5.QtWidgets import QFileDialog
import pydicom
import matplotlib.pyplot as plt
import os

class BaseDato(QObject):
    def __init__(self):
        super().__init__()
        self.__login = "medicoAnalitico"
        self.__password = "bio12345"

    def validarusuario(self, l, p):
        return (self.__login == l) and (self.__password == p)

class Modelo(QObject):
    def __init__(self):
        super().__init__()
        self.lista = []
        self.carpeta = ""

    def metodoi(self, a):
        info_dicom = ""
        for elemento in self.data[a]:
            if elemento.tag.group == 0x0010:
                atributo_nombre = elemento.description()
                atributo_valor = str(elemento.value)
                info_dicom += f"{atributo_nombre}: {atributo_valor}\n"
        return info_dicom

    def seleccionar_carpeta(self):
        self.carpeta = QFileDialog.getExistingDirectory(None, "Seleccionar Carpeta")

    def picture_creator(self):
        for i in os.listdir(self.carpeta):
            file_path = os.path.join(self.carpeta, i)
            if os.path.isfile(file_path):
                ds = pydicom.dcmread(file_path)
                pixel_data = ds.pixel_array
                if len(pixel_data.shape) == 3:
                    slice_index = pixel_data.shape[0] // 2
                    selected_slice = pixel_data[slice_index, :, :]
                    plt.imshow(selected_slice, cmap=plt.cm.bone)
                else:
                    plt.imshow(pixel_data, cmap=plt.cm.bone)
                plt.axis('off')
                plt.savefig("temp_image.png")
