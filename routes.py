from flask import Flask, request, redirect, url_for, render_template, jsonify, current_app
from config import get_db_connection
from datetime import datetime
import informe
app = Flask(__name__)

@app.route('/')
def index():
    conn = get_db_connection()
    cursor = conn.cursor()
        
    cursor.execute("SELECT Id, Matricula, Agencia, Destino, Observación FROM Pendientes WHERE Pendiente = True ORDER BY Agencia")
    trucks = cursor.fetchall()
        
    cursor.execute("SELECT Id, Matricula, Agencia, Destino, Observación FROM Pendientes WHERE Preparado = True ORDER BY Agencia")
    Preparados = cursor.fetchall()
    
    cursor.execute("SELECT Id, Matricula, Agencia, Destino, Observación FROM Pendientes WHERE Llegado = True ORDER BY Agencia")
    Llegados = cursor.fetchall()
    
    cursor.execute("SELECT Id, Matricula, Agencia, Destino, Observación FROM Pendientes WHERE Salido = True ORDER BY Agencia")
    Salidos = cursor.fetchall()
    cursor.close()
    conn.close()
    return render_template('index.html', trucks=trucks,Preparados=Preparados, Llegados=Llegados, Salidos=Salidos )
    
@app.route('/add_trucks', methods=['POST'])
def add_trucks():
    truck_numbers = request.form.getlist('truck_number[]')
    agencias = request.form.getlist('agencia[]')
    destinos = request.form.getlist('destino[]')
    observaciones = request.form.getlist('observacion[]')
    conn = get_db_connection()
    cursor = conn.cursor()
    # Procesar cada camión y agregarlo a la base de datos o lo que sea necesario
    for truck_number, agencia, destino, observacion in zip(truck_numbers, agencias, destinos, observaciones):
    
        cursor.execute(
            "INSERT INTO Pendientes (Matricula, Agencia, Destino, Observación) VALUES (?, ?, ?, ?)",
            (truck_number, agencia, destino, observacion)
        )
    conn.commit()
    cursor.close()
    conn.close()

    return redirect(url_for('index'))

@app.route('/add_truck', methods=['POST'])
def add_truck():
    truck_number = request.form['truck_number']
    agencia = request.form['agencia']
    observacion = request.form['observacion']
    destino = request.form['destino']

    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO Pendientes (Matricula, Agencia, Destino, Observación) VALUES (?, ?, ?, ?)",
        (truck_number, agencia, destino, observacion)
    )
    conn.commit()
    cursor.close()
    conn.close()

    return redirect(url_for('index'))

@app.route('/add')
def add():
    return render_template('add.html')

@app.route('/guardar-cambios', methods=['POST'])
def guardar_cambios():
    Id = request.form['id']
    matricula = request.form['matricula']
    agencia = request.form['agencia']
    destino = request.form['destino']
    observacion = request.form['observacion']
    
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        "UPDATE Pendientes SET Matricula = ?, Agencia = ?, Destino = ?, Observación = ? WHERE Id = ?",
        (matricula, agencia, destino, observacion, Id)
    )
    conn.commit()
    cursor.close()
    conn.close()
    
    return redirect(url_for('index'))
@app.route('/preparar', methods=['POST'])
def preparar_camion():
    # Obtener la matrícula desde el cuerpo de la solicitud (JSON)
    data = request.get_json()
    Id = data['Id']
    
    # Establecer la conexión a la base de datos
    conn = get_db_connection()
    cursor = conn.cursor()
    
    # Ejecutar la consulta de actualización
    cursor.execute(
        "UPDATE Pendientes SET Preparado = TRUE, Pendiente = FALSE WHERE Id = ?",
        (Id,)
    )
    
    # Confirmar los cambios y cerrar la conexión
    conn.commit()
    cursor.close()
    conn.close()
    
    # Enviar una respuesta exitosa (opcional)
    return jsonify({'status': 'success', 'message': f'Camión {Id} marcado como preparado.'}), 200
@app.route('/comprobar_estado')
def comprobar_estado():
    with app.app_context():
        print(f"Ejecutando comprobar_estado a las {datetime.now()}")
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT Matricula_Camion_R FROM Llegados WHERE FECH_S <> Date() ")
        Llegados = cursor.fetchall()
        print (Llegados)
        cursor.execute("SELECT Matricula_Camion_R FROM Llegados WHERE FECH_S = Date()")
        Salidos = cursor.fetchall()
        print (Salidos)
        for truck in Llegados:
            cursor.execute("UPDATE Pendientes SET Preparado = FALSE, Llegado = True WHERE Matricula = ?",
            (truck.Matricula_Camion_R))
        for truck in Salidos:
            cursor.execute("UPDATE Pendientes SET Llegado = FALSE, Preparado = FALSE, Salido = True WHERE Matricula = ?",
            (truck.Matricula_Camion_R))
        conn.commit()
        cursor.close()
        conn.close()
        return redirect(url_for('index'))
    
@app.route('/resetear-tabla', methods=['GET'])
def resetear_tabla():
    informe.main()
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM Pendientes")  # Vacía la tabla
        conn.commit()
        cursor.close()
        conn.close()
        return redirect(url_for('index'))  # Vuelve a la página principal
    except Exception as e:
        print(f"Error al resetear la tabla: {e}")
        return "Ocurrió un error al intentar resetear la tabla.", 500

"""scheduler = BackgroundScheduler()
scheduler.add_job(func=comprobar_estado, trigger="interval", minutes=1)
scheduler.start()
print(f"Tareas activas: {scheduler.get_jobs()}")"""

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)