from Ocr import Ocr 
from Postprocesador import Postprocesador
from Extractor_datos import Extractor_datos



class Main:
    ocr = Ocr()
    postprocesador = Postprocesador()
    extractor = Extractor_datos()
    
    
    ruta_pdf = '/Insertar/Ruta/DelArchivoDeseado/HOLA4.pdf' 
    texto_extraido = ocr.pdf_a_texto(ruta_pdf)
    
    print(texto_extraido)
    file = open('texto_extraido.txt', 'w').write(texto_extraido)
    
    personas = extractor.obtener_datos_curp(texto_extraido)
    

    for persona in personas:
        file = open('datos_extraidos.txt', 'a').write(str(persona)+"\n")
        print(persona)
    
    
    
    