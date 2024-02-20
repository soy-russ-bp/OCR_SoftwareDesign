import fitz  # PyMuPDF
import pytesseract
from PIL import Image
import io
from Preprocesador import Preprocesador
from Postprocesador import Postprocesador

class Ocr:
    def __init__(self):
        self.postprocesador = Postprocesador()

    
    def imagen_a_texto(self, imagen):
        # Usa OCR para convertir la imagen a texto
        texto = pytesseract.image_to_string(imagen, lang='spa')
        texto = self.postprocesador.corregir_ortografia(texto)  # Corrige la ortografía del texto extraído
        return texto

    def pdf_a_texto(self, ruta_pdf):
        doc = fitz.open(ruta_pdf)  # Abre el PDF
        texto_total = ""  # Aquí se almacenará el texto extraído

        for pagina in doc:  # Itera sobre las páginas del PDF
            imagenes = pagina.get_images(full=True)  # Regresa una lista de tuplas con la referencia a cada imagen y su información

            for ref_imagen in imagenes:  # Itera sobre las imágenes de la página
                # Extrae la imagen del PDF
                base_imagen = doc.extract_image(ref_imagen[0])  # ref_imagen[0] es la referencia a la imagen
                imagen_bytes = base_imagen["image"]  # Extrae los bytes de la imagen
                # Convierte bytes a un objeto de imagen de PIL
                imagen = Image.open(io.BytesIO(imagen_bytes))
                
                preprocesador = Preprocesador(imagen)
                
                #imagen = preprocesador.mejorar_nitidez()  # Mejora la nitidez de la imagen
                imagen_np = preprocesador.convertir_a_opencv()  # Convierte a formato OpenCV
                #Preprocesador.visualizar_imagen(imagen_np)
                imagen_np = preprocesador.aumentar_resolucion(3.0)  # Aumenta la resolución de la imagen
                imagen_np = preprocesador.convertir_a_escala_de_gris()  # Convierte a escala de grises
                #Preprocesador.visualizar_imagen(imagen_np)
                
                imagen_np = preprocesador.eliminar_ruido(3)
                
                #imagen_np = preprocesador.binarizar_imagen(2)
                #Preprocesador.visualizar_imagen(imagen_np)
                
                imagen_np = preprocesador.ajustar_brillo_contraste(brillo=30, contraste=1.3)

    
                texto = self.imagen_a_texto(imagen_np)  # Convierte la imagen a texto con OCR
                texto_total += texto + "\n"  # Agrega el texto extraído al texto total

        return texto_total

