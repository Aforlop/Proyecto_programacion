class Producto:
    # Clase que representa un producto en el inventario.
    def __init__(self, nombre, cantidad, precio):
        # Inicializa los atributos del producto.
        self.nombre = nombre  # Nombre del producto.
        self.cantidad = cantidad  # Cantidad disponible del producto.
        self.precio = precio  # Precio unitario del producto.

    def descripcion(self):
        # Devuelve una descripción detallada del producto.
        return f"Producto: {self.nombre}, Cantidad: {self.cantidad}, Precio: {self.precio}"

def agregar_producto(productos, producto):
    # Agrega un producto a la lista si no existe ya.
    for Producto in productos:
        if Producto.nombre == producto.nombre:
            print("Error: El producto ya existe en el inventario.")
            return
    productos.append(producto)
    print(f"Producto {producto.nombre} agregado correctamente.")

def modificar_producto(productos, nombre, nueva_cantidad, nuevo_precio):
    # Modifica los atributos de un producto existente en la lista.
    for Producto in productos:
        if Producto.nombre == nombre:
            Producto.cantidad = nueva_cantidad  # Actualiza la cantidad del producto.
            Producto.precio = nuevo_precio  # Actualiza el precio del producto.
            print(f"Producto {nombre} modificado correctamente.")
            return
    print("Error: Producto no encontrado.")

def eliminar_producto(productos, nombre):
    # Elimina un producto de la lista si existe.
    for Producto in productos:
        if Producto.nombre == nombre:
            productos.remove(Producto)  # Elimina el producto de la lista.
            print(f"Producto {nombre} eliminado correctamente.")
            return
    print("Error: Producto no encontrado.")

def mostrar_inventario(productos):
    # Muestra todos los productos en el inventario.
    if not productos:
        print("El inventario está vacío.")
        return
    for Producto in productos:
        print(Producto.descripcion())  # Muestra la descripción de cada producto.

def main():
    # Función principal que gestiona el menú interactivo.
    productos = []  # Lista que almacena los productos del inventario.
    salir = False  # Controla el bucle del menú.

    while not salir:
        # Muestra el menú principal.
        print("\nMenú de gestión de inventario:")
        print("1. Agregar producto")
        print("2. Modificar producto")
        print("3. Eliminar producto")
        print("4. Consultar todos los productos")
        print("5. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            # Opción para agregar un producto.
            nombre = input("Nombre del producto: ")
            cantidad = int(input("Cantidad: "))
            precio = float(input("Precio: "))
            producto = Producto(nombre, cantidad, precio)
            agregar_producto(productos, producto)

        elif opcion == "2":
            # Opción para modificar un producto existente.
            nombre = input("Nombre del producto a modificar: ")
            nueva_cantidad = int(input("Nueva cantidad: "))
            nuevo_precio = float(input("Nuevo precio: "))
            modificar_producto(productos, nombre, nueva_cantidad, nuevo_precio)

        elif opcion == "3":
            # Opción para eliminar un producto.
            nombre = input("Nombre del producto a eliminar: ")
            eliminar_producto(productos, nombre)

        elif opcion == "4":
            # Opción para consultar el inventario.
            mostrar_inventario(productos)

        elif opcion == "5":
            # Opción para salir del programa.
            print("¡Adiós!")
            salir = True

        else:
            # Manejo de opción no válida.
            print("Opción no válida. Inténtelo de nuevo.")

if __name__ == "__main__":
    main()