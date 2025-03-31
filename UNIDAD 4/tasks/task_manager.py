import tkinter as tk
from tkinter import ttk, messagebox
import random

class TaskApp:
    def __init__(self, root):
        """Inicializa la aplicación de lista de tareas"""
        self.root = root
        self.root.title("Gestor de Tareas")
        self.root.geometry("500x450")
        self.root.resizable(True, True)

        # Definir colores para estados de tareas
        self.normal_bg = "#ffffff"
        self.completed_bg = "#90ee90"  # Verde claro

        # Variable para mantener el estado de las tareas (0: pendiente, 1: completada)
        self.task_status = {}

        # Crear y configurar widgets
        self.setup_ui()

        # Asignar manejadores de eventos
        self.bind_events()

    def setup_ui(self):
        """Configura todos los elementos de la interfaz de usuario"""
        # Frame principal para organizar los elementos
        main_frame = ttk.Frame(self.root, padding="10")
        main_frame.pack(fill=tk.BOTH, expand=True)

        # Sección para añadir tareas
        add_frame = ttk.Frame(main_frame)
        add_frame.pack(fill=tk.X, pady=(0, 10))

        # Etiqueta y campo de entrada para nuevas tareas
        ttk.Label(add_frame, text="Nueva tarea:").pack(side=tk.LEFT, padx=(0, 5))

        self.task_entry = ttk.Entry(add_frame, width=40)
        self.task_entry.pack(side=tk.LEFT, padx=(0, 5), fill=tk.X, expand=True)
        self.task_entry.focus()  # Cursor en el campo de entrada al iniciar

        self.add_button = ttk.Button(add_frame, text="Añadir", command=self.add_task)
        self.add_button.pack(side=tk.LEFT)

        # Lista de tareas con scrollbar
        list_frame = ttk.Frame(main_frame)
        list_frame.pack(fill=tk.BOTH, expand=True)

        # Scrollbar para la lista de tareas
        scrollbar = ttk.Scrollbar(list_frame)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        # Lista para mostrar las tareas
        self.task_listbox = tk.Listbox(
            list_frame,
            height=15,
            selectmode=tk.SINGLE,
            yscrollcommand=scrollbar.set,
            font=("Arial", 11)
        )
        self.task_listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.config(command=self.task_listbox.yview)

        # Frame para botones de acción
        button_frame = ttk.Frame(main_frame)
        button_frame.pack(fill=tk.X, pady=(10, 0))

        # Botones para gestionar tareas
        self.complete_button = ttk.Button(
            button_frame,
            text="Marcar como Completada",
            command=self.toggle_task_status
        )
        self.complete_button.pack(side=tk.LEFT, padx=(0, 5))

        self.delete_button = ttk.Button(
            button_frame,
            text="Eliminar Tarea",
            command=self.delete_task
        )
        self.delete_button.pack(side=tk.LEFT)

    def bind_events(self):
        """Asigna todos los manejadores de eventos necesarios"""
        # Presionar Enter para añadir tarea
        self.task_entry.bind("<Return>", lambda event: self.add_task())

        # Doble clic en una tarea para cambiar su estado
        self.task_listbox.bind("<Double-1>", lambda event: self.toggle_task_status())

        # Selección de tarea para habilitar/deshabilitar botones
        self.task_listbox.bind("<<ListboxSelect>>", self.on_task_select)

    def add_task(self):
        """Añade una nueva tarea a la lista"""
        task_text = self.task_entry.get().strip()

        if task_text:
            # Generar un identificador único para la tarea
            task_id = random.randint(10000, 99999)
            while task_id in self.task_status:
                task_id = random.randint(10000, 99999)

            # Añadir la tarea a la lista y guardar su estado
            self.task_listbox.insert(tk.END, task_text)
            index = self.task_listbox.size() - 1
            self.task_status[index] = 0  # 0 = pendiente

            # Limpiar el campo de entrada
            self.task_entry.delete(0, tk.END)
            self.task_entry.focus()

            # Actualizar colores de la lista
            self.update_listbox_colors()
        else:
            messagebox.showwarning("Advertencia", "¡No puedes añadir una tarea vacía!")

    def toggle_task_status(self):
        """Cambia el estado de la tarea seleccionada entre pendiente y completada"""
        selected_indices = self.task_listbox.curselection()

        if selected_indices:
            index = selected_indices[0]

            # Cambiar estado de la tarea
            current_status = self.task_status.get(index, 0)
            self.task_status[index] = 1 if current_status == 0 else 0

            # Actualizar colores
            self.update_listbox_colors()

    def delete_task(self):
        """Elimina la tarea seleccionada de la lista"""
        selected_indices = self.task_listbox.curselection()

        if selected_indices:
            index = selected_indices[0]

            # Eliminar la tarea
            self.task_listbox.delete(index)

            # Actualizar el estado de las tareas (reasignar índices)
            new_status = {}
            for old_index, status in self.task_status.items():
                if old_index < index:
                    new_status[old_index] = status
                elif old_index > index:
                    new_status[old_index - 1] = status

            self.task_status = new_status

            # Actualizar colores
            self.update_listbox_colors()

    def update_listbox_colors(self):
        """Actualiza los colores de fondo de las tareas según su estado"""
        for i in range(self.task_listbox.size()):
            # Obtener el estado de la tarea
            status = self.task_status.get(i, 0)

            # Aplicar color según estado
            if status == 1:  # Completada
                self.task_listbox.itemconfig(i, {'bg': self.completed_bg})
            else:  # Pendiente
                self.task_listbox.itemconfig(i, {'bg': self.normal_bg})

    def on_task_select(self, event):
        """Maneja el evento de selección de una tarea"""
        # Verificar si hay alguna tarea seleccionada
        has_selection = len(self.task_listbox.curselection()) > 0

        # Esto podría usarse para habilitar/deshabilitar botones según sea necesario
        # Por ahora los botones siempre están habilitados cuando hay selección

if __name__ == "__main__":
    # Crear la ventana principal
    root = tk.Tk()

    # Inicializar la aplicación
    app = TaskApp(root)

    # Iniciar el bucle principal
    root.mainloop()