from mc_python_flask.tutorialFUP.Modelos.Departamento import Departamento
class ControladorDepartamento():
   """
   constructor que permite llevar a cabo la creacion de instancias del controlador.
   """
   def __init__(self):
       print("Creando ControladorDepartamento")


   def index(self):
       print("Listar todos los departamentos")
       unDepartamento = {
           "_id": "abc456",
           "codigo": "123",
           "nombre": "Rectoria"

       }
       return [unDepartamento]


   def create(self, elDepartamento):
       print("Crear un departamento")
       elDepartamento = Departamento(elDepartamento)
       return elDepartamento.__dict__


   def show(self, id):
       print("Mostrando un departamento con id ", id)
       elDepartamento = {
           "_id": id,
           "_codigo": "123",
            "nombre": "Rectoria"
       }
       return elDepartamento


   def update(self,id, elDepartamento):
       print("Actualizando departamento con id ", id)
       elDepartamento = Departamento(elDepartamento)
       return elDepartamento.__dict__


   def delete(self, id):
       print("Elimiando departamento con id", id)
       return {"deleted_count": 1}

