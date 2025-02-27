class Producto:
    def __init__(self, id_producto, nombre, cantidad, precio):
        self.id_producto = id_producto
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    def get_id(self):
        return self.id_producto

    def get_nombre(self):
        return self.nombre

    def get_cantidad(self):
        return self.cantidad

    def get_precio(self):
        return self.precio

    def set_cantidad(self, nueva_cantidad):
        if nueva_cantidad >= 0:
            self.cantidad = nueva_cantidad
        else:
            raise ValueError("❌ La cantidad no puede ser negativa.")

    def set_precio(self, nuevo_precio):
        if nuevo_precio > 0:
            self.precio = nuevo_precio
        else:
            raise ValueError("❌ El precio debe ser mayor que 0.")

    def to_dict(self):
        """Convierte el objeto en un diccionario para serialización."""
        return {
            "id": self.id_producto,
            "nombre": self.nombre,
            "cantidad": self.cantidad,
            "precio": self.precio
        }

    @classmethod
    def from_dict(cls, data):
        """Crea un objeto Producto desde un diccionario."""
        return cls(data["id"], data["nombre"], data["cantidad"], data["precio"])

    def __str__(self):
        return f"ID: {self.id_producto} | Nombre: {self.nombre} | Cantidad: {self.cantidad} | Precio: ${self.precio:.2f}"
