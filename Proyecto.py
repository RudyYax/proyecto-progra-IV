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
            print("5.- Buscar Categoria.")
            print("6.- Salir Categoria.")
            opcion = int(input("Seleccione que opcion desea:"))
            match opcion:
                case 1:
                    self.Agregar_Categoria()
                case 2:
                    self.Actualizar_Categoria()
                case 3:
                    self.Eliminar_Categoria()
                case 4:
                    self.Mostrar_Categorias()
                case 5:
                    self.Buscar_Categoria()
                case 6:
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
        print("\n Actualizar Categoria")
        while True:
            id_Categoria = input("Ingrese el ID de la categoria que desea modificar")
            if id_Categoria not in self.categorias:
                print("Categoria no encontrada")
                reintentar = input("Presione ENTER para intentar de nuevo o 0 para regresar al menú de Categorias")
                if reintentar == "0":
                    break
            nombre_nuevo = input("Ingrese el nuevo nombre de la categoria").lower()
            self.categorias[id_Categoria].nombre = nombre_nuevo
            print("Producto actualizado correctamente.")
            intento = input("Presione ENTER para actualizar otro producto o 0 para regresar al menú de Categorias ")
            if intento == "0":
                break

    def Eliminar_Categoria(self):
        print("\n Eliminar Categoria")
        while True:
            id_Categoria = input("Ingrese el ID de la categoria que desea eliminar")
            if id_Categoria in self.categorias:
                eliminado = self.categorias.pop(id_Categoria)
                print(f"El producto  ha sido eliminado correctamente.")
                reintentar = input("Presione ENTER para intentar de nuevo o 0 para regresar al menú de Categorias")
                if reintentar == "0":
                    break
            else:
                intentar = input("Categoria no encontrada presione ENTER para intentar de nuevo o 0 para regresar al menú de categorias")
                if intentar == "0":
                    break

    def quick_sort(self, lista):
        if len(lista) <= 1:
            return lista
        else:
            pivote = lista[0].nombre.lower()
            mayores = [x for x in lista[1:] if x.nombre.lower() > pivote]
            iguales = [x for x in lista[1:] if x.nombre.lower() == pivote]
            menores = [x for x in lista[1:] if x.nombre.lower() < pivote]
            return self.quick_sort(menores) + [lista[0]] + iguales + self.quick_sort(mayores)

    def Mostrar_Categorias(self):
        if not self.categorias:
            print(f"No hay Categorias Registradas")
            return
        lista_Categorias = list(self.categorias.values())
        ordenados = self.quick_sort(lista_Categorias)
        print("Productos ordenados por nombre: ")
        for i, categoria in enumerate(ordenados, start=1):
            print(f"{i}- ID: {categoria.id_categoria} / nombre {categoria.nombre}")

    def Buscar_Categoria(self):
        while True:
            id_buscar = input("Ingrese el codigo de la categoria que desea buscar")
            if id_buscar not in self.categorias:
                print("Categoria no encontrada")
                reintentar = input("Presione ENTER para intentar de nuevo o 0 para regresar al menú de Categorias")
                if reintentar == "0":
                    break
            categoria = self.categorias.get(id_buscar)
            if categoria:
                print(f"Categoria encontrada: ID: {categoria.id_categoria} / Nombre: {categoria.nombre}")
                intento = input("\n Presione ENTER para agregar otra categoria o ingrese 0 para regresar al menú de categorias. ")
                if intento == "0":
                    break
            else:
                print("Categoria no encontrada.")




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
