from Lista import Lista
from menu import Menu
from ObjectEncoder import ObjectEncoder
if __name__ == "__main__":
    try:
        obj = ObjectEncoder()
        elementos = obj.Decoder(obj.Leer("personal.json"))
        del obj
    except FileNotFoundError:
        elementos = Lista()
        
    menu = Menu()
    print(" 1. Insertar agente \n 2. Agregar \n 3. Mostrar \n 4. Docentes Invetigadores de la carrera \n 5. Agentes en invetigacion")
    print(" 6. Sueldos \n 7. Categoria de investigacion \n 8. Guardar  \n 0. Salir")
    op = int(input("\n Ingrese opcion: "))
    while op > 0:
        menu.opcion(op,elementos)
        print(" 1. Insertar agente \n 2. Agregar \n 3. Mostrar \n 4. Docentes Invetigadores de la carrera \n 5. Agentes en invetigacion")
        print(" 6. Sueldos \n 7. Categoria de investigacion \n 8. Guardar  \n 0. Salir")
        op = int(input("\n Ingrese opcion: "))