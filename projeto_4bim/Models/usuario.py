import json
from crud import CRUD

class Usuario:
    def __init__(self,id,nome,email,fone,senha):
        self.__id = 0
        self.__nome = ""
        self.__email = ""
        self.__senha = ""


    #set e get

    def __str__(self):
        return f"{self.__id} - {self.__nome} - {self.__email} - {self.__senha}"


class Usuarios(CRUD):