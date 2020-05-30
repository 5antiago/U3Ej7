from zope.interface import implementer, implements
from Nodo import Nodo
from IElemento import Ielemetos
from DocenteInvetigador import DocenteInvetigador
from Investigador import Investigador
@implementer(Ielemetos)
class Lista(object):
    __start = None
    __actual = None
    __indice = int
    __tope = int
    def __init__(self):
        self.__start = None
        self.__actual = None
        self.__indice = 0
        self.__tope = 0
    def agregarElemeto(self, dato):
        nodo = Nodo(dato)
        nodo.setSig(self.__start)
        self.__start = nodo
        self.__actual = nodo
        self.__tope +=1
    def insertarElemento(self, elemento, pos):
        aux = self.__start
        i = 0
        elemento = Nodo(elemento)
        while i<pos and aux != None:
            aux = aux.getSig()
            i+=1
        if aux == None:
            raise IndexError
        else:
            elemento.setSig(aux.getSig())
            aux.setSig(elemento)
            self.__tope +=1
    def MostrarElemento(self, pos):
        aux = self.__start
        i = 0
        while i<pos and aux != None:
            aux = aux.getSig()
            i +=1
        if aux == None:
            raise IndexError
        else:
            return aux.getDato()
    def carrerainvetigadores(self, carrera):
        lista = sorted([agente.getnom() for agente in self if (type(agente) == DocenteInvetigador)])
        aux = ""
        for i in lista:
            aux += "\n - {}".format(i)
        return aux
    def agentesinvestigacion(self):
        investigadores = 0
        docentesinvets = 0
        for i in self:
            if type(i) == DocenteInvetigador:
                docentesinvets += 1
            elif type(i) == Investigador:
                investigadores += 1
        return investigadores, docentesinvets
    def catinvetigacion(self, cat):
        cat = cat.upper()
        aux = []
        for i in self:
            if type(i) == DocenteInvetigador and i.getcategoriaincentivos() == cat :
                aux.append(i)
        return aux  
    def Sueldos(self):
        listado = []
        first = True
        for agente in self:
            i = 0
            if first:
                listado.append(agente)
                first = False
            else:
                while i < len(listado) and listado[i].getapellido() < agente.getapellido():
                    i+=1
                listado.insert(i, agente)
        return listado
    def __next__(self):
        if self.__indice == self.__tope:
            self.__actual = self.__start
            self.__indice = 0
            raise StopIteration
        else:
            self.__indice += 1
            dato = self.__actual.getDato()
            self.__actual = self.__actual.getSig()
            return dato
    def toJSON(self):
        return dict(
            __class__ = self.__class__.__name__, 
            Elementos=[elemento.toJSON() for elemento in self]
        )
    def __iter__(self):
        return self
    def __len__(self):
        return self.__tope
