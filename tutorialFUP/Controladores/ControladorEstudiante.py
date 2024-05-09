from Modelos.Estudiante import Estudiante
from Repositorios.RepositorioEstudiante import RepositorioEstudiante


class ControladorEstudiante():
    def __init__(self):
        # Se crea una instancia del RepositorioEstudiante para interactuar con la base de datos
        self.repositorioEstudiante = RepositorioEstudiante()

    def index(self):
        # Retorna todos los estudiantes existentes en la base de datos
        return self.repositorioEstudiante.findAll()

    def create(self, infoEstudiante):
        # Crea un nuevo objeto Estudiante a partir de la información recibida
        nuevoEstudiante = Estudiante(infoEstudiante)

        # Guarda el nuevo estudiante en la base de datos utilizando el repositorio
        return self.repositorioEstudiante.save(nuevoEstudiante)

    def show(self, id):
        # Obtiene un estudiante por su ID desde la base de datos utilizando el repositorio
        elEstudiante = Estudiante(self.repositorioEstudiante.findById(id))

        # Retorna los atributos del estudiante como un diccionario
        return elEstudiante.__dict__

    def update(self, id, infoEstudiante):
        # Obtiene el estudiante actual por su ID desde la base de datos utilizando el repositorio
        estudianteActual = Estudiante(self.repositorioEstudiante.findById(id))

        # Actualiza los atributos del estudiante con la información recibida
        estudianteActual.cedula = infoEstudiante["cedula"]
        estudianteActual.nombre = infoEstudiante["nombre"]
        estudianteActual.apellido = infoEstudiante["apellido"]

        # Guarda los cambios del estudiante actualizado en la base de datos utilizando el repositorio
        return self.repositorioEstudiante.save(estudianteActual)

    def delete(self, id):
        # Elimina un estudiante por su ID desde la base de datos utilizando el repositorio
        return self.repositorioEstudiante.delete(id)
