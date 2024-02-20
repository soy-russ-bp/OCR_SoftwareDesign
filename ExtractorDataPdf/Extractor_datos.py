import re

class Persona:
    def __init__(self, curp, fecha_nacimiento, sexo, estado, nombre):
        self.curp = curp
        self.fecha_nacimiento = fecha_nacimiento
        self.sexo = sexo
        self.estado = estado
        self.nombre = nombre

    def __str__(self):
        return f"Fecha de nacimiento: {self.fecha_nacimiento}\nSexo: {self.sexo}\nEstado: {self.estado}\nNombre: {self.nombre}\n"

class Extractor_datos:
    def __init__(self):
        self.estados = {
            "AS": "Aguascalientes",
            "BC": "Baja California",
            "BS": "Baja California Sur",
            "CC": "Campeche",
            "CS": "Chiapas",
            "CH": "Chihuahua",
            "CL": "Coahuila",
            "CM": "Colima",
            "DF": "Ciudad de México",
            "DG": "Durango",
            "GT": "Guanajuato",
            "GR": "Guerrero",
            "HG": "Hidalgo",
            "JC": "Jalisco",
            "MC": "México",
            "MN": "Michoacán",
            "MS": "Morelos",
            "NT": "Nayarit",
            "NL": "Nuevo León",
            "OC": "Oaxaca",
            "PL": "Puebla",
            "QT": "Querétaro",
            "QR": "Quintana Roo",
            "SP": "San Luis Potosí",
            "SL": "Sinaloa",
            "SR": "Sonora",
            "TC": "Tabasco",
            "TS": "Tamaulipas",
            "TL": "Tlaxcala",
            "VZ": "Veracruz",
            "YN": "Yucatán",
            "ZS": "Zacatecas"
        }

    @staticmethod
    def extraer_nombre(texto, fin_curp):
        # Se asume que el nombre sigue inmediatamente después de la CURP
        patron_nombre =  r"Nombre\s+([A-Z\s]+)\s"

        coincidencias = list(re.finditer(patron_nombre, texto, re.IGNORECASE))
        for match in coincidencias:
            if match.start() > fin_curp:
                return match.group(1).strip()
        return "Nombre no encontrado"

    def obtener_estado(self, clave_estado):
        return self.estados.get(clave_estado, "Estado no encontrado")

    @staticmethod
    def obtener_sexo(clave_sexo):
        return "Hombre" if clave_sexo == "H" else "Mujer"

    def obtener_datos_curp(self, texto):
        regex_curp = r"([A-Z]{4})([0-9]{2})([0-9]{2})([0-9]{2})([A-Z])([A-Z]{2})"
        matches_curp = re.finditer(regex_curp, texto)

        personas = []
        for match in matches_curp:
            curp_full = match.group(0)
            año = "20" + match.group(2) if int(match.group(2)) < 22 else "19" + match.group(2)
            fecha_nacimiento = f"{match.group(4)}/{match.group(3)}/{año}"
            sexo = self.obtener_sexo(match.group(5))
            estado = self.obtener_estado(match.group(6))
            nombre = self.extraer_nombre(texto, match.end())

            persona = Persona(curp_full, fecha_nacimiento, sexo, estado, nombre)
            personas.append(persona)

        return personas

