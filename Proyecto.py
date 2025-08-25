class Categoria:
    def __init__(self, id_categoria, Nombre):
        self.id_categoria = id_categoria
        self.Nombre = Nombre

class Producto:
    def __init__(self, id_producto, nombre, precio, id_categoria, total_compras, total_ventas, stock):
        self.id_producto = id_producto
        self.nombre = nombre
        self.precio = precio
        self.id_categoria = id_categoria
        self.total_compras = total_compras
        self.total_ventas = total_ventas
        self.stock = stock

class Menu:
    def __init__(self):
                print("\n ---Bienvenidos a nuestra tienda ----")
                print("1.- Agregar Categoria")
                print("2.- Agregar Producto")
                print("3.- Agregar Cliente")
                print("4.- Agregar Proveedor")
                print("5.- Agregar Empleado")
                print("6.- salir")
categorias = {}
productos = {}

while True:
        menu = Menu()
        try:
            opcion = int(input("Ingrese la opcion que deseea:"))
        except(ValueError):
            opcion = input("Opcion ingresada no valida Presione ENTER para continuar o 6 para salir")
            if opcion == "":
                continue
            else:
                break

        match opcion:
            case 1:
                print("\n Agregar Categoria")
                print("Bienvenido")
                print("1.- Registrar Nueva Categoria.")
                print("2.- Actualizar Categoria.")
                print("2.- Eliminar Categoria.")
                print("3.- Mostrar Categoria.")

