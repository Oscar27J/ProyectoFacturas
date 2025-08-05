import os
from pdf2image import convert_from_path
import pytesseract
import pandas as pd
import re

# Configuración de Tesseract
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
os.environ["TESSDATA_PREFIX"] = r"C:\Program Files\Tesseract-OCR\tessdata"

# Carpeta de entrada
input_folder = "input"
archivos_pdf = [f for f in os.listdir(input_folder) if f.endswith(".pdf")]

# Lista para guardar datos extraídos
datos_facturas = []

# Procesar cada PDF
for archivo in archivos_pdf:
    print(f"Procesando: {archivo}")
    ruta_pdf = os.path.join(input_folder, archivo)

    # Convertir PDF a imágenes
    paginas = convert_from_path(ruta_pdf, dpi=300)

    texto_total = ""
    for pagina in paginas:
        texto = pytesseract.image_to_string(pagina, lang='spa')
        texto_total += texto + "\n"

    num_factura = None
    cliente = None
    fecha = None
    ruc = None
    igv = None
    total = None

    for linea in texto_total.splitlines():
        if "Factura" in linea and not num_factura:
            num_factura = linea.strip()
        elif "Cliente" in linea:
            cliente = linea.split(":")[-1].strip()
        elif "Fecha" in linea:
            fecha = linea.split(":")[-1].strip()
        elif "RUC" in linea:
            ruc = linea.split(":")[-1].strip()
        elif "IGV" in linea:
            valor = linea.split(":")[-1].replace("S/","").strip()
            igv = re.sub(r"[^\d, \.]", "", valor).replace(",", ".")
        elif "Total" in linea:
            valor = linea.split(":")[-1].replace("S/.","").strip()
            total = re.sub(r"[^\d, \.]", "", valor).replace(",", ".")

    datos_facturas.append({
        "Archivo": archivo,
        "Número de Factura": num_factura,
        "Cliente": cliente,
        "Fecha": fecha,
        "RUC": ruc,
        "IGV": igv,
        "Total": total,
    })

# Crear Excel
df = pd.DataFrame(datos_facturas)
df.to_excel("output/facturas_resumen.xlsx", index=False)
print("✅ Datos exportados a 'facturas.xlsx'")