
productos = []

def añadir_producto():
    nombre = input("Ingrese el Nombre del producto: ")
    while True:
        try:
            precio = float(input("Ingrese el Precio del producto: "))
            cantidad = int(input("Ingrese la Cantidad disponible: "))
            break
        except ValueError:
            print("Por favor, introduce un número válido para el precio y la cantidad.")
    
    producto = {'nombre': nombre, 'precio': precio, 'cantidad': cantidad}
    productos.append(producto)
    print(f"Producto '{nombre}' añadido con éxito.")

def ver_productos():
    
    if not productos:
        print("No hay productos en la lista.")
    else:
        for idx, producto in enumerate(productos, start=1):
            print(f"{idx}. Nombre: {producto['nombre']}, Precio: {producto['precio']}, Cantidad: {producto['cantidad']}")


def actualizar_producto():
    ver_productos()
    if productos:
        try:
            indice = int(input("Selecciona el número del producto a actualizar: ")) - 1
            if 0 <= indice < len(productos):
                nombre = input("Ingrese el nuevo nombre del producto: ")
                if nombre:
                    productos[indice]['nombre'] = nombre
                
                try:
                    precio = input("Ingrese el nuevo precio del producto: ")
                    if precio:
                        productos[indice]['precio'] = float(precio)

                    cantidad = input("Ingrese la nueva cantidad del producto: ")
                    if cantidad:
                        productos[indice]['cantidad'] = int(cantidad)

                    print(f"Producto actualizado: {productos[indice]}")
                except ValueError:
                    print("Por favor, introduce un número válido para el precio y la cantidad.")
            else:
                print("Número de producto no válido.")
        except ValueError:
            print("Por favor, selecciona un número válido.")

def eliminar_producto():
    ver_productos()
    if productos:
        try:
            indice = int(input("Selecciona el número del producto a eliminar: ")) - 1
            if 0 <= indice < len(productos):
                eliminado = productos.pop(indice)
                print(f"Producto '{eliminado['nombre']}' eliminado.")
            else:
                print("Número de producto no válido.")
        except ValueError:
            print("Por favor, selecciona un número válido.")


def guardar_datos():
    with open("productos.txt", "w") as archivo:
        for producto in productos:
            archivo.write(f"{producto['nombre']},{producto['precio']},{producto['cantidad']}\n")
    print("Los datos se han guardado correctamente en 'productos.txt'.")

def cargar_datos():
    try:
        with open("productos.txt", "r") as archivo:
            for linea in archivo:
                nombre, precio, cantidad = linea.strip().split(',')
                productos.append({'nombre': nombre, 'precio': float(precio), 'cantidad': int(cantidad)})
        print("Datos cargados desde 'productos.txt'.")
    except FileNotFoundError:
        print("No se encontró el archivo 'productos.txt', comenzando con una lista vacía.")


def menu():
    cargar_datos()  

    while True:
        print("1: Añadir producto")
        print("2: Ver productos")
        print("3: Actualizar producto")
        print("4: Eliminar producto")
        print("5: Guardar datos y salir")

        opcion = input("Selecciona una opción: ")

        if opcion == '1':
            añadir_producto()
        elif opcion == '2':
            ver_productos()
        elif opcion == '3':
            actualizar_producto()
        elif opcion == '4':
            eliminar_producto()
        elif opcion == '5':
            guardar_datos()
            break
        else:
            print("Por favor, selecciona una opción válida.")

menu()