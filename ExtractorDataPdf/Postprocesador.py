from spellchecker import SpellChecker

class Postprocesador:
    def __init__(self, idioma='es'):
        # Crea una instancia del corrector ortográfico al crear un objeto Postprocesador
        self.spell = SpellChecker(language=idioma)
    
    @staticmethod
    def dividir_texto_en_palabras(texto):
        # Divide el texto en palabras
        palabras = texto.split()
        return palabras
    
    
    
    def corregir_ortografia(self, texto):
        spell = SpellChecker(language='es')
        palabras = texto.split()
        
        texto_corregido = []
        for palabra in palabras:
            if palabra.isupper():  # Si la palabra está en mayúsculas, se deja intacta
                texto_corregido.append(palabra)
            else:
                palabra_corregida = palabra  # Asume la palabra original por defecto
                if palabra.lower() in spell.unknown([palabra.lower()]) or r"\b[A-Z]{4}[A-Za-z0-9]{14}\b":
                    palabra_corregida = spell.correction(palabra.lower())
                    # Asegúrate de que palabra_corregida sea una cadena
                    if palabra_corregida is None:
                        palabra_corregida = ""  # O maneja de otra manera, pero asegúrate de que no sea None
                # Aplica capitalización si es necesario
                palabra_corregida = palabra_corregida.capitalize() if palabra[0].isupper() else palabra_corregida
                texto_corregido.append(palabra_corregida)
        
        texto_corregido = ' '.join(texto_corregido)
        return texto_corregido
