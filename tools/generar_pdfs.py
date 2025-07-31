from fpdf import FPDF
import os

os.makedirs("input", exist_ok=True)

facturas = [
    {
        "num": "001",
        "cliente": "Empresa A",
        "ruc": "20123456789",
        "direccion": "Av. Los Álamos 123 - Lima",
        "fecha": "01/07/2025",
        "productos": [
            {"cant": 2, "desc": "Monitor 24\" LG", "pu": 600.00},
            {"cant": 1, "desc": "Teclado mecánico", "pu": 250.00},
        ]
    },
    {
        "num": "002",
        "cliente": "Empresa B",
        "ruc": "20456789123",
        "direccion": "Jr. Amazonas 456 - Arequipa",
        "fecha": "02/07/2025",
        "productos": [
            {"cant": 3, "desc": "Laptop Lenovo", "pu": 1800.00},
            {"cant": 2, "desc": "Mouse inalámbrico", "pu": 90.00},
        ]
    }
]

for f in facturas:
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    pdf.cell(0, 10, f"Factura N° {f['num']}", ln=True)
    pdf.cell(0, 10, f"Cliente: {f['cliente']}", ln=True)
    pdf.cell(0, 10, f"RUC: {f['ruc']}", ln=True)
    pdf.cell(0, 10, f"Dirección: {f['direccion']}", ln=True)
    pdf.cell(0, 10, f"Fecha: {f['fecha']}", ln=True)
    pdf.ln(5)

    pdf.set_font("Arial", 'B', size=12)
    pdf.cell(30, 10, "Cantidad", 1)
    pdf.cell(80, 10, "Descripción", 1)
    pdf.cell(40, 10, "P. Unitario", 1)
    pdf.cell(40, 10, "Subtotal", 1, ln=True)
    pdf.set_font("Arial", size=12)

    total = 0
    for p in f["productos"]:
        subtotal = p["cant"] * p["pu"]
        total += subtotal
        pdf.cell(30, 10, str(p["cant"]), 1)
        pdf.cell(80, 10, p["desc"], 1)
        pdf.cell(40, 10, f"{p['pu']:.2f}", 1)
        pdf.cell(40, 10, f"{subtotal:.2f}", 1, ln=True)

    igv = total * 0.18
    total_final = total + igv

    pdf.ln(5)
    pdf.cell(0, 10, f"IGV (18%): {igv:.2f}", ln=True)
    pdf.cell(0, 10, f"Total a pagar: S/.{total_final:.2f}", ln=True)

    pdf.output(f"input/factura_{f['num']}.pdf")

print("✅ PDFs realistas generados en carpeta 'input/'.")
