class Categoria:
    def __init__(self, id_categoria, nombre):
        self.id_categoria = id_categoria
        self.nombre = nombre

class Datos_Categoria:
    def __init__(self):
        self.categorias = {}
        self.cargar_categorias()
    def cargar_categorias(self):
        try:
            with open("categorias.txt", "r", encoding="utf-8") as archivo:
                for linea in archivo:
                    linea = linea.strip()
                    if linea:
                        id_categoria, nombre = linea.split(":")
                        self.categorias[id_categoria] = Categoria(id_categoria, nombre)

            print("Categorias importadas desde catetorias.txt")
        except FileNotFoundError:
            print("No existe el archivo categorias.txt, se creará uno nuevo al guardar.")
    def guardar_categorias(self):
        with open("categorias.txt", "w", encoding="utf-8") as archivo:
            for categoria in self.categorias.values():
                archivo.write(f"{categoria.id_categoria}:{categoria.nombre}\n")

    def sub_menu(self):
        while True:
            print("\n --Bienvenido--")
            print(" **** CATEGORIAS ****")
            print("1.- Registrar Nueva Categoria.")
            print("2.- Actualizar Categoria.")
            print("3.- Eliminar Categoria.")
            print("4.- Mostrar Categoria.")
            print("5.- Buscar Categoria.")
            print("6.- Salir Menú Categoria.")
            opcion = int(input("Seleccione la opción desea: "))
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
                    print("REGRESANDO AL MENÚ PRINCIPAL.... \n")
                    break
    def Agregar_Categoria(self):
        print("\n **** Registrar Categoria ****")
        while True:
            try:
                Id_Categoria = input("Ingrese el Id de la nueva categoria: ")
                if Id_Categoria in self.categorias:
                    print("La Categoria ya existe.")
                    error = input("Presione ENTER para intentar de nuevo o 0 para salir: ")
                    if error == "0":
                        print("SALIENDO AL MENU CATEGORIAS...")
                        break
                    else:
                        continue
                Nombre_Categoria = input("Ingrese el nombre de la categoria: ").lower()
                self.categorias[Id_Categoria] = Categoria(Id_Categoria, Nombre_Categoria)
                self.guardar_categorias()
                print("Categoría registrada correctamente.")
                intento = input("Presione ENTER para agregar otra categoria o ingrese 0 para regresar al menú de categorias: ")
                if intento == "0":
                    print("SALIENDO AL MENU CATEGORIAS...")
                    break
            except ValueError:
                print("No se puede agregar una categoría")
    def Actualizar_Categoria(self):
        print("\n **** Actualizar Categoria ****")
        while True:
            id_Categoria = input("Ingrese el ID de la categoria que desea modificar: ")
            if id_Categoria not in self.categorias:
                print("Categoria no encontrada.")
                reintentar = input("Presione ENTER para intentar de nuevo o 0 para regresar al menú de Categorias: ")
                if reintentar == "0":
                    print("SALIENDO AL MENU CATEGORIAS...")
                    break
                else:
                    continue
            nombre_nuevo = input("Ingrese el nuevo nombre de la categoria: ").lower()
            self.categorias[id_Categoria].nombre = nombre_nuevo
            self.guardar_categorias()
            print("Categoria actualizada correctamente.")
            intento = input("Presione ENTER para actualizar otra Categoria o 0 para regresar al menú de Categorias: ")
            if intento == "0":
                print("SALIENDO AL MENU CATEGORIAS...")
                break
    def Eliminar_Categoria(self):
        print("\n **** Eliminar Categoria ****")
        while True:
            id_Categoria = input("Ingrese el ID de la categoria que desea eliminar: ")
            if id_Categoria in self.categorias:
                eliminado = self.categorias.pop(id_Categoria)
                self.guardar_categorias()
                print(f"La categoria ha sido eliminado correctamente.")
                reintentar = input("Presione ENTER para Eliminar otra categoria o 0 para regresar al menú de Categorias: ")
                if reintentar == "0":
                    print("SALIENDO AL MENU CATEGORIAS...")
                    break
            else:
                intentar = input("Categoria no encontrada presione ENTER para intentar de nuevo o 0 para regresar al menú de categorias: ")
                if intentar == "0":
                    print("SALIENDO AL MENU CATEGORIAS...")
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
        while True:
            print("\n **** Mostrar Categoria ****")
            if not self.categorias:
                print(f"No hay Categorias Registradas.")
                return
            lista_Categorias = list(self.categorias.values())
            ordenados = self.quick_sort(lista_Categorias)
            print("Categorias ordenados por nombre: ")
            for i, categoria in enumerate(ordenados, start=1):
                print(f"{i}- ID: {categoria.id_categoria} - nombre {categoria.nombre}")
            reintentar = input("Presione ENTER para regresar al menú de Categorias")
            if reintentar == "6":
                print("SALIENDO AL MENU CATEGORIAS...")
                break
    def Buscar_Categoria(self):
        print("\n **** Buscar Categoria ****")
        while True:
            id_buscar = input("Ingrese el codigo de la categoria que desea buscar: ")
            if id_buscar not in self.categorias:
                print("Categoria no encontrada")
                reintentar = input("Presione ENTER para intentar de nuevo o 0 para regresar al menú de Categorias: ")
                if reintentar == "0":
                    print("SALIENDO AL MENU CATEGORIAS...")
                    break
            categoria = self.categorias.get(id_buscar)
            if categoria:
                print(f"Categoria encontrada: ")
                print(f"ID: {categoria.id_categoria} / Nombre: {categoria.nombre}")
                intento = input("\n Presione ENTER para buscar otra categoria o ingrese 0 para regresar al menú de categorias: ")
                if intento == "0":
                    print("SALIENDO AL MENU CATEGORIAS...")
                    break
            else:
                print("Categoria no encontrada.")

class Producto:
    def __init__(self, id_producto, nombre, precio, id_categoria, stock=0):
        self.id_producto = id_producto
        self.nombre = nombre
        self.precio = precio
        self.id_categoria = id_categoria
        self.stock = stock

class Datos_Productos:
    def __init__(self):
        self.productos = {}
        self.cargar_productos()

    def cargar_productos(self):
        try:
            with open("productos.txt", "r", encoding="utf-8") as archivo:
                for linea in archivo:
                    linea = linea.strip()
                    if linea:
                        id_producto, nombre, precio, id_categoria, stock = linea.split(":")
                        self.productos[id_producto] = Producto(id_producto, nombre, precio, id_categoria, stock)

            print("Productos importados desde productos.txt")
        except FileNotFoundError:
            print("No existe el archivo productos.txt, se creará uno nuevo al guardar.")

    def guardar_productos(self):
        with open("productos.txt", "w", encoding="utf-8") as archivo:
            for productos in self.productos.values():
                archivo.write(f"{productos.id_producto}:{productos.nombre}:{productos.precio}:{productos.id_categoria}:{productos.stock}\n")

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
        print("\n **** Crear codigo del Producto ****")
        while True:
            idp = input("ID del producto: ")
            if idp in self.productos:
                print("Error: Ya existe un producto con ese ID.")
                reintentar = input("Presione ENTER para intentar de nuevo o 0 para regresar al menú de Productos: ")
                if reintentar == "0":
                    print("SALIENDO AL MENU PRODUCTOS...")
                    return
                else:
                    continue
            else:
                nombre = input("Nombre producto: ")
                precio = float(input("Precio estimado: Q"))
                idc = input("IDCategoria del producto: ")
                stock = 0
                if idc not in datos_categoria.categorias:
                    print("Error: La categoría no existe. Agrega primero la categoría.")
                    print("SALIENDO AL MENU PRODUCTOS....")
                    break
                else:
                    self.productos[idp] = Producto(idp, nombre, precio, idc, stock)
                    self.guardar_productos()
                    print("Producto agregado Correctamente.")
                reintentar = input("Presione ENTER para agregar otro producto o 0 para regresar al menú de Productos: ")
                if reintentar == "0":
                    print("SALIENDO AL MENU PRODUCTOS...")
                    return
                else:
                    continue
    def Actualizar_Producto(self):
        print("\n **** Actualizar Producto ****")
        while True:
            id_Producto = input("Ingrese el ID del producto que desea modificar: ")
            if id_Producto not in self.productos:
                print("Producto no encontrado")
                reintentar = input("Presione ENTER para intentar de nuevo o 0 para regresar al menú de Productos: ")
                if reintentar == "0":
                    print("SALIENDO AL MENU PRODUCTOS...")
                    break
            print("1.- Cambiar Id del Producto")
            print("2.- Cambiar nombre del producto")
            print("3.- Salir")
            actualizar = int(input("Ingrese la opcion que desea: "))
            if actualizar == 1:
                nuevo_id = input("Ingrese el nuevo ID: ")
                if nuevo_id in self.productos:
                    print("El ID ya existe en otro producto intente de nuevo")
                    intento = input("Presione ENTER para intentar de nuevo o 0 para regresar al menú de Productos: ")
                    if intento == "0":
                        print("SALIENDO AL MENU PRODUCTOS...")
                        break
                else:
                     producto = self.productos.pop(id_Producto)
                     producto.id_producto = nuevo_id
                     self.productos[nuevo_id] = producto
                     self.guardar_productos()
                     print("Id producto actualizado Correctamente.")
                     intento = input("Presione ENTER para actualizar otro producto o 3 para regresar al menú de Productos: ")
                     if intento == "3":
                        print("SALIENDO AL MENU PRODUCTOS...")
                        break
            elif actualizar == 2:
                nombre_nuevo = input("Ingrese el nuevo nombre del producto: ").lower()
                self.productos[id_Producto].nombre = nombre_nuevo
                self.guardar_productos()
                print("Nombre del Producto actualizado correctamente.")
                intento = input("Presione ENTER para actualizar otro producto o 3 para regresar al menú de Productos: ")
                if intento == "3":
                    print("SALIENDO AL MENU PRODUCTOS...")
                    break
            if actualizar == 3:
                print("Regresando al menú Productos")
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
        while True:
            print("\n **** Mostrar Productos ****")
            if not self.productos:
                print(f"No hay Productos Registrados")
                reintentar = input("Presione ENTER para intentar de nuevo o 0 para regresar al menú de Productos: ")
                if reintentar == "0":
                    print("SALIENDO AL MENU PRODUCTOS...")
                    break
                return
            lista_Productos = list(self.productos.values())
            ordenados = self.quick_sort_Productos(lista_Productos)
            print("Productos ordenados por nombre: ")
            for i, producto in enumerate(ordenados, start=1):
                print(f" ID: {producto.id_producto} / nombre: {producto.nombre}")
            reintentar = input("Presione ENTER para regresar al menú de Productos")
            if reintentar == "6":
                print("SALIENDO AL MENU PRODUCTOS...")
    def Eliminar_Productos(self):
        print("\n **** Eliminar Productos ****")
        while True:
            id_Producto = input("Ingrese el ID del producto que desea eliminar: ")
            if id_Producto in self.productos:
                eliminado = self.productos.pop(id_Producto)
                self.guardar_productos()
                print(f"El producto ha sido eliminado correctamente.")
                reintentar = input("Presione ENTER para intentar de nuevo o 3 para regresar al menú de Productos")
                if reintentar == "3":
                    print("SALIENDO AL MENU PRODUCTOS...")
                    break
            else:
                intentar = input("Producto no encontrado presione ENTER para intentar de nuevo o 0 para regresar al menú de categorias")
                if intentar == "0":
                    print("SALIENDO AL MENU PRODUCTOS...")
                    break
    def Buscar_Producto(self):
        print("\n **** Buscar Producto ****")
        while True:
            id_buscar = input("Ingrese el ID del producto que desea buscar: ")
            if id_buscar not in self.productos:
                print("Producto no encontrado")
                reintentar = input("Presione ENTER para intentar de nuevo o 0 para regresar al menú de Productos: ")
                if reintentar == "0":
                    print("SALIENDO AL MENU PRODUCTOS...")
                    break
            producto = self.productos.get(id_buscar)
            if producto:
                print(f"Producto encontrado: ID: {producto.id_producto} / Nombre: {producto.nombre}")
                intento = input("\n Presione ENTER para buscar otro producto o ingrese 3 para regresar al menú de Productos: ")
                if intento == "3":
                    print("SALIENDO AL MENU PRODUCTOS...")
                    break
            else:
                print("Producto no encontrado.")

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
        self.cargar_proveedor()

    def cargar_proveedor(self):
        try:
            with open("proveedor.txt", "r", encoding="utf-8") as archivo:
                for linea in archivo:
                    linea = linea.strip()
                    if linea:
                        nit, nombre, direccion, telefono, correo, empresa = linea.split(":")
                        self.proveedores[nit] = Proveedores(nit, nombre, direccion, telefono, correo, empresa)

            print("Proveedores importados desde proveedor.txt")
        except FileNotFoundError:
            print("No existe el archivo proveedor.txt, se creará uno nuevo al guardar.")
    def guardar_proveedores(self):
        with (open("proveedor.txt", "w", encoding="utf-8") as archivo):
            for proveedor in self.proveedores.values():
                archivo.write(f"{proveedor.nit}:{proveedor.nombre}:{proveedor.direccion}:{proveedor.telefono}:{proveedor.correo}:{proveedor.empresa}\n")
    def sub_menu(self):
        while True:
            print("\n --Bienvenido--")
            print(" **** PROVEEDORES ****")
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
                    self.Actualizar_Proveedor()
                case 3:
                    self.Eliminar_Proveedor()
                case 4:
                    self.Mostrar_Proveedor()
                case 5:
                    self.Buscar_Proveedor()
                case 6:
                    print("Salir...")
                    print("REGRESANDO AL MENÚ PRINCIPAL....")
                    break
    def Agregar_Proveedor(self):
        while True:
            print("\n **** Agregar Proveedor ****")
            Nit = input("NIT del Proveedor/Empresa: ")
            nombre = input("Ingrese el NIT Proveedor/Empresa: ")
            direccion = input("Direccion del Proveedor/Empresa: ")
            telefono  = input("Telefono del Proveedor/Empresa: ")
            correo = input("Correo del Proveedor/Empresa: ")
            empresa = input("Nombre de la Empresa: ")
            self.proveedores[Nit] = Proveedores(Nit, nombre, direccion, telefono, correo, empresa)
            self.guardar_proveedores()
            print("Proveedor/Empresa Agregado Correctamente.")
            reintentar = input("Presione ENTER para agregar otro Proveedor/Empresa o 0 para regresar al menú de Proveedores: ")
            if reintentar == "0":
                print("SALIENDO AL MENU PROVEEDORES...")
                return
            else:
                continue
    def Actualizar_Proveedor(self):
        print("\n **** Actualizar Proovedor ****")
        while True:
            nit_Proveedor = input("Ingrese el NIT del proveedor que va modificar: ")
            if nit_Proveedor not in self.proveedores:
                print("Proveedor no encontrado")
                reintentar = input("Presione ENTER para intentar de nuevo o 0 para regresar al menú de Proveedor")
                if reintentar == "0":
                    print("SALIENDO AL MENU PROVEEDOR...")
                    break
            print("\n **** Actualizar Proovedor/Empresa ****")
            print("1.- Cambiar Nit del Proveedor/Empresa")
            print("2.- Cambiar Nombre del Proveedor/Empresa")
            print("3.- Cambiar Direccion del Proveedor/Empresa")
            print("4.- Cambiar Telefono del Proveedor/Empresa")
            print("5.- Cambiar Correo del Proveedor/Empresa")
            print("6.- Salir")
            actualizar = int(input("Ingrese la opcion que desea: "))
            if actualizar == 1:
                nuevo_NIT = input("Ingrese el nuevo NIT: ")
                if nuevo_NIT in self.proveedores:
                    print("El NIT ya existe en otro Proveedor/Empresa intente de nuevo")
                    intento = input("Presione ENTER para intentar de nuevo o 6 para regresar al menú de Proveedores: ")
                    if intento == "0":
                        print("SALIENDO AL MENU PROVEEDOR...")
                        break
                else:
                    NIT = self.proveedores.pop(nit_Proveedor)
                    NIT.nit = nuevo_NIT
                    self.proveedores[nuevo_NIT] = NIT
                    self.guardar_proveedores()
                    print("NIT Proveedor actualizado Correctamente.")
                    intento = input("Presione ENTER para actualizar otro Proveedor o 6 para regresar al menú de Proveedores: ")
                    if intento == "6":
                        print("SALIENDO AL MENU PROVEEDOR...")
                        break
            elif actualizar == 2:
                nombre_nuevo = input("Ingrese el nuevo nombre del propietario: ").lower()
                self.proveedores[nit_Proveedor].nombre = nombre_nuevo
                self.guardar_proveedores()
                print("Nombre del Propietario actualizado correctamente.")
                intento = input("Presione ENTER para actualizar otro Proveedor o 6 para regresar al menú de Proveedores: ")
                if intento == "6":
                    print("SALIENDO AL MENU PROVEEDOR...")
                    break
            elif actualizar == 3:
                direccion_nuevo = input("Ingrese la nueva direccion del proveedor: ").lower()
                self.proveedores[nit_Proveedor].direccion = direccion_nuevo
                self.guardar_proveedores()
                print("Direccion del Proveedor actualizado Correctamente.")
                intento = input("Presione ENTER para actualizar otro Proveedor o 6 para regresar al menú de Proveedores: ")
                if intento == "6":
                    print("SALIENDO AL MENU PROVEEDOR...")
                    break
            elif actualizar == 4:
                telefono_nuevo = input("Ingrese el nuevo telefono del Proveedor: ").lower()
                self.proveedores[nit_Proveedor].telefono = telefono_nuevo
                self.guardar_proveedores()
                print("Telefono del Proveedor actualizado Correctamente.")
                intento = input("Presione ENTER para actualizar otro Proveedor o 6 para regresar al menú de Proveedores: ")
                if intento == "6":
                    break
            elif actualizar == 5:
                correo_nuevo = input("Ingrese el nuevo correo del proveedor: ").lower()
                self.proveedores[nit_Proveedor].correo = correo_nuevo
                self.guardar_proveedores()
                print("Correo del proveedor actualizado Correctamente.")
                intento = input("Presione ENTER para actualizar otro Proveedor o 6 para regresar al menú de Proveedores: ")
                if intento == "6":
                    print("SALIENDO AL MENU PROVEEDOR...")
                    break
            elif actualizar == 6:
                print("Regresando al menú de Proveedor...")
                break
    def quick_sort_Proveedores(self, lista):
        if len(lista) <= 1:
            return lista
        else:
            pivote = lista[0].nombre.lower()
            mayores = [x for x in lista[1:] if x.nombre.lower() > pivote]
            iguales = [x for x in lista[1:] if x.nombre.lower() == pivote]
            menores = [x for x in lista[1:] if x.nombre.lower() < pivote]
            return self.quick_sort_Proveedores(menores) + [lista[0]] + iguales + self.quick_sort_Proveedores(mayores)
    def Mostrar_Proveedor(self):
        print("\n **** Mostrar Proveedor **** ")
        if not self.proveedores:
            print(f"No hay Proveedores Registrados.")
            return
        lista_Proveedores = list(self.proveedores.values())
        ordenados = self.quick_sort_Proveedores(lista_Proveedores)
        print("Proveedores ordenados por nombre: ")
        for i, proveedores in enumerate(ordenados, start=1):
            print(f"Empresa: {proveedores.empresa}")
            print(f"NIT: {proveedores.nit}")
            print(f"Nombre Propietario: {proveedores.nombre}")
            print(f"Direccion: {proveedores.direccion}")
            reintentar = input("Presione ENTER para regresar al menú de Proveedores")
            if reintentar == "6":
                break
    def Eliminar_Proveedor(self):
        print("\n **** Eliminar Proveedor ****")
        while True:
            Nit_Proveedor = input("Ingrese el NIT del proovedor que desea eliminar: ")
            if Nit_Proveedor in self.proveedores:
                eliminado = self.proveedores.pop(Nit_Proveedor)
                self.guardar_proveedores()
                print(f"El Proveedor {Nit_Proveedor} ha sido eliminado correctamente.")
                reintentar = input("Presione ENTER para intentar de nuevo o 6 para regresar al menú de Proveedores: ")
                if reintentar == "6":
                    break
            else:
                intentar = input("Proveedor no encontrado presione ENTER para intentar de nuevo o 6 para regresar al menú de Proveedores: ")
                if intentar == "6":
                    break
    def Buscar_Proveedor(self):
        print("\n **** Buscar Proveedor ****")
        while True:
            Nit_buscar = input("Ingrese el NIT del proveedor que desea buscar: ")
            if Nit_buscar not in self.proveedores:
                print("Proveedor no encontrado")
                reintentar = input("Presione ENTER para intentar de nuevo o 6 para regresar al menú de Proveedores: ")
                if reintentar == "6":
                    break
            proveedor = self.proveedores.get(Nit_buscar)
            if proveedor:
                print(f"Proveedor encontrado:")
                print(f"Empresa: {proveedor.empresa}")
                print(f"NIT: {proveedor.nit}")
                print(f"Nombre: {proveedor.nombre}")
                print(f"Direccion: {proveedor.direccion}")
                intento = input("\n Presione ENTER para buscar otro proveedor o ingrese 6 para regresar al menú de Proveedores: ")
                if intento == "6":
                    break
            else:
                print("Proveedor no encontrado.")

class Empleado:
    def __init__(self, id_Empleado, nombre, direccion, telefono, correo, puesto):
        self.id_Empleado = id_Empleado
        self.nombre = nombre
        self.direccion = direccion
        self.telefono = telefono
        self.correo = correo
        self.puesto = puesto
class Datos_Empleados:
    def __init__(self):
        self.empleados = {}
        self.cargar_empleado()
    def cargar_empleado(self):
        try:
            with open("empleados.txt", "r", encoding="utf-8") as archivo:
                for linea in archivo:
                    linea = linea.strip()
                    if linea:
                        id_Empleado, nombre, direccion, telefono, correo, puesto = linea.split(":")
                        self.empleados[id_Empleado] = Empleado(id_Empleado, nombre, direccion, telefono, correo, puesto)
            print("Empleados importados desde empleados.txt")
        except FileNotFoundError:
            print("No existe el archivo empleados.txt, se creará uno nuevo al guardar.")

    def guardar_empleados(self):
        with (open("empleados.txt", "w", encoding="utf-8") as archivo):
            for empleados in self.empleados.values():
                archivo.write(
                    f"{empleados.id_Empleado}: {empleados.nombre}: {empleados.direccion}: {empleados.telefono}: {empleados.correo}: {empleados.puesto}\n")
    def sub_menu(self):
        while True:
            print("\n --Bienvenido--")
            print(" **** EMPLEADOS ****")
            print("1.- Registrar Nuevo Empleado.")
            print("2.- Actualizar Empleado.")
            print("3.- Eliminar Empleado.")
            print("4.- Mostrar Empleado.")
            print("5.- Buscar Empleado.")
            print("6.- Salir.")
            opcion = int(input("Seleccione que opcion desea: "))
            match opcion:
                case 1:
                    self.Agregar_Empleado()
                case 2:
                    self.Actualizar_Empleado()
                case 3:
                    self.Eliminar_Empleado()
                case 4:
                    self.Mostrar_Empleados()
                case 5:
                    self.Buscar_Empleado()
                case 6:
                    print("Salir...")
                    print("REGRESANDO AL MENÚ PRINCIPAL....")
                    break
    def Agregar_Empleado(self):
        while True:
            print("\n **** Agregar un Nuevo Empleado ****")
            id_empleado = input("Ingrese cual sera el ID del Empleado: ")
            nombre = input("Nombre del Nuevo Empleado: ")
            direccion = input("Direccion del Nuevo Empleado: ")
            telefono = input("Telefono del Empleado: ")
            correo = input("Correo del Empleado: ")
            puesto = input("Puesto del Empleado: ")
            self.empleados[id_empleado] = Empleado(id_empleado, nombre, direccion, telefono, correo, puesto)
            self.guardar_empleados()
            print("Empleado Agregado Correctamente.")
            reintentar = input("Presione ENTER para agregar otro Empleado o 0 para regresar al menú de Empleado: ")
            if reintentar == "0":
                print("SALIENDO AL MENU EMPLEADO...")
                return
            else:
                continue
    def Actualizar_Empleado(self):
        print("\n **** Actualizar Empleado ****")
        while True:
            id_Empleado = input("Ingrese el Id del empleado que va modificar: ")
            if id_Empleado not in self.empleados:
                print("Empleado no encontrado")
                reintentar = input("Presione ENTER para intentar de nuevo o 0 para regresar al menú de Empleados")
                if reintentar == "0":
                    print("SALIENDO AL MENU EMPLEADO...")
                    break
            print("1.- Cambiar Direccion del Empleado")
            print("2.- Cambiar Telefono del Empleado")
            print("3.- Cambiar Correo del Empleado")
            print("4.- Cambiar Puesto del Empleado")
            print("5.- Salir")
            actualizar = int(input("Ingrese la opcion que desea: "))
            if actualizar == 1:
                direccion_nueva = input("Ingrese la nueva direccion del Empleado: ").lower()
                self.empleados[id_Empleado].direccion = direccion_nueva
                self.guardar_empleados()
                print("Direccion del Empleado actualizada Correctamente.")
                intento = input("Presione ENTER para actualizar otro dato de algún empleado o 5 para regresar al menú de Empleados: ")
                if intento == "5":
                    print("SALIENDO AL MENU EMPLEADO...")
                    break
            elif actualizar == 2:
                telefono_nuevo = input("Ingrese el Nuevo Telefono del Empleado: ")
                self.empleados[id_Empleado].telefono = telefono_nuevo
                self.guardar_empleados()
                print("Telefono del Empleado actualizado Correctamente.")
                intento = input("Presione Enter para actualizar otro dato de algún empleado ó 5 para regresar al menú de Empleados: ")
                if intento == "5":
                    print("SALIENDO AL MENU EMPLEADO...")
                    break
            elif actualizar == 3:
                correo_nuevo = input("Ingrese el Nuevo Correo del Empleado: ")
                self.empleados[id_Empleado].correo = correo_nuevo
                self.guardar_empleados()
                print("Correo del Empleado actualizado Correctamente.")
                intento = input("Presione ENTER para actualizar otro dato de algún empleado ó 5 para regresar al menú de Empleados: ")
                if intento == "5":
                    print("SALIENDO AL MENU EMPLEADO...")
                    break
            elif actualizar == 4:
                puesto_nuevo = input("Ingrese el Nuevo Puesto: ")
                self.empleados[id_Empleado].puesto = puesto_nuevo
                self.guardar_empleados()
                print("Puesto del Empleado actualizado Correctamente.")
                intento = input("Presione ENTER para actualizar otro dato de algún empleado ó 5 para regresar al menú de Empleados: ")
                if intento == "5":
                    print("SALIENDO AL MENU EMPLEADO...")
                    break
            elif actualizar == 5:
                print("Regresando al menú de Proveedor...")
                break
    def Eliminar_Empleado(self):
        print("\n **** Eliminar Empleado ****")
        while True:
            id_empleado = input("Ingrese el ID del Empleado que deseea Eliminar: ")
            if id_empleado in self.empleados:
                eliminado = self.empleados.pop(id_empleado)
                self.guardar_empleados()
                print(f"Empleado eliminado correctamente.")
                reintentar = input("Presione ENTER para intentar de nuevo o 5 para regresar al menú de Empleados: ")
                if reintentar == "5":
                    print("SALIENDO AL MENU EMPLEADO...")
                    break
            else:
                intentar = input("Empleado no encontrado presione ENTER para intentar de nuevo o 5 para regresar al menú de Empleados")
                if intentar == "5":
                    print("SALIENDO AL MENU EMPLEADO...")
                    break
    def quick_sort_Empleados(self, lista):
        if len(lista) <= 1:
            return lista
        else:
            pivote = lista[0].nombre.lower()
            mayores = [x for x in lista[1:] if x.nombre.lower() > pivote]
            iguales = [x for x in lista[1:] if x.nombre.lower() == pivote]
            menores = [x for x in lista[1:] if x.nombre.lower() < pivote]
            return self.quick_sort_Empleados(menores) + [lista[0]] + iguales + self.quick_sort_Empleados(mayores)
    def Mostrar_Empleados(self):
        print(" \n **** Mostrar Empleados ****")
        if not self.empleados:
            print(f"No hay Empleados Registrados")
            return
        lista_Empleados = list(self.empleados.values())
        ordenados = self.quick_sort_Empleados(lista_Empleados)
        print("Empleados ordenados por nombre: ")
        for i, empleados in enumerate(ordenados, start=1):
            print(f"Nombre: {empleados.nombre}")
            print(f"Telefono:  {empleados.telefono}")
            print(f"Direccion: {empleados.direccion}")
            print(f"Puesto: {empleados.puesto}")
    def Buscar_Empleado(self):
        print( "\n **** Buscar Empleado ****")
        while True:
            id_buscar = input("Ingrese el Id del empleado que desea buscar: ")
            if id_buscar not in self.empleados:
                print("Empleado no encontrado")
                reintentar = input("Presione ENTER para intentar de nuevo o 5 para regresar al menú de Empleados")
                if reintentar == "5":
                    print("SALIENDO AL MENU EMPLEADO...")
                    break
            empleado = self.empleados.get(id_buscar)
            if empleado:
                print(f"Empleado encontrado:")
                print(f"Nombre: {empleado.nombre}")
                print(f"Direccion: {empleado.direccion}")
                print(f"Telefono: {empleado.telefono}")
                print(f"Correo Electronico: {empleado.correo}")
                print(f"Puesto: {empleado.puesto}")
                intento = input("\n Presione ENTER para buscar otro proveedor o ingrese 5 para regresar al menú de Empleados. ")
                if intento == "5":
                    print("SALIENDO AL MENU EMPLEADO...")
                    break
            else:
                print("Empleado no encontrado.")

class Cliente:
    def __init__(self, nit_cliente, nombre, direccion, telefono, correo):
        self.nit_cliente = nit_cliente
        self.nombre = nombre
        self.direccion = direccion
        self.telefono = telefono
        self.correo = correo

class Datos_Cliente:
    def __init__(self):
        self.clientes = {}
        self.cargar_clientes()

    def cargar_clientes(self):
        try:
            with open("clientes.txt", "r", encoding="utf-8") as archivo:
                for linea in archivo:
                    linea = linea.strip()
                    if linea:
                        nit_cliente, nombre, direccion, telefono, correo = linea.split(":")
                        self.clientes[nit_cliente] = Cliente(nit_cliente, nombre, direccion, telefono, correo)
            print("Productos importados desde clientes.txt")
        except FileNotFoundError:
            print("No existe el archivo clientes.txt, se creará uno nuevo al guardar.")
    def guardar_clientes(self):
        with open("clientes.txt", "w", encoding="utf-8") as archivo:
            for clientes in self.clientes.values():
                archivo.write(f"{clientes.nit_cliente} : {clientes.nombre}: {clientes.direccion}:{clientes.telefono} : {clientes.correo}\n")
    def sub_menu(self):
        while True:
            print("\n --Bienvenido--")
            print(" **** CLIENTES ****")
            print("1.- Registrar Nuevo Cliente.")
            print("2.- Actualizar Datos Cliente.")
            print("3.- Mostrar Clientes.")
            print("4.- Buscar Clientes.")
            print("5.- Salir.")
            opcion = int(input("Seleccione que opcion desea: "))
            match opcion:
                case 1:
                    self.Agregar_Cliente()
                case 2:
                    self.Actualizar_Cliente()
                case 3:
                    self.Mostrar_Cliente()
                case 4:
                    self.Buscar_Cliente()
                case 5:
                    print("Salir...")
                    print("REGRESANDO AL MENÚ PRINCIPAL....")
                    break
    def Agregar_Cliente(self):
        print("\n **** Agregar un Nuevo Cliente ****")
        while True:
            nit_cliente = input("Ingrese el NIT del cliente: ")
            nombre = input("Nombre del Cliente: ")
            direccion = input("Direccion del Cliente: ")
            telefono = input("Telefono del Cliente: ")
            correo = input("Correo del Cliente: ")
            self.clientes[nit_cliente] = Cliente(nit_cliente, nombre, direccion, telefono, correo)
            self.guardar_clientes()
            print("Cliente Agregado Correctamente.")
            reintentar = input("Presione ENTER para agregar otro Cliente o 0 para regresar al menú de Clientes: ")
            if reintentar == "0":
                print("SALIENDO AL MENU CLIENTES...")
                return
            else:
                continue
    def Actualizar_Cliente(self):
        print("\n **** Actualizar Cliente ****")
        while True:
            Nit_cliente = input("Ingrese el NIT del cliente que va modificar: ")
            if Nit_cliente not in self.clientes:
                print("Cliente no encontrado")
                reintentar = input("Presione ENTER para intentar de nuevo o 0 para regresar al menú de Clientes")
                if reintentar == "0":
                    print("SALIENDO AL MENU CLIENTES...")
                    break
            print("\n **** Actualizar Cliente ****")
            print("1.- Cambiar Telefono del Cliente")
            print("2.- Cambiar Correo del Cliente")
            print("3.- Salir")
            actualizar = int(input("Ingrese la opcion que desea: "))
            if actualizar == 1:
                telefono_nuevo = input("Ingrese el nuevo telefono del cliente: ")
                self.clientes[Nit_cliente].telefono = telefono_nuevo
                self.guardar_clientes()
                print("Telefono del Empleado actualizada Correctamente.")
                intento = input("Presione ENTER para actualizar otro dato de algún empleado o 3 para regresar al menú de Clientes: ")
                if intento == "3":
                    print("SALIENDO AL MENU CLIENTES...")
                    break
            elif actualizar == 2:
                correo_nuevo = input("Ingrese el Nuevo Correo del Cliente: ")
                self.clientes[Nit_cliente].correo = correo_nuevo
                self.guardar_clientes()
                print("Correo del Cliente actualizado Correctamente.")
                intento = input("Presione ENTER para actualizar otro dato de algún empleado ó 3 para regresar al menú de Empleados: ")
                if intento == "3":
                    print("SALIENDO AL MENU CLIENTES...")
                    break
            elif actualizar == 3:
                print("Regresando al menú de Proveedor...")
                break
    def quick_sort_Clientes(self, lista):
        if len(lista) <= 1:
            return lista
        else:
            pivote = lista[0].nombre.lower()
            mayores = [x for x in lista[1:] if x.nombre.lower() > pivote]
            iguales = [x for x in lista[1:] if x.nombre.lower() == pivote]
            menores = [x for x in lista[1:] if x.nombre.lower() < pivote]
            return self.quick_sort_Clientes(menores) + [lista[0]] + iguales + self.quick_sort_Clientes(mayores)
    def Mostrar_Cliente(self):
        print("\n **** Mostrar Clientes ****")
        while True:
            if not self.clientes:
                print(f"No hay Clientes Registrados")
                return
            lista_Clientes = list(self.clientes.values())
            ordenados = self.quick_sort_Clientes(lista_Clientes)
            print("Clientes ordenados por nombre: ")
            for i, clientes in enumerate(ordenados, start=1):
                print(f"NIT: {clientes.nit_cliente}")
                print(f"Nombre: {clientes.nombre}")
                print(f"Direccion: {clientes.direccion}")
                print(f"Telefono:  {clientes.telefono}")
                print(f"Correo Electronico: {clientes.correo}")
            reintentar = input("Presione ENTER para regresar al menú de Clientes: ")
            if reintentar == "":
                print("SALIENDO AL MENU CLIENTES...")
                return
            else:
                continue
    def Buscar_Cliente(self):
        print("\n **** Buscar Clientes ****")
        while True:
            nit_buscar = input("Ingrese el NIT del Cliente que desea buscar: ")
            if nit_buscar not in self.clientes:
                print("Cliente no encontrado")
                reintentar = input("Presione ENTER para intentar de nuevo o 5 para regresar al menú de Empleados")
                if reintentar == "5":
                    print("SALIENDO AL MENU CLIENTES...")
                    break
            cliente = self.clientes.get(nit_buscar)
            if cliente:
                print(f"Cliente encontrado:")
                print(f"NIT: {cliente.nit_cliente}")
                print(f"Nombre: {cliente.nombre}")
                print(f"Direccion: {cliente.direccion}")
                print(f"Telefono:  {cliente.telefono}")
                print(f"Correo Electronico: {cliente.correo}")
                intento = input("\n Presione ENTER para buscar otro Cliente o ingrese 5 para regresar al menú de Clientes. ")
                if intento == "5":
                    print("SALIENDO AL MENU CLIENTES...")
                    break
            else:
                print("Cliente no encontrado.")

class Compras:
    def __init__(self, id_compra, id_producto, cantidad, sub_total,total):
        self.id_compra = id_compra
        self.id_producto = id_producto
        self.cantidad = cantidad
        self.sub_total = sub_total
        self.total = total

class Datos_Compra:
    def __init__(self, datos_productos):
        self.compras = {}
        self.datos_productos = datos_productos
        self.cargar_Compras()

    def cargar_Compras(self):
        try:
            with open("compras.txt", "r", encoding="utf-8") as archivo:
                for linea in archivo:
                    linea = linea.strip()
                    if linea:
                        id_compra, id_producto, cantidad, sub_total, total = linea.split(":")
                        self.compras[id_compra] = Compras(id_compra, id_producto, cantidad, sub_total, total)
            print("Compras importadas desde compras.txt")
        except FileNotFoundError:
            print("No existe el archivo compras.txt, se creará uno nuevo al guardar.")
    def guardar_compras(self):
        with open("compras.txt", "w", encoding="utf-8") as archivo:
            for compra in self.compras.values():
                archivo.write(f"{compra.id_compra} : {compra.id_producto} : {compra.cantidad} : {compra.sub_total} : {compra.total}\n")
    def sub_menu(self):
        while True:
            print("\n --Bienvenido--")
            print(" **** COMPRAS ****")
            print("1.- Registrar una Nueva Compra.")
            print("2.- Mostrar Clientes.")
            print("3.- Buscar Clientes.")
            print("4.- Salir.")
            opcion = int(input("Seleccione que opcion desea: "))
            match opcion:
                case 1:
                    self.Agregar_Compra()

                case 4:
                    print("Salir...")
                    print("REGRESANDO AL MENÚ PRINCIPAL....")

                    break

    def Agregar_Compra(self):
        print("\n **** Registrar nueva compra ****")
        while True:
            id_Compra = input("ID de la compra: ")
            if id_Compra in self.compras:
                print("Ya está registrada esta compra.")
                reintentar = input("ENTER para intentar de nuevo o 0 para salir: ")
                if reintentar == "0":
                    return
                else:
                    continue

            id_producto = input("Ingrese el ID del producto: ")
            if id_producto not in self.datos_productos.productos:
                print("El producto no existe. Agrega primero el producto.")
                return
                cantidad2 = int(input("Cantidad de productos: "))
            self.compras[id_Compra] = Compras(id_Compra, id_producto, cantidad2)
            producto = self.datos_productos.productos[id_producto]
            sub_total = producto.precio * cantidad2
            total = sub_total
            self.compras[id_Compra] = Compras(id_Compra, id_producto, cantidad2, sub_total, total)
            stock_anterior = producto.stock
            producto.stock += cantidad2

            self.datos_productos.guardar_productos()
            print(f"Compra registrada. Stock: {stock_anterior} -> {producto.stock}")

            reintentar = input("ENTER para agregar otra compra o 0 para salir: ")
            if reintentar == "0":
                return
            else:
                continue





class Menu:
    def __init__(self):
                print("\n ---Bienvenidos a nuestra tienda ----")
                print("1.- Agregar Categoria")
                print("2.- Agregar Producto")
                print("3.- Agregar Cliente")
                print("4.- Agregar Proveedor")
                print("5.- Agregar Empleado")
                print("6.- Agregar Compra")
                print("7.- salir")

datos_categoria = Datos_Categoria()

while True:
    datos_productos = Datos_Productos()
    datos_compras = Datos_Compra(datos_productos)
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
                    validar = input(f"\n Opcion no valida presione ENTER para intentar de nuevo o 6 para Salir del programa: ")
                    if validar == "6":
                        break
            case 2:
                try:
                    Datos_Productos().sub_menu()
                except ValueError:
                    validar = input(f"\n Opcion no valida presione ENTER para intentar de nuevo o 6 para Salir del programa: ")
                    if validar == "6":
                        break
            case 3:
                try:
                    Datos_Cliente().sub_menu()
                except ValueError:
                    validar = input(f"\n Opcion no valida presione ENTER para intentar de nuevo o 6 para Salir del programa: ")
                    if validar == "6":
                        break
            case 4:
                try:
                    Datos_Proveedor().sub_menu()
                except ValueError:
                    validar = input(f"\n Opcion no valida presione ENTER para intentar de nuevo o 6 para Salir del programa: ")
                    if validar == "6":
                        break
            case 5:
                try:
                    Datos_Empleados().sub_menu()
                except ValueError:
                    validar = input(f"\n Opcion no valida presione ENTER para intentar de nuevo o 6 para Salir del programa:  ")

            case 6:

                    Datos_Compra().sub_menu()

            case 7:
                print("Saliendo...")
                break
