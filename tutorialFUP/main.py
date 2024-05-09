from flask import Flask
from flask import jsonify
from flask import request
from flask_cors import CORS
import json
from waitress import serve
from Controladores.ControladorEstudiante import ControladorEstudiante

# Creamos una instancia de la aplicación Flask
app = Flask(__name__)

# Habilitamos CORS para permitir solicitudes desde diferentes dominios
cors = CORS(app)

# Creamos una instancia del ControladorEstudiante para manejar las operaciones relacionadas con estudiantes
miControladorEstudiante = ControladorEstudiante()


@app.route("/", methods=['GET'])
def test():
    json = {}
    json["message"] = "Server running ..."
    return jsonify(json)


@app.route("/estudiantes", methods=['GET'])
def getEstudiantes():
    # Llama al método 'index' del ControladorEstudiante para obtener todos los estudiantes
    json = miControladorEstudiante.index()

    # Convierte el resultado obtenido en formato JSON y lo retorna como respuesta de la solicitud
    return jsonify(json)


@app.route("/estudiantes", methods=['POST'])
def crearEstudiante():
    # Obtiene los datos enviados en el cuerpo de la solicitud en formato JSON
    data = request.get_json()

    # Llama la funcion 'create' del ControladorEstudiante para crear un nuevo estudiante
    json = miControladorEstudiante.create(data)

    # Convierte el resultado obtenido en formato JSON y lo retorna como respuesta de la solicitud
    return jsonify(json)


@app.route("/estudiantes/<string:id>", methods=['GET'])
def getEstudiante(id):
    # Obtiene el ID del estudiante desde la URL de la solicitud
    # El ID se pasará como parámetro en la URL y se almacenará en la variable 'id'

    # Llama la funcion 'show' del ControladorEstudiante para obtener los detalles del estudiante con el ID especificado
    json = miControladorEstudiante.show(id)

    # Convierte el resultado obtenido en formato JSON y lo retorna como respuesta de la solicitud
    return jsonify(json)


@app.route("/estudiantes/<string:id>", methods=['PUT'])
def modificarEstudiante(id):
    # Obtiene el ID del estudiante desde la URL de la solicitud
    # El ID se pasará como parámetro en la URL y se almacenará en la variable 'id'

    # Obtiene los datos enviados en el cuerpo de la solicitud en formato JSON
    data = request.get_json()

    # Llama la funcion 'update' del ControladorEstudiante para modificar los datos del estudiante con el ID especificado
    json = miControladorEstudiante.update(id, data)

    # Convierte el resultado obtenido en formato JSON y lo retorna como respuesta de la solicitud
    return jsonify(json)


@app.route("/estudiantes/<string:id>", methods=['DELETE'])
def eliminarEstudiante(id):
    # Obtiene el ID del estudiante desde la URL de la solicitud
    # El ID se pasará como parámetro en la URL y se almacenará en la variable 'id'

    # Llama al método 'delete' del ControladorEstudiante para eliminar el estudiante con el ID especificado
    json = miControladorEstudiante.delete(id)

    # Convierte el resultado obtenido en formato JSON y lo retorna como respuesta de la solicitud
    return jsonify(json)


def loadFileConfig():
    with open('config.json') as f:
        data = json.load(f)
    return data


if __name__ == '__main__':
    dataConfig = loadFileConfig()
    print("Server running : " + "http://" + dataConfig["url-backend"] + ":" + str(dataConfig["port"]))
    serve(app, host=dataConfig["url-backend"], port=dataConfig["port"])
