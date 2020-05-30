import abc

class Personal(abc.ABC):
    __cuil = str
    __apellido = str
    __nombre = str
    __basico = float
    __antig = int

    def __init__(self, cuil, apellido, nom, basico, antig):
        self.__cuil = cuil
        self.__apellido = apellido.lower()
        self.__nombre = nom.lower()
        self.__basico = float(basico)
        self.__antig = int(antig)
    def getnom(self):
        return self.__nombre
    def getapellido(self):
        return self.__apellido
    def getcuil(self):
        return self.__cuil
    def getbasico(self):
        return self.__basico
    def getantig(self):
        return self.__antig
    def toJSON(self):
        return dict(
            __atributos__ = dict(
                            cuil = self.__cuil,
                            apellido = self.__apellido, 
                            nom = self.__nombre,
                            basico = self.__basico,
                            antig = self.__antig
                            )
                )
    @abc.abstractmethod
    def Sueldo(self):
        pass