from empresa import Empresa
from menu import Menu
from admin import Administrador
from Empleado import Empleado
import os

class Main(Menu):
    
    def __init__(self):
        pass
    
    def menu_main(self):
        opcion = self.menu(["1.- Administrador", "2.- Empleado",  "3.- Cerrar"],"-"*30+" MENU PRINCIPAL "+"-"*30)
        os.system("cls")
        
        if opcion == '1':
            admin = Administrador()
            os.system("cls")
            return admin.menu_admin()
                
        elif opcion == '2':
            empleado = Empleado()
            os.system("cls")
            return empleado.menu_empleado()
        
        elif opcion == '3':
            print("-"*20+" EXCELENTE SEMANA "+"-"*20)
            
                

opc = Main()
opc.menu_main()