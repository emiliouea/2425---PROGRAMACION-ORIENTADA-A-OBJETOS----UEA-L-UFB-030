from inventario import Inventario
def mostrar_menu():
    print("\n=== SISTEMA DE GESTIÓN DE INVENTARIOS ===")
    print("1. Agregar producto")
    print("2. Eliminar producto")
    print("3. Actualizar cantidad")
    print("4. Actualizar precio")
    print("5. Buscar producto por nombre")
    print("6. Mostrar inventario")
    print("7. Salir")
    return input("Seleccione una opción: ")

def main():
    inventario = Inventario()

    while True:
        opcion = mostrar_menu()

        if opcion == "1":
            try:
                nombre = input("Ingrese nombre del producto: ")
                cantidad = int(input("Ingrese cantidad: "))
                precio = float(input("Ingrese precio: "))

                if inventario.agregar_producto(nombre, cantidad, precio):
                    print("Producto agregado exitosamente")
            except ValueError:
                print("Error: Ingrese valores válidos")

        elif opcion == "2":
            try:
                id_producto = int(input("Ingrese ID del producto a eliminar: "))
                if inventario.eliminar_producto(id_producto):
                    print("Producto eliminado exitosamente")
                else:
                    print("Producto no encontrado")
            except ValueError:
                print("Error: Ingrese un ID válido")

        elif opcion == "3":
            try:
                id_producto = int(input("Ingrese ID del producto: "))
                nueva_cantidad = int(input("Ingrese nueva cantidad: "))
                if inventario.actualizar_cantidad(id_producto, nueva_cantidad):
                    print("Cantidad actualizada exitosamente")
                else:
                    print("Producto no encontrado")
            except ValueError:
                print("Error: Ingrese valores válidos")

        elif opcion == "4":
            try:
                id_producto = int(input("Ingrese ID del producto: "))
                nuevo_precio = float(input("Ingrese nuevo precio: "))
                if inventario.actualizar_precio(id_producto, nuevo_precio):
                    print("Precio actualizado exitosamente")
                else:
                    print("Producto no encontrado")
            except ValueError:
                print("Error: Ingrese valores válidos")

        elif opcion == "5":
            nombre = input("Ingrese nombre a buscar: ")
            resultados = inventario.buscar_por_nombre(nombre)
            if resultados:
                print("\nProductos encontrados:")
                for producto in resultados:
                    print(producto)
            else:
                print("No se encontraron productos")

        elif opcion == "6":
            inventario.mostrar_inventario()

        elif opcion == "7":
            print("¡Gracias por usar el sistema!")
            break

        else:
            print("Opción no válida")

if __name__ == "__main__":
    main()