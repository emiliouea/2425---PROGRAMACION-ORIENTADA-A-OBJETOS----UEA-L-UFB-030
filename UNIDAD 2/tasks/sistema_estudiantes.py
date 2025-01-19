# sistema_estudiantes.py

class Persona:
    """
    Clase base que representa una persona en el sistema educativo.
    Demuestra encapsulación mediante atributos privados y propiedades.
    """

    def __init__(self, id, nombre, edad):
        # Atributos encapsulados usando doble guión bajo
        self.__id = id
        self.__nombre = nombre
        self.__edad = edad
        self.__activo = True

    # Propiedades para acceder a los atributos encapsulados
    @property
    def id(self):
        return self.__id

    @property
    def nombre(self):
        return self.__nombre

    @property
    def edad(self):
        return self.__edad

    @property
    def activo(self):
        return self.__activo

    def mostrar_info(self):
        """
        Método base que será sobrescrito por las clases hijas,
        demostrando polimorfismo.
        """
        return f"Persona - ID: {self.__id}, Nombre: {self.__nombre}, Edad: {self.__edad}"


class Estudiante(Persona):
    """
    Clase derivada de Persona que representa a un estudiante.
    Demuestra herencia y polimorfismo.
    """

    def __init__(self, id, nombre, edad, carrera):
        # Llamada al constructor de la clase base
        super().__init__(id, nombre, edad)
        self.carrera = carrera
        self.__calificaciones = {}  # Diccionario para almacenar calificaciones

    def agregar_calificacion(self, materia, nota):
        """Método para agregar calificaciones al estudiante"""
        if 0 <= nota <= 10:
            self.__calificaciones[materia] = nota
            return f"Calificación agregada para {materia}: {nota}"
        return "La calificación debe estar entre 0 y 10"

    def obtener_promedio(self):
        """Calcula el promedio de calificaciones del estudiante"""
        if not self.__calificaciones:
            return 0
        return sum(self.__calificaciones.values()) / len(self.__calificaciones)

    def mostrar_info(self):
        """
        Sobrescribe el método mostrar_info de la clase base,
        demostrando polimorfismo.
        """
        info_base = super().mostrar_info()
        return f"{info_base}\nCarrera: {self.carrera}\nPromedio: {self.obtener_promedio():.2f}"


class Profesor(Persona):
    """
    Clase derivada de Persona que representa a un profesor.
    Demuestra herencia y polimorfismo.
    """

    def __init__(self, id, nombre, edad, departamento):
        # Llamada al constructor de la clase base
        super().__init__(id, nombre, edad)
        self.departamento = departamento
        self.__cursos = []  # Lista privada de cursos

    def asignar_curso(self, curso):
        """Método para asignar un curso al profesor"""
        if curso not in self.__cursos:
            self.__cursos.append(curso)
            return f"Curso {curso} asignado al profesor {self.nombre}"
        return "El curso ya está asignado"

    def obtener_cursos(self):
        """Método para obtener la lista de cursos del profesor"""
        return self.__cursos.copy()  # Retorna una copia para mantener encapsulación

    def mostrar_info(self):
        """
        Sobrescribe el método mostrar_info de la clase base,
        demostrando polimorfismo.
        """
        info_base = super().mostrar_info()
        return f"{info_base}\nDepartamento: {self.departamento}\nCursos: {', '.join(self.__cursos)}"


# Código de ejemplo para demostrar el funcionamiento del sistema
if __name__ == "__main__":
    # Creación de instancias
    estudiante1 = Estudiante("E001", "Emilio Senguana", 20, "Informática")
    estudiante2 = Estudiante("E002", "Maria Wisuma", 22, "Matemáticas")
    profesor1 = Profesor("P001", "Andrea Santii", 35, "Ciencias de la Computación")

    # Demostración de funcionalidades de estudiantes
    print("\n=== Demostración de Estudiantes ===")
    print(estudiante1.agregar_calificacion("Programación", 9.5))
    print(estudiante1.agregar_calificacion("Bases de Datos", 8.7))
    print(estudiante1.mostrar_info())

    # Demostración de funcionalidades de profesores
    print("\n=== Demostración de Profesores ===")
    print(profesor1.asignar_curso("Programación Orientada a Objetos"))
    print(profesor1.asignar_curso("Estructuras de Datos"))
    print(profesor1.mostrar_info())

    # Demostración de polimorfismo
    print("\n=== Demostración de Polimorfismo ===")
    personas = [estudiante1, estudiante2, profesor1]
    for persona in personas:
        print("\n", persona.mostrar_info())

    # Demostración de encapsulación
    print("\n=== Demostración de Encapsulación ===")
    print(f"Accediendo al nombre mediante property: {estudiante1.nombre}")
    # Intentar modificar un atributo privado directamente causaría error:
    # estudiante1.__calificaciones = {}  # Esto generaría un error