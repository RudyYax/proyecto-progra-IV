class Categoria:
    def __init__(self, id_categoria, nombre):
        self.id_categoria = id_categoria
        self.nombre = nombre

class Datos_Categoria:
    def __init__(self):
        self.categorias = {}

    def sub_menu(self):
        while True:
            print("\n Categorias")
            print("Bienvenido")
            print("1.- Registrar Nueva Categoria.")
            print("2.- Actualizar Categoria.")
            print("3.- Eliminar Categoria.")
            print("4.- Mostrar Categoria.")
            print("5.- Salir Categoria.")
            opcion = int(input("Seleccione que opcion desea:"))
            match opcion:
                case 1:
                    self.Agregar_Categoria()
                case 2:
                    print("Actualiar")
                case 3:
                    print("Eliminar")
                case 4:
                    print("Mostrar")
                case 5:
                    print("Salir")

    def Agregar_Categoria(self):
        print("\n Registrar Categoria")
        while True:
            try:
                Id_Categoria = input("Ingrese el Id de la nueva categoria")
                if Id_Categoria in self.categorias:
                    print("La categoria ya existe")
                    error = print("Presione ENTER para intentar de nuevo o 0 para salir.")
                    if error == 0:
                        break
                    else:
                        continue
                Nombre_Categoria = input("Ingrese el nombre de la categoria").lower()
                self.categorias[Id_Categoria] = Categoria(Id_Categoria, Nombre_Categoria)
                print("Producto registrado correctamente.")
                intento = input("Presione ENTER para agregar otra categoria o ingrese 0 para regresar al menú de categorias. ")
                if intento == "0":
                    break
            except ValueError:
                print("No se puedo agregar un producto")
    def Actualizar_Categoria(self):

        codigo_Actualizar = input("Ingrese el código de la categoria que desea actualizar: ")
        try:
            print(f"C")
            nueva_Categoria = int(input("Ingrese el nue: "))
            gestion.actualizar_stock(codigo, cantidad)
        except ValueError:
            print("La cantidad debe ser un número entero.")
        actualizar = int(input("Si desea actualizar el precio presione ENTER de lo contrario presione 0: "))
        if actualizar == 0:
            break
        elif actualizar == "":








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

datos_categoria = Datos_Categoria()

while True:
    menu = Menu()
    try:
        opcion = int(input("Ingrese la opcion que desea: "))
    except ValueError:
        print("Opción inválida")
        continue

    if opcion == 1:
        datos_categoria.sub_menu()
    elif opcion == 6:
        print("Saliendo...")
        break
    else:
        print("Opción no implementada todavía")
