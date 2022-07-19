from menu import Menu
import os

class Administrador(Menu):
    def __init__(self,tamanio=4):
       self.lista = []
       self.tope = 0
       self.size = tamanio
       
    
    def menu(self):
        opcion = self.menu(["1.- Identificacion", "2.- Area", "3.- Sueldo", "4.- Cerrar Seccion"]," MENU ") 
        os.system("cls")
        if opcion == '1':
            try:
                print(" INGRESE SUS DATOS ")
                dato = input("Escribe los datos para registrarlo : ")
                
                self.push(dato)
                input("\nPresione ENTER para continuar..."), os.system("cls"), self.menu_lista()

            except ValueError:
                print(), input("\nIngrese valores nuemericos!"), os.system("cls"), self.menu_lista()
                
        elif opcion == '2':
            print(" ELIMINAR DATOS ")
            print("Los  datos se han eliminado correctamente:",self.pop())
            
            input("\nPresione ENTER para continuar..."), os.system("cls"), self.menu_lista()
                
        elif opcion == '3':
            print(" DATOS DE LA LISTA ")
            self.mostrar()
            
            input("\nPresione ENTER para continuar..."), os.system("cls"), self.menu_lista()
        
        elif opcion == '4':
            print(" ELIMINAR UN DATO ")
            self.mostrar()
            try:
                pos = int(input("Ingrese la posición del dato a eliminar: "))
                print(self.eleminarElemento(pos)) 
                
                input("\nPresione ENTER para continuar..."),os.system("cls"), self.menu_lista()
                
            except ValueError:
                
                input("\nIngrese Valores NUmericos!"), os.system("cls"), self.menu_lista()
        
        elif opcion == '5':
            print(" INGRESE UN DATO ")
            self.mostrar()
            try:
                print(self.insertarElemento())
                
                input("\nPresione ENTER para continuar..."),os.system("cls"), self.menu_lista()
                
            except ValueError:
                print("*"*48)
                input("\nIngrese Valores Numericos!"), os.system("cls"), self.menu_lista()
        
        elif opcion == '6':
            print(" BUSCAR  DATO ")
            print(self.buscar())
            
            input("\nPresione ENTER para continuar..."), os.system("cls"), self.menu_lista()      
                
        elif opcion == '7': 
            pass
         
    def push(self,dato):
        if self.tope < self.size:
            self.lista = self.lista + [dato]
            self.tope += 1 
        else:
            print("La lista se encuentra llena")
        
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
            return "Lista llena, eliminar un dato"
        else:
            pos = int(input("Ingresa la posición: "))
            dato = input("Ingrese un valor: ")
            self.lista.insert(pos, dato)
            self.tope += 1
            return "Valor agregado correctamente"
    
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
                return "Intruducir una posición"      
    
    def mostrar(self):
        if self.lista != 0:
            print("Posicion"," "*5, "Valor")
            for pos,ele in enumerate(self.lista):
                print("   {}          [{}]".format(pos,ele))
        else:
            print("La lista esta vacia!")

    def empty(self):
        if self.tope == 0:
            return True
        else:
            return False