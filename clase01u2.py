class Cliente:
    def __init__(self,nombre: str,rut: str,edad: int ):
        self.__nombre: str = nombre
        self.__rut: str =  rut
        self.__edad: int = edad 

@property
def nombre(self):
    return self.__nombre

clinte1: Cliente = Cliente(
    nombre = 'Felipe Villaroel', 
    rut = '21789567-k',
    edad = 21)

print(clinte1.nombre)