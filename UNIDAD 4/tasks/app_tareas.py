import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import random  # Para generar IDs aleatorios

class GestorTareas:
    def __init__(self, ventana):
        # Configuración básica de la ventana
        self.ventana = ventana
        self.ventana.title("Mi Gestor de Tareas")
        self.ventana.geometry("580x400")
        self.ventana.resizable(True, True)

        # Variables para los campos
        self.nombre_tarea = tk.StringVar()
        self.desc_tarea = tk.StringVar()

        # Lista para guardar las tareas (podría ser un diccionario o una BD en una app real)
        self.lista_tareas = []

        # ID para las tareas - lo usaré para hacer seguimiento interno
        self.contador_id = 1000

        # Iniciar la interfaz
        self.crear_interfaz()

    def crear_interfaz(self):
        # Marco principal con un poco de padding
        marco = ttk.Frame(self.ventana, padding=8)
        marco.pack(fill=tk.BOTH, expand=True)

        # Sección para agregar tareas
        seccion_agregar = ttk.LabelFrame(marco, text="Agregar Nueva Tarea", padding=10)
        seccion_agregar.pack(fill=tk.X, padx=5, pady=5)

        # Fila 1 - Nombre de la tarea
        ttk.Label(seccion_agregar, text="Tarea:").grid(row=0, column=0, sticky=tk.W, padx=5, pady=5)
        campo_nombre = ttk.Entry(seccion_agregar, textvariable=self.nombre_tarea, width=30)
        campo_nombre.grid(row=0, column=1, padx=5, pady=5)
        campo_nombre.focus()  # Poner el foco aquí al iniciar

        # Fila 2 - Descripción
        ttk.Label(seccion_agregar, text="Detalles:").grid(row=1, column=0, sticky=tk.W, padx=5, pady=5)
        ttk.Entry(seccion_agregar, textvariable=self.desc_tarea, width=50).grid(
            row=1, column=1, columnspan=2, padx=5, pady=5, sticky=tk.W+tk.E)

        # Fila 3 - Botones
        marco_botones = ttk.Frame(seccion_agregar)
        marco_botones.grid(row=2, column=0, columnspan=3, pady=8)

        # Botón agregar con un poco de estilo
        btn_agregar = ttk.Button(
            marco_botones,
            text="➕ Agregar",
            command=self.agregar_nueva_tarea
        )
        btn_agregar.pack(side=tk.LEFT, padx=5)

        # Atajo de teclado para agregar (Enter)
        self.ventana.bind('<Return>', lambda event: self.agregar_nueva_tarea())

        # Botón limpiar campos
        ttk.Button(
            marco_botones,
            text="🧹 Limpiar",
            command=self.limpiar_campos
        ).pack(side=tk.LEFT, padx=5)

        # Sección para mostrar las tareas
        seccion_tareas = ttk.LabelFrame(marco, text="Mis Tareas", padding=10)
        seccion_tareas.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)

        # Tabla para las tareas
        columnas = ("nombre", "descripcion")
        self.tabla = ttk.Treeview(seccion_tareas, columns=columnas, show="headings", selectmode="browse")

        # Configurar columnas
        self.tabla.heading("nombre", text="Tarea")
        self.tabla.heading("descripcion", text="Descripción")

        # Ajustar el ancho
        self.tabla.column("nombre", width=150, minwidth=100)
        self.tabla.column("descripcion", width=350)

        # Barra de desplazamiento
        barra_scroll = ttk.Scrollbar(seccion_tareas, orient=tk.VERTICAL, command=self.tabla.yview)
        self.tabla.configure(yscrollcommand=barra_scroll.set)

        # Colocar tabla y scrollbar
        self.tabla.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        barra_scroll.pack(side=tk.RIGHT, fill=tk.Y)



        # Marco para los botones de acción sobre la tabla
        marco_acciones = ttk.Frame(marco)
        marco_acciones.pack(fill=tk.X, padx=5, pady=(0, 5))

        # Botón eliminar
        ttk.Button(
            marco_acciones,
            text="🗑️ Eliminar",
            command=self.eliminar_tarea
        ).pack(side=tk.RIGHT, padx=5)

    def agregar_nueva_tarea(self):
        # Obtener los datos y quitar espacios extra
        nombre = self.nombre_tarea.get().strip()
        descripcion = self.desc_tarea.get().strip()

        # Comprobar que hay un nombre (obligatorio)
        if not nombre:
            messagebox.showwarning("Atención", "¡Debes poner un nombre a la tarea!")
            return

        # Añadir a mi lista interna y a la tabla visual
        # ID aleatorio para esta tarea (solo interno)
        id_tarea = self.contador_id
        self.contador_id += 1

        self.lista_tareas.append({
            "id": id_tarea,
            "nombre": nombre,
            "descripcion": descripcion
        })

        # Actualizar la tabla - guardaré el id como un valor oculto para referencia
        self.tabla.insert("", tk.END, iid=str(id_tarea), values=(nombre, descripcion))

        # Limpiar después de añadir
        self.limpiar_campos()

    def limpiar_campos(self):
        # Borrar contenido de los campos
        self.nombre_tarea.set("")
        self.desc_tarea.set("")

    def eliminar_tarea(self):
        # Ver si hay algo seleccionado
        seleccion = self.tabla.selection()

        if not seleccion:
            messagebox.showinfo("Selección", "Primero selecciona una tarea para eliminar")
            return

        # Pedir confirmación - un toque personal
        confirmar = messagebox.askyesno(
            "Confirmar eliminación",
            "¿Seguro que quieres eliminar esta tarea?",
            icon="warning"
        )

        if confirmar:
            # Eliminar de la tabla
            for item in seleccion:
                self.tabla.delete(item)

                # También eliminar de mi lista interna
                # En una app real, esto sería más sofisticado
                id_a_borrar = int(item)
                self.lista_tareas = [t for t in self.lista_tareas if t["id"] != id_a_borrar]




# Iniciar la aplicación
if __name__ == "__main__":
    # Crear la ventana principal
    root = tk.Tk()

    # Un poco de estilo global
    estilo = ttk.Style()
    estilo.configure('TButton', font=('Segoe UI', 9))

    # Crear la aplicación
    app = GestorTareas(root)

    # Iniciar el bucle principal
    root.mainloop()