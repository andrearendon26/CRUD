from abc import ABCMeta
"""
Contructor inicial el cual permiritira instanciar un objeto del tipo 
requerido a partir de la informacion almacenada en un diccionario 
"""


class AbstractModelo(metaclass= ABCMeta):
    def _init_(self, data):
        for llave, valor in data.items():
            setattr(self, llave, valor)