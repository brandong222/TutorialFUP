from Repositorios.InterfaceRepositorio import InterfaceRepositorio
from Modelos.Inscripcion import Inscripcion
from bson import ObjectId

class RepositorioInscripcion(InterfaceRepositorio[Inscripcion]):
    def getListadoInscritosEnMateria(self, id_materia):
        # Construye una consulta MongoDB para obtener los inscritos en una materia específica.
        # Se crea un diccionario que representa la consulta. La clave "materia.$id" se utiliza
        # para buscar inscripciones con el campo "materia" que contenga el ObjectId de la materia
        # correspondiente al id_materia proporcionado.
        theQuery = {"materia.$id": ObjectId(id_materia)}

        # Llama al método "query" de la superclase InterfaceRepositorio para ejecutar la consulta
        # en la base de datos. Este método retorna una lista con la información de los estudiantes
        # inscritos en la materia.
        return self.query(theQuery)

    def getMayorNotaPorCurso(self):
        # Se define la primera etapa del pipeline de agregación para MongoDB. Se utiliza el operador "$group"
        # para agrupar los documentos de acuerdo a la materia. En la etapa "$group", se calcula la máxima nota final
        # de cada materia y se almacena en el campo "max". Además, se guarda el primer documento del grupo
        # (con mayor nota) en el campo "doc".
        query1 = {
            "$group": {
                "_id": "$materia",
                "max": {
                    "$max": "$nota_final"
                },
                "doc": {
                    "$first": "$$ROOT"
                }
            }
        }

        # Se construye el pipeline de agregación con la etapa definida anteriormente.
        pipeline = [query1]

        # Se llama al método "queryAggregation" para ejecutar la agregación en MongoDB.
        # Este método retornará una lista de documentos que representan la máxima nota
        # de cada materia junto con los detalles del primer documento con esa nota.
        return self.queryAggregation(pipeline)

    def promedioNotasEnMateria(self, id_materia):
        # Se define la primera etapa del pipeline de agregación para MongoDB. Se utiliza el operador "$match" para
        # filtrar los documentos cuya materia coincida con el ID proporcionado.
        query1 = {
            "$match": {"materia.$id": ObjectId(id_materia)}
        }

        # Se define la segunda etapa del pipeline de agregación para MongoDB. Se utiliza el operador "$group" para
        # agrupar los documentos de acuerdo a la materia. En la etapa "$group", se calcula el promedio de las notas
        # finales de cada materia y se almacena en el campo "promedio".
        query2 = {
            "$group": {
                "_id": "$materia",
                "promedio": {
                    "$avg": "$nota_final"
                }
            }
        }

        # Se construye el pipeline de agregación con las etapas definidas anteriormente.
        pipeline = [query1, query2]

        # Se llama al método "queryAggregation" para ejecutar la agregación en MongoDB. Este método retornará una lista
        # de documentos que representan el promedio de notas finales de la materia con el ID proporcionado.
        return self.queryAggregation(pipeline)

