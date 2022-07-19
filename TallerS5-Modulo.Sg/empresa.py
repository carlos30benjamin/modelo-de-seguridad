class Empresa:
    def __init__(self,ruc, nombre, telf, dirc, correo):
        self.ruc = ruc
        self.razonsocial = nombre
        self.telf = telf
        self.dirc = dirc
        self.correo = correo

if __name__ == "__main__":
    emp1 = Empresa("094372824", "San Gabriel", "0953654921", "Naranjito", "holamundo24@gmail.com")
    emp2 = Empresa("048875243", "Mathius", "0980341678", "Bucay", "holamundo@gmail.com")
    print(emp1.razonsocial, emp1.ruc)
    print(emp2.razonsocial, emp2.ruc)