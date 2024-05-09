from flask import Flask
from flask import jsonify
from flask import request
from flask_cors import CORS
import json
from waitress import serve
from Controladores.ControladorEstudiante import ControladorEstudiante
from Controladores.ControladorMateria import ControladorMateria
from Controladores.ControladorDepartamento import ControladorDepartamento
from Controladores.ControladorInscripcion import ControladorInscripcion

# Creamos una instancia de la aplicación Flask
app = Flask(__name__)

# Habilitamos CORS para permitir solicitudes desde diferentes dominios
cors = CORS(app)

# Creamos una instancia del ControladorEstudiante para manejar las operaciones relacionadas con estudiantes
miControladorEstudiante = ControladorEstudiante()
miControladorMateria = ControladorMateria()
miControladorDepartamento = ControladorDepartamento()
miControladorInscripcion = ControladorInscripcion()


@app.route("/", methods=['GET'])
def test():
    json = {}
    json["message"] = "Server running ..."
    return jsonify(json)


###########################################Estudiante##################################################################

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


#######################################################################################################################


#############################################Departamento##############################################################

@app.route("/departamentos", methods=['GET'])
def getDepartamentos():
    json = miControladorDepartamento.index()
    return jsonify(json)


@app.route("/departamentos/<string:id>", methods=['GET'])
def getDepartamento(id):
    json = miControladorDepartamento.show(id)
    return jsonify(json)


@app.route("/departamentos", methods=['POST'])
def crearDepartamento():
    data = request.get_json()
    json = miControladorDepartamento.create(data)
    return jsonify(json)


@app.route("/departamentos/<string:id>", methods=['PUT'])
def modificarDepartamento(id):
    data = request.get_json()
    json = miControladorDepartamento.update(id, data)
    return jsonify(json)


@app.route("/departamentos/<string:id>", methods=['DELETE'])
def eliminarDepartamento(id):
    json = miControladorDepartamento.delete(id)
    return jsonify(json)


#######################################################################################################################


#################################################Materia###############################################################

@app.route("/materias", methods=['GET'])
def getMaterias():
    json = miControladorMateria.index()
    return jsonify(json)


@app.route("/materias/<string:id>", methods=['GET'])
def getMateria(id):
    json = miControladorMateria.show(id)
    return jsonify(json)


@app.route("/materias", methods=['POST'])
def crearMateria():
    data = request.get_json()
    json = miControladorMateria.create(data)
    return jsonify(json)


@app.route("/materias/<string:id>", methods=['PUT'])
def modificarMateria(id):
    data = request.get_json()
    json = miControladorMateria.update(id, data)
    return jsonify(json)


@app.route("/materias/<string:id>", methods=['DELETE'])
def eliminarMateria(id):
    json = miControladorMateria.delete(id)
    return jsonify(json)


@app.route("/materias/<string:id>/departamento/<string:id_departamento>", methods=['PUT'])
def asignarDepartamentoAMateria(id, id_departamento):
    json = miControladorMateria.asignarDepartamento(id, id_departamento)
    return jsonify(json)


#######################################################################################################################

#####################################################Inscripcion#######################################################

@app.route("/inscripciones", methods=['GET'])
def getInscripciones():
    json = miControladorInscripcion.index()
    return jsonify(json)


@app.route("/inscripciones/<string:id>", methods=['GET'])
def getInscripcion(id):
    json = miControladorInscripcion.show(id)
    return jsonify(json)


@app.route("/inscripciones/estudiante/<string:id_estudiante>/materia/<string:id_materia>", methods=['POST'])
def crearInscripcion(id_estudiante, id_materia):
    data = request.get_json()
    json = miControladorInscripcion.create(data, id_estudiante, id_materia)
    return jsonify(json)


@app.route("/inscripciones/<string:id_inscripcion>/estudiante/<string:id_estudiante>/materia/<string:id_materia>",
           methods=['PUT'])
def modificarInscripcion(id_inscripcion, id_estudiante, id_materia):
    data = request.get_json()
    json = miControladorInscripcion.update(id_inscripcion, data, id_estudiante, id_materia)
    return jsonify(json)


@app.route("/inscripciones/<string:id_inscripcion>", methods=['DELETE'])
def eliminarInscripcion(id_inscripcion):
    json = miControladorInscripcion.delete(id_inscripcion)
    return jsonify(json)

#######################################################################################################################

def loadFileConfig():
    with open('config.json') as f:
        data = json.load(f)
    return data


if __name__ == '__main__':
    dataConfig = loadFileConfig()
    print("Server running : " + "http://" + dataConfig["url-backend"] + ":" + str(dataConfig["port"]))
    serve(app, host=dataConfig["url-backend"], port=dataConfig["port"])