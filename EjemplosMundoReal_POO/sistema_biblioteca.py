# sistema_biblioteca.py

from datetime import datetime, timedelta
from typing import List, Optional

class Libro:
    """
    Clase que representa un libro en la biblioteca.
    Demuestra el uso de atributos y encapsulamiento básico.
    """
    def __init__(self, titulo: str, autor: str, isbn: str):
        self._titulo = titulo
        self._autor = autor
        self._isbn = isbn
        self._disponible = True
        self._fecha_devolucion = None

    @property
    def titulo(self) -> str:
        return self._titulo

    @property
    def disponible(self) -> bool:
        return self._disponible

    def prestar(self) -> bool:
        """Intenta prestar el libro si está disponible"""
        if self._disponible:
            self._disponible = False
            self._fecha_devolucion = datetime.now() + timedelta(days=14)
            return True
        return False

    def devolver(self) -> None:
        """Marca el libro como devuelto"""
        self._disponible = True
        self._fecha_devolucion = None

    def __str__(self) -> str:
        return f"{self._titulo} por {self._autor} (ISBN: {self._isbn})"


class Usuario:
    """
    Clase que representa un usuario de la biblioteca.
    Demuestra la gestión de relaciones entre objetos.
    """
    def __init__(self, nombre: str, id_usuario: str):
        self._nombre = nombre
        self._id_usuario = id_usuario
        self._libros_prestados: List[Libro] = []

    def pedir_prestado(self, libro: Libro) -> bool:
        """
        Intenta pedir prestado un libro.
        Demuestra la interacción entre objetos.
        """
        if len(self._libros_prestados) < 3 and libro.prestar():
            self._libros_prestados.append(libro)
            return True
        return False

    def devolver_libro(self, libro: Libro) -> bool:
        """Procesa la devolución de un libro"""
        if libro in self._libros_prestados:
            libro.devolver()
            self._libros_prestados.remove(libro)
            return True
        return False

    def listar_libros_prestados(self) -> List[str]:
        """Retorna una lista de los libros prestados al usuario"""
        return [str(libro) for libro in self._libros_prestados]


class Biblioteca:
    """
    Clase principal que gestiona la biblioteca.
    Demuestra el principio de composición y la gestión del sistema.
    """
    def __init__(self, nombre: str):
        self._nombre = nombre
        self._catalogo: List[Libro] = []
        self._usuarios: List[Usuario] = []

    def agregar_libro(self, libro: Libro) -> None:
        """Añade un nuevo libro al catálogo"""
        self._catalogo.append(libro)

    def registrar_usuario(self, usuario: Usuario) -> None:
        """Registra un nuevo usuario en la biblioteca"""
        self._usuarios.append(usuario)

    def buscar_libro(self, isbn: str) -> Optional[Libro]:
        """
        Busca un libro por ISBN.
        Demuestra búsqueda y manejo de datos.
        """
        for libro in self._catalogo:
            if libro._isbn == isbn:
                return libro
        return None

    def buscar_usuario(self, id_usuario: str) -> Optional[Usuario]:
        """Busca un usuario por ID"""
        for usuario in self._usuarios:
            if usuario._id_usuario == id_usuario:
                return usuario
        return None


# Ejemplo de uso del sistema
def main():
    # Crear una nueva biblioteca
    biblioteca = Biblioteca("Biblioteca Colegio Antonio Samaniego")

    # Crear algunos libros de programación
    libro1 = Libro("Clean Code", "Robert C. Martin", "9780132350884")
    libro2 = Libro("The Pragmatic Programmer", "Andrew Hunt, David Thomas", "9780201616224")
    libro3 = Libro("Introduction to Algorithms", "Thomas H. Cormen", "9780262033848")


    # Agregar libros a la biblioteca
    for libro in [libro1, libro2, libro3]:
        biblioteca.agregar_libro(libro)

    # Crear y registrar usuarios
    # Crear algunos usuarios
    usuario1 = Usuario("Emilio Senguana", "U001")
    usuario2 = Usuario("Danis Manchu", "U002")

    biblioteca.registrar_usuario(usuario1)
    biblioteca.registrar_usuario(usuario2)

    # Realizar algunas operaciones
    # Préstamo de libros
    if usuario1.pedir_prestado(libro1):
        print(f"{usuario1._nombre} ha pedido prestado: {libro1}")

    # Intentar pedir un libro ya prestado
    if not usuario2.pedir_prestado(libro1):
        print(f"No se pudo prestar el libro {libro1} a {usuario2._nombre}")

    # Devolver un libro
    if usuario1.devolver_libro(libro1):
        print(f"{usuario1._nombre} ha devuelto: {libro1}")

    # Listar libros prestados
    print(f"Libros prestados a {usuario1._nombre}:")
    for libro in usuario1.listar_libros_prestados():
        print(f"- {libro}")

if __name__ == "__main__":
    main()