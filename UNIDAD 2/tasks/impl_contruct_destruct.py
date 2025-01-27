class MiClase:
    """
    Esta es una clase de ejemplo que demuestra el uso de constructores y destructores en Python.
    """

    def __init__(self, nombre):
        """
        Constructor de la clase. Se llama automáticamente cuando se crea una instancia de la clase.
        :param nombre: Nombre que se asignará al atributo 'nombre' del objeto.
        """
        self.nombre = nombre
        print(f"Constructor llamado: Se ha creado una instancia de MiClase con el nombre '{self.nombre}'.")

    def __del__(self):
        """
        Destructor de la clase. Se llama automáticamente cuando la instancia de la clase es destruida.
        """
        print(f"Destructor llamado: La instancia de MiClase con el nombre '{self.nombre}' está siendo destruida.")

    def saludar(self):
        """
        Método que imprime un saludo utilizando el nombre del objeto.
        """
        print(f"Hola, mi nombre es {self.nombre}.")

# Creación de instancias de la clase
objeto1 = MiClase("Objeto1")
objeto2 = MiClase("Objeto2")

# Llamada al método saludar
objeto1.saludar()
objeto2.saludar()

# Los destructores se llamarán automáticamente cuando los objetos salgan del ámbito
# o cuando se eliminen explícitamente.
del objeto1
del objeto2