class Estudiante:
    def __init__(self,nombre,edad,grado):
        self.nombre = nombre
        self.edad = edad
        self.grado = grado
    
    def estudiar(self):
        print(f"{self.nombre} esta estudiando")

# Primer ejercicio
benicio = Estudiante("Benicio",18,6)

print(benicio.edad)

# Segundo ejercicio
nombre = input("Ingrese su nombre")
edad = int(input("Ingrese su edad"))
grado = int(input("Ingrese su grado"))

estudiante = Estudiante(nombre,edad,grado)
print(f"""
      DATOS DEL ESTUDIANTE:
      Nombre : {estudiante.nombre}
      Edad : {estudiante.edad}
      Grado : {estudiante.grado}
      """)
while True:
    estudiar = input()
    if estudiar.lower() == "estudiar":
        estudiante.estudiar()
    