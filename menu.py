from IElemento import Ielemetos
from ObjectEncoder import ObjectEncoder
from Docente import Docente
from Investigador import Investigador
from Apoyo import PersonalApoyo
from DocenteInvetigador import DocenteInvetigador
class Menu(object):
    __switcher = dict
    def __init__(self):
        self.__switcher = { 1: self.Insert, 2: self.Agregar, 3: self.Mostrarpos, 4: self.carrerainvest, 5:self.agentesinvestigacion,
                            6: self.Sueldos, 7:self.catinvetigacion, 8:self.guardar}
    def opcion(self, op, elementos):
        a = self.__switcher.get(op, lambda a: print("Opcion Incorrecta"))
        if a == self.Insert or a == self.Agregar or a == self.Mostrarpos:
            a(Ielemetos(elementos))
        else:
            a(elementos)

    def __crear_agente(self):
        op = 0
        aux = None
        while op == 0:
            op = int(input(" 1. Personal de apoyo \n 2. Docente \n 3. Investigador \n 4. Docente Invetigador \nIngrese opcion: "))
            if op == 1:
                aux = PersonalApoyo(cuil=input("Ingrese Cuil: "), apellido=input("Ingrese Apellido: "), nom=input("Ingrese nombre: "), 
                basico= input("Ingrese Basico: "), antig=input("Ingrese antiguedad: "), cat=input("Ingrese categoria: "))
            elif op == 2:
                aux = Docente(cuil=input("Ingrese Cuil: "), apellido=input("Ingrese Apellido: "), nom=input("Ingrese nombre: "), basico= input("Ingrese Basico: "),
                antig=input("Ingrese antiguedad: "), carrera=input("Ingrese Carrera: "), cat=input("Ingrese Catedra: "), cargo=input("Ingrese Cargo: ") )
            elif op == 3:
                aux = Investigador(cuil=input("Ingrese Cuil: "), apellido=input("Ingrese Apellido: "), nom=input("Ingrese nombre: "), basico= input("Ingrese Basico: "),
                antig=input("Ingrese antiguedad: "), area= input("Ingrese area de Invetigacion: "), tipoinv= input("Ingrese tipo de invetigacion: "))
            elif op == 4:
                aux = DocenteInvetigador(cuil=input("Ingrese Cuil: "), apellido=input("Ingrese Apellido: "), nom=input("Ingrese nombre: "), basico= input("Ingrese Basico: "),
                antig=input("Ingrese antiguedad: "), carrera=input("Ingrese Carrera: "), 
                cat=input("Ingrese Catedra: "), cargo=input("Ingrese Cargo: "), area= input("Ingrese area de Invetigacion: "), 
                tipoinv= input("Ingrese tipo de invetigacion: "), catincent=(input("Ingrese categoria de incentivos: ")), extra=input("Ingrese extra: "))
            else:
                op = 0
        return aux
    def Insert(self, elementos):
        try:
            elementos.insertarElemento(self.__crear_agente(), int(input("Ingrese posicion a insertar: "))-1)
        except IndexError:
            print("Posicion Invalida")
    def Agregar(self, elementos):
        elementos.agregarElemeto(self.__crear_agente())
    def Mostrarpos(self, elementos):
        try:
            print("Se encuentra un: {}".format(elementos.MostrarElemento(int(input("Ingrese la posicion a Mostrar: "))-1).__class__.__name__))
        except IndexError:
            print("Posicion Invalida")
    def guardar(self, elementos):
        print("Guardando...")
        obj = ObjectEncoder()
        if obj.Guardar(elementos.toJSON(), "personal.json"):
            print("Guardado Exitoso")
        else:
            print("Error al Guardar")
    def carrerainvest(self, elementos):
        print(elementos.carrerainvetigadores(input("Ingrese Carrera: ").lower()))
    def agentesinvestigacion(self, elementos):
        invest, docinv = elementos.agentesinvestigacion()
        print(" - Docentes Invetigadores : {} \n - Investigadores: {}".format(docinv, invest))
    def catinvetigacion(self, elementos):
        acum = 0
        aux = ""
        lista = elementos.catinvetigacion(input("Ingrese categoria: "))
        if lista == []:
            print("No hay agentes para la categoria elegida")
        else:
            for i in lista:
                aux += "- {0:10} \n   -Importe extra: {1:5.2f}".format(i.getnom().upper(), i.getextra())
                acum += i.getextra()
            print("{} \n \n Total:  {:6.2f}".format(aux, acum))
    def Sueldos(self, elementos):
        aux = ""
        for i in elementos.Sueldos():
            aux += "\n- {0:20} \n    -Sueldo: {1:5.2f} \n    -Agente: {2:20}".format(i.getapellido().upper() +" "+i.getnom().upper(), i.Sueldo(), i.__class__.__name__)
        print (aux)