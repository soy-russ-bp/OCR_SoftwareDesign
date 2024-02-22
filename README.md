# OCR_SoftwareDesign

### Requerimientos funcionales

- **RF1. El sistema abre un pdf**

- **RF2. El sistema aplica un preprocesado a cada página del pdf escaneado para mejorar los resultados**

- **RF3. El sistema extrae el texto del pdf**

- **RF4. El sistema aplica un postprocesado para corregir ortografía y palabras clave del texto extraidos del pdf**

- **RF5. El sistema procesa los datos corregido del pdf y los clasifica en fecha de nacimiento, sexo, estado y Nombre**

- **RF6. El programa genera un archivo.txt**

- **RF7. El programa guarda los datos previamente clasificados en el archivo.txt**

## Requerimientos no funcionales

### Atributos de calidad
* **Portabilidad:** El sistema se puede ejecutar en todos los dispositivos que cuenten con Python3 y con las librerías correspondientes instaladas (pyteserract, pyspellchecker, numpy, etc. )
* **Mantenibilidad:** El sistema puede ser mantenible dado que cuenta con modularidad.


### Reestricciones

* **Eficacia:** El resultado puede no ser siempre el esperado en caso de tratar de procesar un archivo escaneado con muchas imperfecciones, o un archivo que no ha sido escaneado.

* **Rendimiento:**  Incluye restricciones sobre tiempos de respuesta (El tiempo del proceso puede resultar lento).

* **Usabilidad:** El sistema no cuenta con interfaz gráfica que permita ser comprendido y atractivo para un usuario que no sabe programar.

* **Seguridad:** El software no asegura que los datos no se puedan filtrar, en caso de haber datos guardados en los archivos.txt cualquier persona puede acceder a ellos.

* **Compatibilidad:** El sistema únicamente extrae adecuadamaente los datos de CURPs escaneadas

