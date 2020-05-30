from Personal import Personal

class Docente(Personal):
    """Atributos: carrera, cat, cargo"""

    __carrera = str
    __cargo = str
    __catedra = str

    def __init__(self, **kwargs):
        self.__carrera = kwargs.pop("carrera").lower()
        self.__catedra = kwargs.pop("cat").lower()
        self.__cargo = kwargs.pop("cargo").lower()
        super().__init__(**kwargs)
        
    def getcarrera(self):
        return self.__carrera 

    def getcargo(self):
        return self.__cargo
    def getcatedra(self):
        return self.__catedra
    def Sueldo(self):
        sueldo = self.getbasico()
        if self.__cargo == "simple":
            sueldo += sueldo*0.1
        elif self.__cargo == "semiexclusivo":
            sueldo += sueldo*0.2
        else:
            sueldo += sueldo*0.5
        sueldo += self.getbasico()*(0.01*self.getantig())
        return sueldo
    def toJSON(self):
        d = dict(
                __class__ = self.__class__.__name__, 
                __atributos__ = dict(
                            carrera = self.__carrera,
                            cargo = self.__cargo, 
                            cat = self.__catedra
            )
        )
        d.get("__atributos__").update(super().toJSON().get("__atributos__"))
        return d