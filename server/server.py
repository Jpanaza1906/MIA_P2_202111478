import os
from flask import Flask, jsonify, request, send_file, make_response
from main import analizarComando, limpiarConsola
app = Flask(__name__)

#Login route
@app.route('/login', methods=['POST'])
def login():
    body = request.get_json()
    try:
        if 'command' in body:
            limpiarConsola()
            command = body['command']
            print(command)
            cs = analizarComando(command)
            cadenaConsola = ""
            for linea in cs:
                cadenaConsola += linea
            
            return jsonify({"response": cadenaConsola}), 200
    except Exception as e: 
        return jsonify({"response": e}), 500

#Command route
@app.route('/command', methods=['POST'])
def command():
    body = request.get_json()
    try:
        if 'command' in body:
            limpiarConsola()
            command = body['command']
            print(command)
            lines = command.split('\n')
            for line in lines:       
                if line == "":
                    continue
                cs = analizarComando(line)                         
                cadenaConsola = ""
                for linea in cs:
                    cadenaConsola += linea
                    
            return jsonify({"response": cadenaConsola}), 200
    except: 
        return jsonify({"msg": "Error"}), 500

#Reporte route
@app.route('/reporte/<nombre_reporte>', methods=['GET'])
def reporte(nombre_reporte):
    try:
        #obtengo la carpeta padre donde se encuentra el reporte
        ruta_reporte = os.path.join(os.path.dirname(os.path.abspath(__file__)), "Reportes", nombre_reporte)
        # Crear una respuesta para enviar la imagen
        # Verificar si el archivo existe
        if os.path.exists(ruta_reporte):
            # Enviar el archivo como descarga
            return send_file(ruta_reporte, as_attachment=True)
        else:
            return jsonify({"msg": "El archivo no existe", "error": ""}), 404
    except Exception as e: 
        return jsonify({"msg": "Error al descargar la imagen", "error": str(e)}), 500
    
    
if __name__ == '__main__':
    app.run(debug=True)