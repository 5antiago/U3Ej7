from Personal import Personal

class Investigador(Personal):
    """Atributos: area, tipoinv"""
    __area = str
    __tiponvest = str

    def __init__(self, **kwargs):
        self.__area = kwargs.pop("area").lower()
        self.__tiponvest = kwargs.pop("tipoinv").lower() 
        super().__init__(**kwargs)

    def getarea(self):
        return self.__area
    def gettipoinvest(self):
        return self.__tiponvest
    def Sueldo(self):
        return self.getbasico()*(0.1*self.getantig())
    def toJSON(self):
        d = dict(
            __class__ = self.__class__.__name__,
            __atributos__ = dict(
                            area = self.__area,
                            tipoinv = self.__tiponvest
            )
        )
        d.get("__atributos__").update(super().toJSON().get("__atributos__"))
        return d