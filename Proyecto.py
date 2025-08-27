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
            opcion = int(input("Seleccione que opcion desea: "))
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
                    print("Salir...")
                    print("REGRESANDO AL MENÚ PRINCIPAL....")
                    break


    def Agregar_Categoria(self):
        print("\n Registrar Categoria")
        while True:
            try:
                Id_Categoria = input("Ingrese el Id de la nueva categoria: ")
                if Id_Categoria in self.categorias:
                    print("La categoria ya existe.")
                    error = print("Presione ENTER para intentar de nuevo o 0 para salir.")
                    if error == 0:
                        break
                    else:
                        continue
                Nombre_Categoria = input("Ingrese el nombre de la categoria: ").lower()
                self.categorias[Id_Categoria] = Categoria(Id_Categoria, Nombre_Categoria)
                print("Categoría registrada correctamente.")
                intento = input("Presione ENTER para agregar otra categoria o ingrese 0 para regresar al menú de categorias. ")
                if intento == "0":
                    break
            except ValueError:
                print("No se puede agregar una categoría")

    def Actualizar_Categoria(self):
        print("\n Actualizar Categoria")
        while True:
            id_Categoria = input("Ingrese el ID de la categoria que desea modificar: ")
            if id_Categoria not in self.categorias:
                print("Categoria no encontrada.")
                reintentar = input("Presione ENTER para intentar de nuevo o 0 para regresar al menú de Categorias: ")
                if reintentar == "0":
                    break
                else:
                    continue
            nombre_nuevo = input("Ingrese el nuevo nombre de la categoria: ").lower()
            self.categorias[id_Categoria].nombre = nombre_nuevo
            print("Producto actualizado correctamente.")
            intento = input("Presione ENTER para actualizar otro producto o 0 para regresar al menú de Categorias:  ")
            if intento == "0":
                break

    def Eliminar_Categoria(self):
        print("\n Eliminar Categoria")
        while True:
            id_Categoria = input("Ingrese el ID de la categoria que desea eliminar: ")
            if id_Categoria in self.categorias:
                eliminado = self.categorias.pop(id_Categoria)
                print(f"El producto  ha sido eliminado correctamente.")
                reintentar = input("Presione ENTER para intentar de nuevo o 0 para regresar al menú de Categorias: ")
                if reintentar == "0":
                    break
            else:
                intentar = input("Categoria no encontrada presione ENTER para intentar de nuevo o 0 para regresar al menú de categorias: ")
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
            print(f"No hay Categorias Registradas.")
            return
        lista_Categorias = list(self.categorias.values())
        ordenados = self.quick_sort(lista_Categorias)
        print("Categorias ordenados por nombre: ")
        for i, categoria in enumerate(ordenados, start=1):
            print(f"{i}- ID: {categoria.id_categoria} - nombre {categoria.nombre}")


    def Buscar_Categoria(self):
        while True:
            id_buscar = input("Ingrese el codigo de la categoria que desea buscar: ")
            if id_buscar not in self.categorias:
                print("Categoria no encontrada")
                reintentar = input("Presione ENTER para intentar de nuevo o 0 para regresar al menú de Categorias: ")
                if reintentar == "0":
                    break
            categoria = self.categorias.get(id_buscar)
            if categoria:
                print(f"Categoria encontrada: ID: {categoria.id_categoria} / Nombre: {categoria.nombre}")
                intento = input("\n Presione ENTER para agregar otra categoria o ingrese 0 para regresar al menú de categorias: ")
                if intento == "0":
                    break
            else:
                print("Categoria no encontrada.")




class Producto:
    def __init__(self, id_producto, nombre, precio, id_categoria, stock):
        self.id_producto = id_producto
        self.nombre = nombre
        self.precio = precio
        self.id_categoria = id_categoria
        self.stock = stock

class Datos_Productos:
    def __init__(self):
        self.productos = {}

    def sub_menu(self):
        while True:
            print("\n Productos ")
            print("Bienvenido")
            print("1.- Registrar Nuevo Producto.")
            print("2.- Actualizar Producto.")
            print("3.- Eliminar Productos.")
            print("4.- Mostrar Productos.")
            print("5.- Buscar Productos.")
            print("6.- Salir.")
            opcion = int(input("Seleccione que opcion desea: "))
            match opcion:
                case 1:
                    self.Agregar_Producto()
                case 2:
                    print("Actualizar")
                    self.Actualizar_Producto()
                case 3:
                    self.Eliminar_Productos()
                case 4:
                    self.Mostrar_Productos()
                case 5:
                    self.Buscar_Producto()
                case 6:
                    print("Salir...")
                    print("REGRESANDO AL MENÚ PRINCIPAL....")
                    break

    def Agregar_Producto(self):
        print("\n Agregar Producto")
        idp = input("IDProducto: ")
        nombre = input("Nombre producto: ")
        precio = float(input("Precio: Q"))
        idc = input("IDCategoria del producto: ")

        if idc not in datos_categoria.categorias:
            print("Error: La categoría no existe. Agrega primero la categoría.")
        else:
            self.productos[idp] = Producto(idp, nombre, precio, idc, stock=0)
            print("Producto agregado.")


    def Actualizar_Producto(self):
        print("\n Actualizar Producto")
        while True:
            id_Producto = input("Ingrese el ID del producto que desea modificar")
            if id_Producto not in self.productos:
                print("Producto no encontrado")
                reintentar = input("Presione ENTER para intentar de nuevo o 0 para regresar al menú de Productos")
                if reintentar == "0":
                    break
            print("1.- Cambiar Id del Producto")
            print("2.- Cambiar nombre del producto")
            print("3.- Salir")
            actualizar = int(input("Ingrese la opcion que desea."))
            if actualizar == 1:
                nuevo_id = input("Ingrese el nuevo ID: ")
                if nuevo_id in self.productos:
                    print("El ID ya existe en otro producto intente de nuevo")
                    intento = input("Presione ENTER para intentar de nuevo o 0 para regresar al menú de Categorias ")
                    if intento == "0":
                        break
                else:
                     producto = self.productos.pop(id_Producto)
                     producto.id_producto = nuevo_id
                     self.productos[nuevo_id] = producto
                     print("Id producto actualizado Correctamente.")
                     intento = input("Presione ENTER para actualizar otro producto o 3 para regresar al menú de Productos ")
                     if intento == "3":
                        break
            elif actualizar == 2:
                nombre_nuevo = input("Ingrese el nuevo nombre del producto").lower()
                self.productos[id_Producto].nombre = nombre_nuevo
                print("Nombre del Producto actualizado correctamente.")
                intento = input("Presione ENTER para actualizar otro producto o 3 para regresar al menú de Productos ")
                if intento == "3":
                    break
            if actualizar == 3:
                break

    def quick_sort_Productos(self, lista):
        if len(lista) <= 1:
            return lista
        else:
            pivote = lista[0].nombre.lower()
            mayores = [x for x in lista[1:] if x.nombre.lower() > pivote]
            iguales = [x for x in lista[1:] if x.nombre.lower() == pivote]
            menores = [x for x in lista[1:] if x.nombre.lower() < pivote]
            return self.quick_sort_Productos(menores) + [lista[0]] + iguales + self.quick_sort_Productos(mayores)

    def Mostrar_Productos(self):
        if not self.productos:
            print(f"No hay Productos Registrados")
            return
        lista_Productos = list(self.productos.values())
        ordenados = self.quick_sort_Productos(lista_Productos)
        print("Productos ordenados por nombre: ")
        for i, producto in enumerate(ordenados, start=1):
            print(f" ID: {producto.id_producto} / nombre: {producto.nombre}")


    def Eliminar_Productos(self):
        print("\n Eliminar Productos")
        while True:
            id_Producto = input("Ingrese el ID del producto que desea eliminar")
            if id_Producto in self.productos:
                eliminado = self.productos.pop(id_Producto)
                print(f"El producto ha sido eliminado correctamente.")
                reintentar = input("Presione ENTER para intentar de nuevo o 0 para regresar al menú de Productos")
                if reintentar == "0":
                    break
            else:
                intentar = input("Producto no encontrado presione ENTER para intentar de nuevo o 0 para regresar al menú de categorias")
                if intentar == "0":
                    break

    def Buscar_Producto(self):
        while True:
            id_buscar = input("Ingrese el codigo del producto que desea buscar")
            if id_buscar not in self.productos:
                print("Producto no encontrado")
                reintentar = input("Presione ENTER para intentar de nuevo o 0 para regresar al menú de Categorias")
                if reintentar == "0":
                    break
            producto = self.productos.get(id_buscar)
            if producto:
                print(f"Categoria encontrada: ID: {producto.id_producto} / Nombre: {producto.nombre}")
                intento = input("\n Presione ENTER para buscar otro producto o ingrese 0 para regresar al menú de categorias. ")
                if intento == "0":
                    break
            else:
                print("Producto no encontrada.")

class Proveedores:
    def __init__(self, nit, nombre, direccion, telefono, correo, empresa):
        self.nit = nit
        self.nombre = nombre
        self.direccion = direccion
        self.telefono = telefono
        self.correo = correo
        self.empresa = empresa

class Datos_Proveedor:
    def __init__(self):
        self.proveedores = {}

    def sub_menu(self):
        while True:
            print("\n Proveedores ")
            print("Bienvenido")
            print("1.- Registrar Nuevo Proveedor.")
            print("2.- Actualizar Proveedor.")
            print("3.- Eliminar Proveedor.")
            print("4.- Mostrar Proveedor.")
            print("5.- Buscar Proveedor.")
            print("6.- Salir.")
            opcion = int(input("Seleccione que opcion desea: "))
            match opcion:
                case 1:
                    self.Agregar_Proveedor()
                case 2:
                    print("Actualizar")
                    self.Actualizar_Proveedor()
                case 3:
                    self.Eliminar_Productos()
                case 4:
                    self.Mostrar_Productos()
                case 5:
                    self.Buscar_Producto()
                case 6:
                    print("Salir...")
                    print("REGRESANDO AL MENÚ PRINCIPAL....")
                    break
    def Agregar_Proveedor(self):
            print("\n Agregar Proveedor")
            Nit = input("NIT de la Empresa: ")
            nombre = input("Nombre a quien esta el NIT: ")
            direccion = input("Direccion de la empresa: ")
            telefono  = input("Telefono del proveedor: ")
            correo = input("Correo a la empresa: ")
            empresa = input("Nombre de la Empresa: ")
            self.proveedores[Nit] = Proveedores(Nit, nombre, direccion, telefono, correo, empresa)
            print("Proveedor Agregado Correctamente.")

    def Actualizar_Proveedor(self):
        print("\n Actualizar Proovedor")
        while True:
            nit_Proveedor = input("Ingrese el NIT del proveedor que va modificar")
            if nit_Proveedor not in self.proveedores:
                print("Proveedor no encontrado")
                reintentar = input("Presione ENTER para intentar de nuevo o 0 para regresar al menú de Proveedor")
                if reintentar == "0":
                    break
            print("1.- Cambiar Nit del Proveedor")
            print("2.- Cambiar Nombre del Proveedor")
            print("3.- Cambiar Direccion del Proveedor")
            print("4.- Cambiar Telefono del Proveedor")
            print("5.- Cambiar Correo del Proveedor")
            print("6.- Salir")
            actualizar = int(input("Ingrese la opcion que desea."))
            if actualizar == 1:
                nuevo_NIT = input("Ingrese el nuevo NIT: ")
                if nuevo_NIT in self.proveedores:
                    print("El NIT ya existe en otro proveedor intente de nuevo")
                    intento = input("Presione ENTER para intentar de nuevo o 0 para regresar al menú de Proveedores ")
                    if intento == "0":
                        break
                else:
                    NIT = self.proveedores.pop(Nit)
                    NIT. = nuevo_id
                    self.productos[nuevo_id] = producto
                    print("Id producto actualizado Correctamente.")
                    intento = input(
                        "Presione ENTER para actualizar otro producto o 3 para regresar al menú de Productos ")
                    if intento == "3":
                        break
            elif actualizar == 2:
                nombre_nuevo = input("Ingrese el nuevo nombre del Propietario del NIT").lower()
                self.proovedor[n].nombre = nombre_nuevo
                print("Nombre del Propietario actualizado correctamente.")
                intento = input("Presione ENTER para actualizar otro Nombre del Propietario ó 6 para regresar al menú de Productos ")
                if intento == "3":
                    break
            if actualizar == 3:
                direccion_nueva = input("Ingrese la nueva Direccion del Proveedor").lower()
                self.proovedor[nit_Proveedor].direccion = direccion_nueva
                print("Direccion del Propietario actualizado correctamente.")
                intento = input("Presione ENTER para actualizar otra direccion ó 6 para regresar al menú de Productos ")
                if intento == "3":
                    break

        def quick_sort_Productos(self, lista):
            if len(lista) <= 1:
                return lista
            else:
                pivote = lista[0].nombre.lower()
                mayores = [x for x in lista[1:] if x.nombre.lower() > pivote]
                iguales = [x for x in lista[1:] if x.nombre.lower() == pivote]
                menores = [x for x in lista[1:] if x.nombre.lower() < pivote]
                return self.quick_sort_Productos(menores) + [lista[0]] + iguales + self.quick_sort_Productos(mayores)

        def Mostrar_Productos(self):
            if not self.productos:
                print(f"No hay Productos Registrados")
                return
            lista_Productos = list(self.productos.values())
            ordenados = self.quick_sort_Productos(lista_Productos)
            print("Productos ordenados por nombre: ")
            for i, producto in enumerate(ordenados, start=1):
                print(f" ID: {producto.id_producto} / nombre: {producto.nombre}")

        def Eliminar_Productos(self):
            print("\n Eliminar Productos")
            while True:
                id_Producto = input("Ingrese el ID del producto que desea eliminar")
                if id_Producto in self.productos:
                    eliminado = self.productos.pop(id_Producto)
                    print(f"El producto ha sido eliminado correctamente.")
                    reintentar = input("Presione ENTER para intentar de nuevo o 0 para regresar al menú de Productos")
                    if reintentar == "0":
                        break
                else:
                    intentar = input(
                        "Producto no encontrado presione ENTER para intentar de nuevo o 0 para regresar al menú de categorias")
                    if intentar == "0":
                        break

        def Buscar_Producto(self):
            while True:
                id_buscar = input("Ingrese el codigo del producto que desea buscar")
                if id_buscar not in self.productos:
                    print("Producto no encontrado")
                    reintentar = input("Presione ENTER para intentar de nuevo o 0 para regresar al menú de Categorias")
                    if reintentar == "0":
                        break
                producto = self.productos.get(id_buscar)
                if producto:
                    print(f"Categoria encontrada: ID: {producto.id_producto} / Nombre: {producto.nombre}")
                    intento = input(
                        "\n Presione ENTER para buscar otro producto o ingrese 0 para regresar al menú de categorias. ")
                    if intento == "0":
                        break
                else:
                    print("Producto no encontrada.")


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
    match opcion:
            case 1:
                try:
                    datos_categoria.sub_menu()
                except ValueError:
                    validar = input(f"\n Opcion no valida presione ENTER para intentar de nuevo o 6 para Salir del programa")
                    if validar == "6":
                        break
            case 2:
                try:
                    Datos_Productos().sub_menu()
                except ValueError:
                    validar = input(f"\n Opcion no valida presione ENTER para intentar de nuevo o 6 para Salir del programa")
                    if validar == "6":
                        break
            case 4:
                try:
                    Datos_Proveedor().sub_menu()
                except ValueError:
                    validar = input(f"\n Opcion no valida presione ENTER para intentar de nuevo o 6 para Salir del programa")
                    if validar == "6":
                        break

            case 6:
                print("Saliendo...")
                break
