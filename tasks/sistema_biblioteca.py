 
"""
Sistema de Gestión de Biblioteca Digital

Este módulo implementa un sistema para gestionar una biblioteca digital,
permitiendo administrar libros, usuarios y préstamos.
"""

class Libro:
    """
    Representa un libro en la biblioteca digital.
    
    Atributos:
        _info: Tupla con (título, autor) - datos inmutables del libro
        categoria: Categoría del libro
        isbn: ISBN único del libro
        disponible: Estado de disponibilidad del libro
    """
    
    def __init__(self, titulo, autor, categoria, isbn):
        """
        Inicializa un nuevo libro.

        Args:
            titulo: Título del libro
            autor: Autor del libro
            categoria: Categoría del libro
            isbn: ISBN único del libro
        """
        self._info = (titulo, autor)  
        self.categoria = categoria
        self.isbn = isbn
        self.disponible = True
    
    @property
    def titulo(self):
        """Obtiene el título del libro."""
        return self._info[0]
    
    @property
    def autor(self):
        """Obtiene el autor del libro."""
        return self._info[1]
    
    def __str__(self):
        """Representación en cadena del libro."""
        estado = "Disponible" if self.disponible else "Prestado"
        return f"'{self.titulo}' por {self.autor} [{self.categoria}] (ISBN: {self.isbn}) - {estado}"


class Usuario:
    """
    Representa a un usuario de la biblioteca digital.
    
    Atributos:
        nombre: Nombre del usuario
        id_usuario: ID único del usuario
        libros_prestados: Lista de libros actualmente prestados al usuario
    """
    
    def __init__(self, nombre, id_usuario):
        """
        Inicializa un nuevo usuario.

        Args:
            nombre: Nombre del usuario
            id_usuario: ID único del usuario
        """
        self.nombre = nombre
        self.id_usuario = id_usuario
        self.libros_prestados = []   
    
    def prestar_libro(self, libro):
        """
        Registra un libro como prestado a este usuario.

        Args:
            libro: Objeto Libro a prestar
        """
        self.libros_prestados.append(libro)
    
    def devolver_libro(self, libro):
        """
        Registra la devolución de un libro.

        Args:
            libro: Objeto Libro a devolver
            
        Returns:
            bool: True si el libro fue devuelto, False si no estaba prestado al usuario
        """
        if libro in self.libros_prestados:
            self.libros_prestados.remove(libro)
            return True
        return False
    
    def listar_libros_prestados(self):
        """
        Lista todos los libros prestados al usuario.
        
        Returns:
            list: Lista de libros prestados al usuario
        """
        return self.libros_prestados
    
    def __str__(self):
        """Representación en cadena del usuario."""
        return f"Usuario: {self.nombre} (ID: {self.id_usuario}) - Libros prestados: {len(self.libros_prestados)}"


class Biblioteca:
    """
    Gestiona la colección de libros, usuarios y préstamos.
    
    Atributos:
        libros: Diccionario de libros con ISBN como clave
        usuarios: Diccionario de usuarios con ID como clave
        ids_usuarios: Conjunto de IDs de usuario para garantizar unicidad
    """
    
    def __init__(self):
        """Inicializa una nueva biblioteca digital."""
        self.libros = {}  # Diccionario con ISBN como clave y objeto Libro como valor
        self.usuarios = {}  # Diccionario con ID de usuario como clave y objeto Usuario como valor
        self.ids_usuarios = set()  # Conjunto para asegurar IDs únicos
    
    def añadir_libro(self, libro):
        """
        Añade un libro a la biblioteca.

        Args:
            libro: Objeto Libro a añadir
            
        Returns:
            bool: True si el libro fue añadido, False si ya existía
        """
        if libro.isbn in self.libros:
            return False
        
        self.libros[libro.isbn] = libro
        return True
    
    def quitar_libro(self, isbn):
        """
        Quita un libro de la biblioteca.

        Args:
            isbn: ISBN del libro a quitar
            
        Returns:
            bool: True si el libro fue quitado, False si no existía
        """
        if isbn in self.libros:
            # Verificar que no esté prestado
            libro = self.libros[isbn]
            if not libro.disponible:
                return False
            
            del self.libros[isbn]
            return True
        return False
    
    def registrar_usuario(self, usuario):
        """
        Registra un nuevo usuario en la biblioteca.

        Args:
            usuario: Objeto Usuario a registrar
            
        Returns:
            bool: True si el usuario fue registrado, False si el ID ya está en uso
        """
        if usuario.id_usuario in self.ids_usuarios:
            return False
        
        self.usuarios[usuario.id_usuario] = usuario
        self.ids_usuarios.add(usuario.id_usuario)
        return True
    
    def dar_baja_usuario(self, id_usuario):
        """
        Da de baja a un usuario de la biblioteca.

        Args:
            id_usuario: ID del usuario a dar de baja
            
        Returns:
            bool: True si el usuario fue dado de baja, False si no existía o tiene libros prestados
        """
        if id_usuario in self.usuarios:
            usuario = self.usuarios[id_usuario]
            # Verificar que no tenga libros prestados
            if usuario.libros_prestados:
                return False
            
            del self.usuarios[id_usuario]
            self.ids_usuarios.remove(id_usuario)
            return True
        return False
    
    def prestar_libro(self, isbn, id_usuario):
        """
        Presta un libro a un usuario.

        Args:
            isbn: ISBN del libro a prestar
            id_usuario: ID del usuario que solicita el préstamo
            
        Returns:
            bool: True si el préstamo fue exitoso, False en caso contrario
        """
        if isbn not in self.libros or id_usuario not in self.usuarios:
            return False
        
        libro = self.libros[isbn]
        usuario = self.usuarios[id_usuario]
        
        if not libro.disponible:
            return False
        
        libro.disponible = False
        usuario.prestar_libro(libro)
        return True
    
    def devolver_libro(self, isbn, id_usuario):
        """
        Registra la devolución de un libro.

        Args:
            isbn: ISBN del libro a devolver
            id_usuario: ID del usuario que devuelve el libro
            
        Returns:
            bool: True si la devolución fue exitosa, False en caso contrario
        """
        if isbn not in self.libros or id_usuario not in self.usuarios:
            return False
        
        libro = self.libros[isbn]
        usuario = self.usuarios[id_usuario]
        
        if libro.disponible or libro not in usuario.libros_prestados:
            return False
        
        libro.disponible = True
        return usuario.devolver_libro(libro)
    
    def buscar_por_titulo(self, titulo):
        """
        Busca libros por título.

        Args:
            titulo: Título o parte del título a buscar
            
        Returns:
            list: Lista de libros que coinciden con la búsqueda
        """
        titulo = titulo.lower()
        return [libro for libro in self.libros.values() 
                if titulo in libro.titulo.lower()]
    
    def buscar_por_autor(self, autor):
        """
        Busca libros por autor.

        Args:
            autor: Nombre o parte del nombre del autor a buscar
            
        Returns:
            list: Lista de libros que coinciden con la búsqueda
        """
        autor = autor.lower()
        return [libro for libro in self.libros.values() 
                if autor in libro.autor.lower()]
    
    def buscar_por_categoria(self, categoria):
        """
        Busca libros por categoría.

        Args:
            categoria: Categoría a buscar
            
        Returns:
            list: Lista de libros que coinciden con la búsqueda
        """
        categoria = categoria.lower()
        return [libro for libro in self.libros.values() 
                if categoria == libro.categoria.lower()]
    
    def listar_libros_usuario(self, id_usuario):
        """
        Lista los libros prestados a un usuario.

        Args:
            id_usuario: ID del usuario
            
        Returns:
            list: Lista de libros prestados al usuario, o None si el usuario no existe
        """
        if id_usuario not in self.usuarios:
            return None
        
        return self.usuarios[id_usuario].listar_libros_prestados()


 
def probar_sistema():
    """
    Función para probar el sistema de gestión de biblioteca digital.
    """
    
    biblioteca = Biblioteca()
    
    # Crear algunos libros
    libro1 = Libro("Cien años de soledad", "Gabriel García Márquez", "Ficción", "978-0307474728")
    libro2 = Libro("El código Da Vinci", "Dan Brown", "Misterio", "978-0307474001")
    libro3 = Libro("Harry Potter y la piedra filosofal", "J.K. Rowling", "Fantasía", "978-0590353427")
    libro4 = Libro("Crimen y castigo", "Fiódor Dostoyevski", "Clásico", "978-0143058142")
    libro5 = Libro("El principito", "Antoine de Saint-Exupéry", "Fantasía", "978-0156012195")
    
    # Añadir libros a la biblioteca
    print("=== Añadiendo libros a la biblioteca ===")
    biblioteca.añadir_libro(libro1)
    biblioteca.añadir_libro(libro2)
    biblioteca.añadir_libro(libro3)
    biblioteca.añadir_libro(libro4)
    biblioteca.añadir_libro(libro5)
    
    # Mostrar los libros añadidos
    print("\n=== Libros en la biblioteca ===")
    for isbn, libro in biblioteca.libros.items():
        print(libro)
    
    # Crear algunos usuarios
    usuario1 = Usuario("Ana García", "U001")
    usuario2 = Usuario("Juan Martínez", "U002")
    usuario3 = Usuario("María López", "U003")
    
    # Registrar usuarios
    print("\n=== Registrando usuarios ===")
    biblioteca.registrar_usuario(usuario1)
    biblioteca.registrar_usuario(usuario2)
    biblioteca.registrar_usuario(usuario3)
    
    # Mostrar los usuarios registrados
    print("\n=== Usuarios registrados ===")
    for id_usuario, usuario in biblioteca.usuarios.items():
        print(usuario)
    
    # Prestar libros
    print("\n=== Prestando libros ===")
    biblioteca.prestar_libro("978-0307474728", "U001")  # Cien años de soledad a Ana
    biblioteca.prestar_libro("978-0307474001", "U001")  # El código Da Vinci a Ana
    biblioteca.prestar_libro("978-0590353427", "U002")  # Harry Potter a Juan
    
    # Listar libros prestados por usuario
    print("\n=== Libros prestados por Ana (U001) ===")
    libros_ana = biblioteca.listar_libros_usuario("U001")
    for libro in libros_ana:
        print(libro)
    
    # Buscar libros por categoría
    print("\n=== Libros de Fantasía ===")
    libros_fantasia = biblioteca.buscar_por_categoria("Fantasía")
    for libro in libros_fantasia:
        print(libro)
    
    # Buscar libros por autor
    print("\n=== Libros de García Márquez ===")
    libros_garcia = biblioteca.buscar_por_autor("García Márquez")
    for libro in libros_garcia:
        print(libro)
    
    # Buscar libros por título
    print("\n=== Libros con 'Harry' en el título ===")
    libros_harry = biblioteca.buscar_por_titulo("Harry")
    for libro in libros_harry:
        print(libro)
    
    # Devolver un libro
    print("\n=== Devolviendo un libro ===")
    if biblioteca.devolver_libro("978-0307474728", "U001"):
        print("Libro 'Cien años de soledad' devuelto correctamente")
    
    # Verificar estado después de la devolución
    print("\n=== Estado de los libros después de la devolución ===")
    for isbn, libro in biblioteca.libros.items():
        print(libro)
    
    # Intentar dar de baja a un usuario con libros prestados
    print("\n=== Intentando dar de baja a un usuario con libros prestados ===")
    if not biblioteca.dar_baja_usuario("U001"):
        print("No se puede dar de baja a un usuario con libros prestados")
    
    # Devolver todos los libros de Ana
    print("\n=== Devolviendo todos los libros de Ana ===")
    for libro in libros_ana.copy():  # Usamos una copia para evitar problemas al modificar la lista original
        if biblioteca.devolver_libro(libro.isbn, "U001"):
            print(f"Libro '{libro.titulo}' devuelto correctamente")
    
    # Ahora sí podemos dar de baja a Ana
    print("\n=== Dando de baja a un usuario sin libros prestados ===")
    if biblioteca.dar_baja_usuario("U001"):
        print("Usuario Ana García dado de baja correctamente")
    
    # Verificar usuarios restantes
    print("\n=== Usuarios restantes ===")
    for id_usuario, usuario in biblioteca.usuarios.items():
        print(usuario)


if __name__ == "__main__":
    probar_sistema()