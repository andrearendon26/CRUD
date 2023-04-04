from mc_python_flask.tutorialFUP.Modelos.Materia import Materia

"""
Dentro de la clase se crean unos metodos, estos serán los encargados de manipular
a los modelos, en estos se programarán las tareas básicas tales como crear, listar,
visualizar, modificar y eliminar. (CRUD)
"""


class ControladorMateria():
   """
   constructor que permite llevar a cabo la creacion de instancias del controlador.
   """
   def __init__(self):
       print("Creando ControladorMateria")


   def index(self):
       print("Listar todos las materias")
       unaMateria = {
           "_id": "1A",
           "nombre": "Matematicas",
           "Docente": "Pedro Perez"
       }
       return [unaMateria]

   def create(self, unaMateria):
       print("Crear una Inscripcion")
       unaMateria = Materia(unaMateria)
       return unaMateria.__dict__


   def show(self, id):
       print("Mostrando un estudiante con id ", id)
       unaMateria = {
           "_id": id,
           "nombre": "Matematicas",
           "Docente": "Pedro Perez"
       }
       return unaMateria


   def update(self, id, unaMateria):
       print("Actualizando materia con id ", id)
       unaMateria = Materia(unaMateria)
       return unaMateria.__dict__


   def delete(self, id):
       print("Elimiando materia con id ", id)
       return {"deleted_count": 1}
