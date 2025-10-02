class Mascotas:
    def __init__(self,nombre:str, edad: int,especie:str):
        self._nombre: str = nombre
        self._edad: int = edad
        self._especie: str = especie

    @staticmethod
    def emitirSonido(sonido):
        print(sonido)

class Perro:
    def __init__(self):
        self.__historial_de_vacunas: list[dict] = []
    @staticmethod
    def emitirSonido(sonido):
        print(sonido)


class Gato:
    def __init__(self):
        self.registro_esterilizacion: list[dict] = []
    @staticmethod
    def emitirSonido(sonido):
        print(sonido)

class Ave:
    def __init__(self):
        self.control_vuelo: bool
        self.control_jaula: bool
    @staticmethod
    def emitirSonido(sonido):
        print(sonido)

class Vacunas:
    def __init__(self, nombre_vacuna: str, dosis:float, fecha_implememntacion):
        self.nombre_vacuna:  str = nombre_vacuna
        self.dosis: float = dosis
        self.fecha_implementacion

    def aplicarDosis(self):
        print(self)
        