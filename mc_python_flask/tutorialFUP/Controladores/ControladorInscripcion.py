from mc_python_flask.tutorialFUP.Modelos.Inscripcion import Inscripcion

"""
Dentro de la clase se crean unos metodos, estos serán los encargados de manipular
a los modelos, en estos se programarán las tareas básicas tales como crear, listar,
visualizar, modificar y eliminar. (CRUD)
"""


class ControladorInscripcion():
   """
   constructor que permite llevar a cabo la creacion de instancias del controlador.
   """
   def __init__(self):
       print("Creando ControladorInscripcion")


   def index(self):
       print("Listar todos la inscripcion")
       unaInscripcion = {
           "_id": "11B",
           "nombre":"Pedro",
           "apellido": "Perez",
           "carrera":"sistemas"
       }
       return [unaInscripcion]

   def create(self, unaInscripcion):
       print("Crear una inscripcion")
       unaInscripcion = Inscripcion(unaInscripcion)
       return unaInscripcion.__dict__


   def show(self, id):
       print("Mostrando una inscripcion con id ", id)
       unaInscripcion = {
           "_id": id,
           "nombre":"Pedro",
           "apellido": "Perez",
           "carrera":"sistemas"
       }
       return unaInscripcion


   def update(self, id, unaInscripcion):
       print("Actualizando inscripcion con id ", id)
       unaInscripcion = Inscripcion(unaInscripcion)
       return unaInscripcion.__dict__


   def delete(self, id):
       print("Elimiando Inscripcion con id ", id)
       return {"deleted_count": 1}
