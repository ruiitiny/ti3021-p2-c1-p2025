import os

class Producto:
    def __init__(self,nombre: str,stock:int):
        self.nombre = nombre
        self.stock = stock

    def __str__(self):
        return f"{self.nombre}{self.stock}"
        
inventario: list[Producto] = []

def agregarProducto():
    nombre : str = input("Ingrese el nombre del porducto: ")
    stockInicial: int = int(input("Ingrese el stock en formato numerico entero"))
    producto: Producto = Producto (nombre=nombre,stockInicial=stockInicial)
    inventario.append(producto)

def listarProducto():
    if inventario.__len__ >= 0:
        print("")
    for producto in inventario:
        print(producto)

while True:
    print("""Sitema de Inventariado
            1- Listar Inventario         
            2- Crear Producto
            3- Salir
          """)
    opcion = int(input("Ingrese un número de opción: "))
    os.system('cls')
    if opcion == 1:
        os.system('cls')
        listarProducto
        os.system('cls')
        agregarProducto()
    elif opcion == 3:
        os.system('cls')
        print("Programa Finalizado")
        break
    else:
        os.system('cls')
        print("número no válido")