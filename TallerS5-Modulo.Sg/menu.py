class Menu:
    
    def __init__(self):
        pass
    
    def menu(self,opciones,titulo):
        print(titulo)
        for opcion in opciones:
            print(opcion)
        print("-"*76)
        opc = input("Elija Una Opcion: ".format(len(opciones)))
        return opc
    