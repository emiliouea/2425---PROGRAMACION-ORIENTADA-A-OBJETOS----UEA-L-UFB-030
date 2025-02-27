from inventario import Inventario

def mostrar_menu():
    print("\n=== 📦 SISTEMA DE GESTIÓN DE INVENTARIOS ===")
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
            nombre = input("Ingrese nombre del producto: ")
            cantidad = int(input("Ingrese cantidad: "))
            precio = float(input("Ingrese precio: "))
            inventario.agregar_producto(nombre, cantidad, precio)

        elif opcion == "2":
            id_producto = int(input("Ingrese ID del producto a eliminar: "))
            inventario.eliminar_producto(id_producto)

        elif opcion == "6":
            inventario.mostrar_inventario()

        elif opcion == "7":
            print("¡Gracias por usar el sistema!")
            break

if __name__ == "__main__":
    main()
