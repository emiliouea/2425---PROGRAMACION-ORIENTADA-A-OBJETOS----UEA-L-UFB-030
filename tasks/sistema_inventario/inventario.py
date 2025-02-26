import os
import json
from producto import Producto

class Inventario:
    def __init__(self, archivo="inventario.txt"):
        self.archivo = archivo
        self.productos = []  # Lista de productos
        self.ultimo_id = 0  # Último ID utilizado
        self.cargar_desde_archivo()  # Cargar productos al iniciar

    def generar_id(self):
        """Genera un ID único para cada producto"""
        self.ultimo_id += 1
        return self.ultimo_id

    def cargar_desde_archivo(self):
        """Carga el inventario desde el archivo de texto al iniciar el programa"""
        if not os.path.exists(self.archivo):
            print("Archivo de inventario no encontrado, se creará uno nuevo.")
            return

        try:
            with open(self.archivo, "r", encoding="utf-8") as file:
                datos = json.load(file)  # Leer datos en formato JSON

                for item in datos:
                    producto = Producto(
                        item["id"], item["nombre"], item["cantidad"], item["precio"]
                    )
                    self.productos.append(producto)
                    self.ultimo_id = max(self.ultimo_id, item["id"])  # Actualizar último ID

                print("Inventario cargado correctamente desde el archivo.")

        except (json.JSONDecodeError, FileNotFoundError):
            print("Error: El archivo está vacío o corrupto. Se iniciará un nuevo inventario.")
        except PermissionError:
            print("Error: No se tiene permiso para leer el archivo de inventario.")

    def guardar_en_archivo(self):
        """Guarda el inventario en un archivo de texto en formato JSON"""
        try:
            with open(self.archivo, "w", encoding="utf-8") as file:
                datos = [
                    {"id": p.get_id(), "nombre": p.get_nombre(), "cantidad": p.get_cantidad(), "precio": p.get_precio()}
                    for p in self.productos
                ]
                json.dump(datos, file, indent=4, ensure_ascii=False)
                print("Inventario guardado correctamente en archivo.")

        except PermissionError:
            print("Error: No se tiene permiso para escribir en el archivo de inventario.")

    def agregar_producto(self, nombre, cantidad, precio):
        """Agrega un nuevo producto al inventario y lo guarda en el archivo"""
        try:
            if not nombre.strip():
                raise ValueError("El nombre no puede estar vacío")
            if cantidad < 0:
                raise ValueError("La cantidad no puede ser negativa")
            if precio <= 0:
                raise ValueError("El precio debe ser mayor que 0")

            nuevo_id = self.generar_id()
            nuevo_producto = Producto(nuevo_id, nombre, cantidad, precio)
            self.productos.append(nuevo_producto)

            self.guardar_en_archivo()  # Guardar cambios en archivo
            print("✅ Producto agregado exitosamente.")
            return True
        except ValueError as e:
            print(f"❌ Error al agregar producto: {str(e)}")
            return False

    def eliminar_producto(self, id_producto):
        """Elimina un producto por su ID y actualiza el archivo"""
        for producto in self.productos:
            if producto.get_id() == id_producto:
                self.productos.remove(producto)
                self.guardar_en_archivo()
                print("✅ Producto eliminado exitosamente.")
                return True
        print("❌ Producto no encontrado.")
        return False

    def actualizar_cantidad(self, id_producto, nueva_cantidad):
        """Actualiza la cantidad de un producto y guarda cambios en el archivo"""
        for producto in self.productos:
            if producto.get_id() == id_producto:
                try:
                    producto.set_cantidad(nueva_cantidad)
                    self.guardar_en_archivo()
                    print("✅ Cantidad actualizada exitosamente.")
                    return True
                except ValueError as e:
                    print(f"❌ {str(e)}")
                    return False
        print("❌ Producto no encontrado.")
        return False

    def actualizar_precio(self, id_producto, nuevo_precio):
        """Actualiza el precio de un producto y guarda cambios en el archivo"""
        for producto in self.productos:
            if producto.get_id() == id_producto:
                try:
                    producto.set_precio(nuevo_precio)
                    self.guardar_en_archivo()
                    print("✅ Precio actualizado exitosamente.")
                    return True
                except ValueError as e:
                    print(f"❌ {str(e)}")
                    return False
        print("❌ Producto no encontrado.")
        return False

    def buscar_por_nombre(self, nombre):
        """Busca productos por nombre (búsqueda parcial)"""
        nombre = nombre.lower()
        resultados = [p for p in self.productos if nombre in p.get_nombre().lower()]
        return resultados

    def mostrar_inventario(self):
        """Muestra todos los productos en el inventario"""
        if not self.productos:
            print("\n📦 El inventario está vacío.")
            return
        print("\n📋 Productos en inventario:")
        for producto in self.productos:
            print(producto)
