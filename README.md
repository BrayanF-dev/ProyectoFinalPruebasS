# Proyecto Final

Este proyecto es sobre lo aprendido en el segundo corte, donde se realizaran pruebas automatizadas utilizando Python y Selenium WebDriver sobre el sitio [demoqa.com](https://demoqa.com/).

## Tecnologías utilizadas
- Python 3.13
- Selenium
- unittest
- HtmlTestRunner
- VS Code

## 📂 Estructura del proyecto

ProyectoFinalPruebasS/
    ProyectoFinal.py        # Codigo para las preubas automatizadas
    README.md               # Documento donde explicamos todo el proceso del proyecto
    ImagenPrueba.jpg        # Imagen de referencia (un gatito jaja)
    argv.json               # Archivo de configuración usado por el proyecto


## ✅ Casos de prueba automatizados

1. **Formulario**
   - Llena campos como nombre, apellido, email, género, etc.
   - Envía el formulario y valida que los datos aparezcan correctamente

2. **Subida de archivo**
   - Carga una imagen del sistema (ImagenPrueba.jpg) en el sitio y comprueba que se sube correctamente.

3. **Descarga de archivo**
   - Descarga un archivo desde la web y verifica que este en la carpeta local de descargas.

4. **Manejo de alertas**
   - Alertas simples, de confirmación y prompts.

## ¿Cómo ejecutar el proyecto?

1. Asegurarnos de tener Python y las extensiones necesarias instaladas en VS Code 

2. Instala las dependencias del proyecto:
    pip install -r requirements.txt

3. Al ejecutar abrimos el proyedto (ProyectoFinal.py) y lo corremos (RUN)

4. El resultado de las pruebas aparecerá en la terminal de abajo y se generará un reporte HTML dentro de la carpeta reportes_html.

## Requisitos del sistema

- Python 3.13
- Google Chrome
- ChromeDriver

## 🎥 Video explicativo.

Video de explicaion de pruebas con Selenium, ejecucion de las mismas y qué hace cada parte del código:

🔗 [Ver video en Google Drive](https://drive.google.com/file/d/1UWqK1LJW-3ew8bP6_HNX3NMfGNwieWdM/view?usp=sharing)


## Lo que aprendí con este proyecto

Este proyecto aprendí y entendí un poco mas cómo funciona la automatización de pruebas con Python.  
Pude practicar con herramientas como:

- Python, que fue el lenguaje principal que usé para escribir todo el código.
- Selenium, que me permitió controlar un navegador automáticamente, para que de esta manera autoamticamente se realiara la preuba 
- unittest, que me ayudó a organizar las pruebas para que corran de forma ordenada.
- HtmlTestRunner, que me generó un reporte en HTML con los resultados de las pruebas, donde puedeo ver si fueron positivas o negativas
 


