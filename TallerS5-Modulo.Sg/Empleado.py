from menu import Menu
import os

class Empleado(Menu):
    def __init__(self,tam=4):
       self.lista = []
       self.tope = 0
       self.size = tam
       
    
    def menu_empleado(self):
        opcion = self.menu(["1) Art", "2) Lact", "3) Post", "4) Eliminar", "5) Insertar", "6) Buscar", "7) Salir"],"*"*20+" MENU LISTA "+"*"*20) 
        os.system("cls")
        if opcion == '1':
            try:
                print("*-*"*20+" INGRESO DE DATOS "+"*-*"*20)
                dato = input("Escribe una dato para agregarlo: ")
                print("*-*"*55)
                self.push(dato)
                input("\nPresine una tecla"), os.system("cls"), self.menu_lista()

            except ValueError:
                print("*-*"*50), input("\nIngrese un valor Numerico"), os.system("cls"), self.menu_lista()
                
        elif opcion == '2':
            print("*-*"*20+" ELIMINACION DE DATO "+"*-*"*20)
            print("El dato se a eliminado correctamente:",self.pop())
            print("*_*"*55)
            input("\nPresione ENTER para continuar..."), os.system("cls"), self.menu_lista()
                
        elif opcion == '3':
            print("*-*"*20+" DATOS DE LA LISTA "+"*-*"*20)
            self.mostrar()
            print("*-*"*55)
            input("\nPresione ENTER para continuar..."), os.system("cls"), self.menu_lista()
        
        elif opcion == '4':
            print("*-*"*20+" ELIMINAR UN DATO "+"*-*"*20)
            self.mostrar()
            try:
                pos = int(input("Ingrese la posición del dato a eliminar: "))
                print(self.eleminarElemento(pos)) 
                print("*-*"*50)
                input("\nPresione ENTER para continuar..."),os.system("cls"), self.menu_lista()
                
            except ValueError:
                print("*-*"*50)
                input("\nIngrese un valor Numerico"), os.system("cls"), self.menu_lista()
        
        elif opcion == '5':
            print("*-*"*20+" INGRESE UN DATO "+"*-*"*20)
            self.mostrar()
            try:
                print(self.insertarElemento())
                print("*-*"*50)
                input("\nPresione ENTER para continuar..."),os.system("cls"), self.menu_lista()
                
            except ValueError:
                print("*-*"*50)
                input("\nIngrese un valor Numerico"), os.system("cls"), self.menu_lista()
        
        elif opcion == '6':
            print("*_*"*20+" BUSCAR DATO "+"*_*"*20)
            print(self.buscar())
            print("*-*"*50)
            input("\nPresione ENTER para continuar..."), os.system("cls"), self.menu_lista()      
                
        elif opcion == '7': 
            pass
         
    def push(self,dato):
        if self.tope < self.size:
            self.lista = self.lista + [dato]
            self.tope += 1 
        else:
            print(" Lista llena")
        
    def pop(self):
        if self.empty():
            return "Lista Vacia"
        else:
            top = self.lista[-1]
            self.tope -= 1
            self.lista = self.lista[:-1]
            return top
    
    def eleminarElemento(self,pos):
        if pos < 0 or pos >= self.tope:
            return "Error"
        else:
            self.tope -= 1
            self.lista = self.lista[:pos] + self.lista[pos + 1:]
            return f"Lista Actualizada {self.lista}"
 
    def insertarElemento(self):
        if len(self.lista) == self.size or self.tope > self.size:
            return "Lista llena, elimine un dato"
        else:
            pos = int(input("Ingresa la posición: "))
            dato = input("Ingrese un valora: ")
            self.lista.insert(pos, dato)
            self.tope += 1
            return "Valor agregado"
    
    def buscar(self):
        if self.tope == 0:
            return "La Lista se encuentra vacia"
        else:
            self.mostrar()
            try:
                
                buscado = int(input("Ingrese la posicion del valor a buscar: "))
                enc = False
                for pos, elemento in enumerate(self.lista):
                    if elemento == buscado:
                        enc = True
                        break
                if enc == True:  
                    return "La posición es: {}".format(pos)
                else:
                    return "-1"
            except ValueError:
                return "Debes intruducir una posición"      
    
    def mostrar(self):
        if self.lista != 0:
            print("Posicion"," "*5, "Valor")
            for pos,ele in enumerate(self.lista):
                print("   {}          [{}]".format(pos,ele))
        else:
            print("La lista se escuentra vacia")

    def empty(self):
        if self.tope == 0:
            return True
        else:
            return False