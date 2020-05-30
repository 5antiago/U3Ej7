from Personal import Personal

class PersonalApoyo(Personal):
    __cat = int

    def __init__(self, cuil, apellido, nom, basico, antig, cat):
        super().__init__(cuil, apellido, nom, basico, antig)
        self.__cat = int(cat)
    def getcategoria(self):
        return self.__cat
    def Sueldo(self):
        sueldo = self.getbasico()
        if self.__cat <= 10:
            sueldo *= 0.1
        elif self.__cat <= 20:
            sueldo *= 0.2
        else:
            sueldo *= 0.3
        sueldo += self.getbasico()*(self.getantig()*0.1)
        return sueldo
    def toJSON(self):
        d = dict(
            __class__ = self.__class__.__name__,
            __atributos__ = dict(
                        cat = self.__cat
                            )
            )
        d.get("__atributos__").update(super().toJSON().get("__atributos__"))
        return d
