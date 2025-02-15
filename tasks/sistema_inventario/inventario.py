from producto import Producto
class Inventario:
    def __init__(self):
        self.productos = []  # Lista para almacenar los productos
        self.ultimo_id = 0  # Para generar IDs únicos

    def generar_id(self):
        """Genera un ID único para cada producto"""
        self.ultimo_id += 1
        return self.ultimo_id

    def agregar_producto(self, nombre, cantidad, precio):
        """Agrega un nuevo producto al inventario"""
        try:
            # Validaciones básicas
            if not nombre.strip():
                raise ValueError("El nombre no puede estar vacío")
            if cantidad < 0:
                raise ValueError("La cantidad no puede ser negativa")
            if precio <= 0:
                raise ValueError("El precio debe ser mayor que 0")

            nuevo_id = self.generar_id()
            nuevo_producto = Producto(nuevo_id, nombre, cantidad, precio)
            self.productos.append(nuevo_producto)
            return True
        except ValueError as e:
            print(f"Error al agregar producto: {str(e)}")
            return False

    def eliminar_producto(self, id_producto):
        """Elimina un producto por su ID"""
        for producto in self.productos:
            if producto.get_id() == id_producto:
                self.productos.remove(producto)
                return True
        return False

    def actualizar_cantidad(self, id_producto, nueva_cantidad):
        """Actualiza la cantidad de un producto"""
        for producto in self.productos:
            if producto.get_id() == id_producto:
                try:
                    producto.set_cantidad(nueva_cantidad)
                    return True
                except ValueError as e:
                    print(f"Error al actualizar cantidad: {str(e)}")
                    return False
        return False

    def actualizar_precio(self, id_producto, nuevo_precio):
        """Actualiza el precio de un producto"""
        for producto in self.productos:
            if producto.get_id() == id_producto:
                try:
                    producto.set_precio(nuevo_precio)
                    return True
                except ValueError as e:
                    print(f"Error al actualizar precio: {str(e)}")
                    return False
        return False

    def buscar_por_nombre(self, nombre):
        """Busca productos por nombre (búsqueda parcial)"""
        resultados = []
        nombre = nombre.lower()
        for producto in self.productos:
            if nombre in producto.get_nombre().lower():
                resultados.append(producto)
        return resultados

    def mostrar_inventario(self):
        """Muestra todos los productos en el inventario"""
        if not self.productos:
            print("\nEl inventario está vacío")
            return
        print("\nProductos en inventario:")
        for producto in self.productos:
            print(producto)