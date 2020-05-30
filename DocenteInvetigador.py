from Docente import Docente
from Investigador import Investigador

class DocenteInvetigador(Docente, Investigador):
    """cuil, apellido, nom, basico, antig, carrera, cargo, cat, area, tipoinv, catincent, extra"""
    __catincent = str
    __extra = float

    def __init__(self,**kwargs ):
        self.__catincent = kwargs.pop("catincent").upper()
        self.__extra = float(kwargs.pop("extra"))
        super().__init__(**kwargs)
    def getcategoriaincentivos(self):
        return self.__catincent
    def getextra(self):
        return self.__extra
    def Sueldo(self):
        return  Docente.Sueldo(self) + self.__extra
    def toJSON(self):
        d = dict(
            __class__ = self.__class__.__name__, 
            __atributos__ = dict(
                            extra = self.__extra,
                            catincent = self.__catincent, 
            )
        )
        d.get("__atributos__").update(super().toJSON().get("__atributos__"))
        return d