from datetime import date


class Persona:
    def __init__(
            self,
            rut: str,
            nombres: str,
            apellidos: str,
            fecha_nacimiento: date,
            cod_area: int,
            telefono: int
    ):
        self.rut: str = rut
        self.nombres: str= nombres
        self.apellidos: str = apellidos
        self.fecha_nacimiento: date = fecha_nacimiento
        self.cod_area: int = cod_area
        self.telefono: int = telefono
        
    def __str__(self):
        return f"{self.rut}{self.nombres}{self.apellidos}{self.fecha_nacimiento}{self.cod_area}{self.telefono}"

personas: list[Persona] = []


def persona_existe(persona_nueva = Persona)-> bool:
    for persona in personas:
        if persona.rut == persona_nueva.rut:
            print("Persona Existe")
            return True
    print("Persona no existe")
    return False

def create_persona():
    rut: str = input("Ingresa el rut de la persona: ")
    nombres: str = input("Ingresa los nombres de la persona: ")
    apellidos: str = input("Ingresa los aellidos de la persona: ")
    dia_nacimiento = int(input("Ingrese el día de nacimiento de la persona"))
    mes_nacimiento = int(input("Ingrese el mes  de nacimiento de la persona"))
    anio_nacimiento =int(input("Ingrese el año de nacimiento de la persona"))
    fecha_nacimiento: date = date(
        year = anio_nacimiento,
        month = mes_nacimiento,
        day = dia_nacimiento
    )

    cod_area: int = int(input("Ingresa el codigo de area de la persona: "))
    telefono: int = int(input("Ingresa el telefono de la persona: "))
    persona = Persona(
        rut = rut,
        nombres = nombres,
        apellidos = apellidos,
        fecha_nacimiento = fecha_nacimiento,
        cod_area = cod_area,
        telefono = telefono,
        persona = personas
    )
    if persona_existe(persona):
        return print(f"La persona con el rut {persona.rut} ya existe. Intente con otro rut.")
    
    personas.append(persona)


def read_persona():
    for persona in personas:
        print(persona)


def update_persona():
    pass


def delete_persona():
    pass


while True:
    print(
        """
        ||Gestor de Personas||
        1- Crear persona
        2- Listar persona
        0-Salir
        """
    )
    opcion = int(input("Ingrese una opcion [1-2-0]: "))
    if opcion == 1:
        create_persona()
    elif opcion == 2:
        read_persona()
    elif opcion  == 0:
        print("Adios")
        break
    else:
        print("Opción no valida")
