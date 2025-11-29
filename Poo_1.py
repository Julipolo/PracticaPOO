class Persona:
    def __init__(self,nombre,apellido,edad):
        self.nombre_apellido = nombre + " " + apellido
        self.edad = edad     

julian=Persona("julian","polo",19)
print(julian.edad)