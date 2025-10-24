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

personas = []


def persona_existe(persona_nueva: Persona) -> bool:
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
    dia_nacimiento: int = int(input("Ingrese el día de nacimiento de la persona"))
    mes_nacimiento: int = int(input("Ingrese el mes  de nacimiento de la persona"))
    anio_nacimiento: int =int(input("Ingrese el año de nacimiento de la persona"))
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
        telefono = telefono
    )
    if persona_existe(persona):
        return print(f"La persona con el rut {persona.rut} ya existe. Intente con otro rut.")
    personas.append(persona)


def read_persona():
    for persona in personas:
        print(persona)


def update_persona():
    rut_busqueda = input("Ingresa el rut de la persona a editar (Ej: 12345678-K)")
    for persona in personas:
        print("")
        while True:
            if persona.rut == rut_busqueda:
                print(f"""
                    ||Edición de Personas||
                    Qué datos quieres cambiar?
                    1-Rut: {persona.rut}
                    2-Nombres: {persona.nombres}
                    3-Apellidos: {persona.apellidos}
                    4-Fecha de Nacimiento: {persona.fecha_nacimiento}
                    5-Código de area: {persona.cod_area}
                    6-Teléfono: {persona.telefono}
                    0-Salir/No seguir modificando
                    """
                )
                opcion = int(input("Qué datos quiere modificar?"))
                if opcion == 1:
                    rut: str = input("Ingresa el rut de la persona: ")
                    if persona_existe(persona):
                        print(f"La persona con el rut {persona.rut} ya existe. Intente con otro rut.")
                    persona.rut = rut
                    print("Rut modificado exitosamente")
                elif opcion == 2:
                    nombres: str = input("Ingresa los nombres de la persona: ")
                    persona.nombres =  nombres
                    print("Nomnbre modifcado exitosamente")
                elif opcion == 3:
                    apellidos: str = input("Ingresa los aellidos de la persona: ")
                    persona.apellidos = apellidos 
                    print("Apellido modficado exitosamente")
                elif opcion == 4:
                    dia_nacimiento: int = int(input("Ingrese el día de nacimiento de la persona"))
                    mes_nacimiento: int = int(input("Ingrese el mes  de nacimiento de la persona"))
                    anio_nacimiento: int =int(input("Ingrese el año de nacimiento de la persona"))
                    fecha_nacimiento: date = date(
                        year = anio_nacimiento,
                        month = mes_nacimiento,
                        day = dia_nacimiento
                    )
                    persona.fecha_nacimiento = fecha_nacimiento
                    print("fecha de nacimiento modificado exitosmante")
                elif opcion == 5:
                    cod_area: int = int(input("Ingresa el codigo de area de la persona: "))
                    persona.cod_area = cod_area
                    print("Código de area modificado exitosamente")
                elif opcion == 6: 
                    telefono: int = int(input("Ingresa el telefono de la persona: "))
                    persona.telefono = telefono 
                    print("Telefono modificado exitosamente ")
                elif opcion == 0:
                    print("Modificación completa")
                    break
                else:
                    print("Opcion incorrecta")
        print(f"Persona con rut {rut_busqueda} no existe")



def delete_persona():
    rut_busqueda = input("Ingresa el rut de la persona a editar (Ej: 12345678-K)")
    for persona in personas:
        if persona.rut == rut_busqueda:
            print(f"Eliminando persona {persona}")
            personas.remove(persona)
            print(f"Persona con rut {rut_busqueda} eliminada exitosamente")



while True:
    print(
        """
        ||Gestor de Personas||
        1- Crear persona
        2- Listar persona
        3- Actualizar datos
        0-Salir
        """
    )
    opcion = int(input("Ingrese una opcion [1-2-3-4-0]: "))
    if opcion == 1:
        create_persona()
    elif opcion == 2:
        read_persona()
    elif opcion == 3:
        update_persona()
    elif opcion  == 4:
        delete_persona()
    elif opcion  == 0:
        print("Adios")
        break
    else:
        print("Opción no valida")
