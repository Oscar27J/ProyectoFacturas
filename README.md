# 🧾 Proyecto: Extracción de datos de facturas en PDF con Python

Este script automatiza la lectura de archivos PDF que contienen facturas, extrae datos clave (como número de factura, cliente, fecha, RUC, IGV y total), y genera:

- Un archivo Excel con todos los datos (facturas_resumen.xlsx)

---

## 📂 Estructura del proyecto

```plaintext
Proyecto/
├── input/            # Coloca aquí tus archivos PDF de facturas
├── output/           # Se generarán el Excel
├── main.py           # Script principal
├── requirements.txt  # Dependencias
└── README.md         # Este archivo
```

---

## ⚙️ Requisitos

### 1. Python 3.10+  
[🔗 Descargar Python](https://www.python.org/downloads/)

Durante la instalación, asegúrate de marcar: ✅ *Add Python to PATH*

---

### 2. Tesseract OCR  
Este proyecto utiliza OCR para extraer texto de los PDF.

#### 🔽 Instala Tesseract:
- [🔗 Windows Installer oficial](https://github.com/tesseract-ocr/tesseract/wiki#windows)
  - Recomendado: Instala en *C:\Program Files\Tesseract-OCR\ *

#### 📂 Importante:
Después de instalar Tesseract, verifica que este archivo exista:

*C:\Program Files\Tesseract-OCR\tessdata\spa.traineddata*

Si no tienes *spa.traineddata*, descárgalo manualmente desde:

👉 [🔗 Descargar spa.traineddata](https://github.com/tesseract-ocr/tessdata/blob/main/spa.traineddata)

y colócalo en la carpeta:

*C:\Program Files\Tesseract-OCR\tessdata\ *

---

## 🧰 Instalación del proyecto

1. Clona este repositorio o descarga los archivos ZIP
2. Abre una terminal (CMD o PowerShell)
3. Ve a la carpeta del proyecto:

*cd ruta\del\proyecto*

4. Crea un entorno virtual (opcional pero recomendado)

python -m venv venv
venv\Scripts\activate

5. Instala las dependencias

*pip install -r requirements.txt*

---

## ▶️ Cómo usar

1. Coloca tus facturas PDF dentro de la carpeta /input
2. Corre el script:

*python main.py*

3. Al finalizar se generarán los siguientes archivos en /output:

facturas_resumen.xlsx → Datos limpios en formato Excel

---

## 📌 Ejemplo de salida en Excel

```plaintext
Archivo	Número de Factura	Cliente	Fecha	RUC	IGV	Total

factura1.pdf	F001-12345	Juan Pérez	01/08/2025	20123456789	21.30	135.00
factura2.pdf	F001-12346	ACME S.A.	02/08/2025	20456789123	34.00	221.00
```

---

## 💡 Notas adicionales

Asegúrate de que los PDFs sean legibles (no escaneos borrosos).

Si usas otro idioma, cambia el valor de *lang='spa'* en el código.

El script no requiere conexión a internet una vez que todo está instalado.



---

## 🤝 Autor

### Oscar Alegre
💼 Especialista en Automatización con Python.
📧 Contacto: (oscaralregre19@gmail.com)


---