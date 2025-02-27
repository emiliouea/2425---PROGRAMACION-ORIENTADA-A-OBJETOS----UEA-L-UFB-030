import os
import json
from producto import Producto

class Inventario:
    def __init__(self, archivo="inventario.json"):
        self.archivo = archivo
        self.productos = {}  # Diccionario de productos {id: Producto}
        self.ultimo_id = 0  # Último ID utilizado
        self.cargar_desde_archivo()  # Cargar datos al iniciar

    def generar_id(self):
        """Genera un ID único para cada producto"""
        self.ultimo_id += 1
        return self.ultimo_id

    def cargar_desde_archivo(self):
        """Carga el inventario desde un archivo JSON"""
        if not os.path.exists(self.archivo):
            print("Archivo de inventario no encontrado. Se creará uno nuevo.")
            return

        try:
            with open(self.archivo, "r", encoding="utf-8") as file:
                datos = json.load(file)  # Leer datos en formato JSON
                self.productos = {int(item["id"]): Producto.from_dict(item) for item in datos}
                self.ultimo_id = max(self.productos.keys(), default=0)  # Actualizar ID máximo
                print("📂 Inventario cargado correctamente.")
        except (json.JSONDecodeError, FileNotFoundError):
            print("⚠️ Error: Archivo vacío o corrupto. Se iniciará un nuevo inventario.")
        except PermissionError:
            print("🚫 Error: No se tiene permiso para leer el archivo.")

    def guardar_en_archivo(self):
        """Guarda el inventario en un archivo JSON"""
        try:
            with open(self.archivo, "w", encoding="utf-8") as file:
                datos = [p.to_dict() for p in self.productos.values()]
                json.dump(datos, file, indent=4, ensure_ascii=False)
                print("💾 Inventario guardado correctamente.")
        except PermissionError:
            print("🚫 Error: No se tiene permiso para escribir en el archivo.")

    def agregar_producto(self, nombre, cantidad, precio):
        """Agrega un nuevo producto al inventario y lo guarda en el archivo"""
        if not nombre.strip():
            print("❌ El nombre no puede estar vacío.")
            return False
        if cantidad < 0:
            print("❌ La cantidad no puede ser negativa.")
            return False
        if precio <= 0:
            print("❌ El precio debe ser mayor que 0.")
            return False

        nuevo_id = self.generar_id()
        nuevo_producto = Producto(nuevo_id, nombre, cantidad, precio)
        self.productos[nuevo_id] = nuevo_producto
        self.guardar_en_archivo()
        print(f"✅ Producto '{nombre}' agregado exitosamente.")
        return True

    def eliminar_producto(self, id_producto):
        """Elimina un producto por su ID y actualiza el archivo"""
        if id_producto in self.productos:
            del self.productos[id_producto]
            self.guardar_en_archivo()
            print("✅ Producto eliminado exitosamente.")
            return True
        print("❌ Producto no encontrado.")
        return False

    def actualizar_cantidad(self, id_producto, nueva_cantidad):
        """Actualiza la cantidad de un producto"""
        if id_producto in self.productos:
            try:
                self.productos[id_producto].set_cantidad(nueva_cantidad)
                self.guardar_en_archivo()
                print("✅ Cantidad actualizada exitosamente.")
                return True
            except ValueError as e:
                print(f"❌ {str(e)}")
                return False
        print("❌ Producto no encontrado.")
        return False

    def actualizar_precio(self, id_producto, nuevo_precio):
        """Actualiza el precio de un producto"""
        if id_producto in self.productos:
            try:
                self.productos[id_producto].set_precio(nuevo_precio)
                self.guardar_en_archivo()
                print("✅ Precio actualizado exitosamente.")
                return True
            except ValueError as e:
                print(f"❌ {str(e)}")
                return False
        print("❌ Producto no encontrado.")
        return False

    def buscar_por_nombre(self, nombre):
        """Busca productos por nombre"""
        nombre = nombre.lower()
        resultados = [p for p in self.productos.values() if nombre in p.get_nombre().lower()]
        return resultados

    def mostrar_inventario(self):
        """Muestra todos los productos en el inventario"""
        if not self.productos:
            print("\n📦 El inventario está vacío.")
            return
        print("\n📋 Productos en inventario:")
        for producto in self.productos.values():
            print(producto)
