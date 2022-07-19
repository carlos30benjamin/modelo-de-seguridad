

class Usuario:
    def __init__(self, ced, nom, telf, dir, correo):
        self.cedula = ced
        self.nombre = nom
        self.telefono = telf
        self.direccion = dir
        self.correo = correo
        
    def validaCedula(self):
        if len(self.cedula) == 10:
            return self.cedula
        else:
            return "9999999999"
        
    def validaTelefono(self):
        if len(self.telefono) == 10:
            return self.telefono
        else:
            return "9999999999"