import cv2
import numpy as np
from PIL import Image, ImageFilter

class Preprocesador:
    def __init__(self, imagen):
        self.imagen = imagen

    def mejorar_nitidez(self):
        self.imagen = self.imagen.filter(ImageFilter.SHARPEN)
        return self.imagen
        
    def convertir_a_opencv(self):
        # Convierte un objeto PIL.Image en un formato que OpenCV pueda usar (arreglo de NumPy)
        imagen_np = np.array(self.imagen)  # Convertir PIL.Image a un arreglo de NumPy
        self.imagen = cv2.cvtColor(imagen_np, cv2.COLOR_RGB2BGR)  # Convertir RGB a BGR
        return self.imagen

    def convertir_a_escala_de_gris(self):
        self.imagen = cv2.cvtColor(self.imagen, cv2.COLOR_BGR2GRAY)  # Convertir a escala de grises
        return self.imagen
    
    def aumentar_resolucion(self, escala=2.0):
        ancho = int(self.imagen.shape[1] * escala)
        alto = int(self.imagen.shape[0] * escala)
        dimensiones = (ancho, alto)
        self.imagen = cv2.resize(self.imagen, dimensiones, interpolation=cv2.INTER_CUBIC)
        return self.imagen
        
    def binarizar_imagen(self, umbral=0):
        _, self.imagen = cv2.threshold(self.imagen, umbral, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
        return self.imagen

    def eliminar_ruido(self, kernel=5):
        self.imagen = cv2.medianBlur(self.imagen, kernel)
        return self.imagen

    def visualizar_imagen(imagen):
        cv2.imshow('Imagen Preprocesada', imagen)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    def ajustar_brillo_contraste(self, brillo=0, contraste=1.0):
        self.imagen = cv2.convertScaleAbs(self.imagen, alpha=contraste, beta=brillo)
        return self.imagen

