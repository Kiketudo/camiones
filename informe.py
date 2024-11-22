import pyodbc
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib import colors
from datetime import datetime
import os
def fetch_data_from_db():
    # Configuración de conexión
    conn = pyodbc.connect(
        r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};'
        r'DBQ=./BaseDatosBascula.accdb;'
    )
    cursor = conn.cursor()
    
    # Consulta SQL para obtener los datos
    query = "SELECT  Matricula, Agencia, Destino, Observación FROM Pendientes WHERE Llegado = True OR Salido = True ORDER BY Agencia" 
    cursor.execute(query)
    data = cursor.fetchall()
    cursor.close()
    conn.close()
    
    return data

def generate_pdf(data, filename):
    c = canvas.Canvas(filename, pagesize=letter)
    width, height = letter
    
    # Título del informe
    c.setFont("Helvetica-Bold", 18)
    c.setFillColor(colors.darkblue)
    c.drawString(30, height - 40, "Informe de Camiones Llegados")
    
    # Fecha actual
    c.setFont("Helvetica", 10)
    current_date = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    c.drawString(30, height - 60, f"Fecha de generación: {current_date}")
    
    # Línea separadora
    c.setStrokeColor(colors.darkblue)
    c.setLineWidth(1)
    c.line(30, height - 70, width - 30, height - 70)
    
    # Títulos de las columnas
    c.setFont("Helvetica-Bold", 12)
    c.setFillColor(colors.black)
    c.drawString(30, height - 100, "Truck Number")
    c.drawString(150, height - 100, "Agencia")
    c.drawString(250, height - 100, "Destino")
    c.drawString(350, height - 100, "Observación")
    
    # Ajustar posición para las filas
    y_position = height - 120
    line_height = 20  # Espacio entre filas
    
    # Llenar el PDF con los datos
    c.setFont("Helvetica", 10)
    for row in data:
        c.drawString(30, y_position, str(row[0]))  # Número de camión
        c.drawString(150, y_position, str(row[1]))  # Agencia
        c.drawString(250, y_position, str(row[2]))  # Destino
        c.drawString(350, y_position, str(row[3]))  # Observación
        y_position -= line_height
    
    # Línea final
    c.setStrokeColor(colors.darkblue)
    c.setLineWidth(1)
    c.line(30, y_position - 5, width - 30, y_position - 5)
    
    # Guardar el PDF
    c.save()

def main():
    # Obtener datos de la base de datos
    data = fetch_data_from_db()
    
    timestamp = datetime.now().strftime("%Y-%m-%d")
    
    # Definir la ruta del archivo PDF con la fecha
    output_folder = './informes'
    
    # Crear la carpeta 'informes' si no existe
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    # Nombre del archivo con timestamp
    pdf_filename = os.path.join(output_folder, f'Informe_camiones_{timestamp}.pdf')

    # Generar el archivo PDF
    generate_pdf(data, pdf_filename)
    print(f"Informe generado correctamente en {pdf_filename}")

