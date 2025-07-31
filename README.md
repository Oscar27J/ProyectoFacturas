# 🧾 Proyecto: Extracción de Facturas PDF a Excel

Este proyecto automatiza la extracción de datos de facturas en formato PDF y los convierte en un archivo Excel organizado y listo para su análisis.

---

## 🚀 Funcionalidad

✅ Lee todos los archivos PDF de la carpeta `input/`.  
✅ Extrae texto de cada factura utilizando OCR (Reconocimiento Óptico de Caracteres).  
✅ Procesa los datos y los organiza en formato tabla.  
✅ Exporta los resultados a un archivo Excel dentro de la carpeta `output/`.

---

## 📁 Estructura del Proyecto

```
ProyectoFacturas/
│
├── input/
│   ├── factura_001.pdf
│   └── factura_002.pdf
│
├── output/
│   └── facturas_procesadas.xlsx
│
├── main.py
├── requirements.txt
└── README.md
```

---

## ⚙️ Requisitos

- Python 3.10 o superior
- Tesseract OCR instalado en el sistema (versión recomendada: 5.x)
- Sistema operativo: Windows (aunque puede adaptarse a Linux/Mac)

---

## 🛠 Instalación y uso

### 1. Clona o descarga este repositorio

```bash
git clone https://github.com/tuusuario/ProyectoFacturas.git
cd ProyectoFacturas
```

### 2. Crea y activa el entorno virtual

```bash
python -m venv venv
.\venv\Scripts\activate
```

### 3. Instala las dependencias

```bash
pip install -r requirements.txt
```

> Si no tienes Tesseract instalado, descárgalo desde:  
> 👉 https://github.com/tesseract-ocr/tesseract  
> Asegúrate de agregar la ruta de instalación a las variables del sistema y que incluya el archivo `spa.traineddata`.

### 4. Ejecuta el script

```bash
python main.py
```

---

## 🧪 Ejemplo de resultado

El script generará un archivo Excel llamado `facturas_procesadas.xlsx` con los datos extraídos, en formato limpio y estructurado para su posterior análisis o reporte.

---

## 📌 Notas

- Este proyecto está pensado para facturas escaneadas o digitales simples.
- Para documentos muy complejos, pueden necesitarse ajustes personalizados en el OCR o el parser.
- Puedes personalizar el script para adaptarse a otros idiomas o formatos de factura.

---

## 📄 Licencia

Este proyecto es de uso libre para fines educativos o profesionales. Si lo utilizas como base, agradecería que cites la fuente en tu portafolio. 🙌

---

## 🧑‍💻 Autor

Oscar Alegre  
Proyecto creado para mi portafolio de automatización con Python.  
Contacto: oscaralegre19@gmail.com