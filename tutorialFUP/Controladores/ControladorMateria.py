from Repositorios.RepositorioMateria import RepositorioMateria
from Repositorios.RepositorioDepartamento import RepositorioDepartamento
from Modelos.Materia import Materia
from Modelos.Departamento import Departamento


class ControladorMateria():
    def __init__(self):
        self.repositorioMateria = RepositorioMateria()
        self.repositorioDepartamento = RepositorioDepartamento()

    def index(self):
        return self.repositorioMateria.findAll()

    def create(self, infoMateria):
        nuevoMateria = Materia(infoMateria)
        return self.repositorioMateria.save(nuevoMateria)

    def show(self, id):
        elMateria = Materia(self.repositorioMateria.findById(id))
        return elMateria.__dict__

    def update(self, id, infoMateria):
        materiaActual = Materia(self.repositorioMateria.findById(id))
        materiaActual.nombre = infoMateria["nombre"]
        materiaActual.creditos = infoMateria["creditos"]
        return self.repositorioMateria.save(materiaActual)

    def delete(self, id):
        return self.repositorioMateria.delete(id)

    """
        Relación departamento y materia
        """
    def asignarDepartamento(self, id, id_departamento):
        # Obtiene la materia actual por su ID desde la base de datos utilizando el repositorio
        materiaActual = Materia(self.repositorioMateria.findById(id))

        # Obtiene el departamento actual por su ID desde la base de datos utilizando el repositorio
        departamentoActual = Departamento(self.repositorioDepartamento.findById(id_departamento))

        # Asigna el departamento actual a la materia actual
        materiaActual.departamento = departamentoActual

        # Guarda los cambios de la materia actualizada en la base de datos utilizando el repositorio
        return self.repositorioMateria.save(materiaActual)