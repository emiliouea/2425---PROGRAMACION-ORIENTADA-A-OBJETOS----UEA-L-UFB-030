import tkinter as tk
from tkinter import ttk, messagebox

class AplicacionTareas:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestor de Tareas")
        self.root.geometry("500x400")
        self.root.configure(bg="#f0f0f0")

        # Estilo
        self.configurar_estilo()

        # Variables
        self.tareas = []
        self.indice_seleccionado = None

        # Crear componentes
        self.crear_componentes()

        # Configurar atajos de teclado
        self.configurar_atajos()

    def configurar_estilo(self):
        self.estilo = ttk.Style()
        self.estilo.theme_use("clam")

        # Configuración para el Treeview (lista de tareas)
        self.estilo.configure("Treeview",
                              background="#ffffff",
                              foreground="#333333",
                              rowheight=25,
                              fieldbackground="#ffffff")
        self.estilo.map('Treeview',
                        background=[('selected', '#4a6984')])

        # Configuración para botones
        self.estilo.configure("TButton",
                              padding=6,
                              relief="flat",
                              background="#4a6984",
                              foreground="#ffffff")

        self.estilo.map('TButton',
                        background=[('active', '#5a7994')])

    def crear_componentes(self):
        # Frame principal
        frame_principal = ttk.Frame(self.root, padding="10")
        frame_principal.pack(fill=tk.BOTH, expand=True)

        # Frame superior para entrada y botón de añadir
        frame_superior = ttk.Frame(frame_principal)
        frame_superior.pack(fill=tk.X, pady=(0, 10))

        # Campo de entrada
        self.entrada_tarea = ttk.Entry(frame_superior, width=40, font=("Arial", 11))
        self.entrada_tarea.pack(side=tk.LEFT, padx=(0, 5), fill=tk.X, expand=True)
        self.entrada_tarea.focus()

        # Botón añadir
        self.boton_anadir = ttk.Button(frame_superior, text="Añadir", command=self.anadir_tarea)
        self.boton_anadir.pack(side=tk.RIGHT)

        # Frame para la lista de tareas
        frame_lista = ttk.Frame(frame_principal)
        frame_lista.pack(fill=tk.BOTH, expand=True)

        # Lista de tareas (Treeview)
        columnas = ("estado", "tarea")
        self.lista_tareas = ttk.Treeview(frame_lista, columns=columnas, show="headings", selectmode="browse")
        self.lista_tareas.heading("estado", text="Estado")
        self.lista_tareas.heading("tarea", text="Tarea")

        self.lista_tareas.column("estado", width=100, anchor=tk.CENTER)
        self.lista_tareas.column("tarea", width=400)

        # Configurar tag para tareas completadas
        self.lista_tareas.tag_configure("completada", foreground="#999999")

        # Scrollbar para la lista
        scrollbar = ttk.Scrollbar(frame_lista, orient=tk.VERTICAL, command=self.lista_tareas.yview)
        self.lista_tareas.configure(yscrollcommand=scrollbar.set)

        self.lista_tareas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        # Vincular eventos de selección
        self.lista_tareas.bind("<<TreeviewSelect>>", self.al_seleccionar)

        # Frame para botones de acciones
        frame_botones = ttk.Frame(frame_principal)
        frame_botones.pack(fill=tk.X, pady=(10, 0))

        # Botones para completar y eliminar
        self.boton_completar = ttk.Button(frame_botones, text="Marcar como Completada (C)",
                                          command=self.marcar_completada, state=tk.DISABLED)
        self.boton_completar.pack(side=tk.LEFT, padx=(0, 5))

        self.boton_eliminar = ttk.Button(frame_botones, text="Eliminar (D)",
                                         command=self.eliminar_tarea, state=tk.DISABLED)
        self.boton_eliminar.pack(side=tk.LEFT)

        # Frame para instrucciones
        frame_info = ttk.Frame(frame_principal)
        frame_info.pack(fill=tk.X, pady=(10, 0))

        # Etiqueta con instrucciones
        ttk.Label(frame_info, text="Atajos: Enter - Añadir, C - Completar, D - Eliminar, Esc - Salir",
                  font=("Arial", 9), foreground="#666666").pack(side=tk.LEFT)

    def configurar_atajos(self):
        # Tecla Enter para añadir tarea
        self.entrada_tarea.bind("<Return>", lambda event: self.anadir_tarea())

        # Tecla C para marcar como completada
        self.root.bind("<KeyPress-c>", lambda event: self.marcar_completada())

        # Tecla D para eliminar
        self.root.bind("<KeyPress-d>", lambda event: self.eliminar_tarea())

        # Tecla Delete como alternativa para eliminar
        self.root.bind("<Delete>", lambda event: self.eliminar_tarea())

        # Tecla Escape para cerrar
        self.root.bind("<Escape>", lambda event: self.confirmar_salida())

    def anadir_tarea(self):
        texto_tarea = self.entrada_tarea.get().strip()
        if texto_tarea:
            # Insertar en la lista
            id_item = self.lista_tareas.insert("", tk.END, values=("Pendiente", texto_tarea))
            # Guardar en la lista interna
            self.tareas.append({"id": id_item, "texto": texto_tarea, "completada": False})
            # Limpiar campo de entrada
            self.entrada_tarea.delete(0, tk.END)
        else:
            messagebox.showwarning("Entrada vacía", "Por favor, ingresa una tarea.")

    def al_seleccionar(self, event):
        seleccion = self.lista_tareas.selection()
        if seleccion:
            # Habilitar botones si hay selección
            self.boton_completar.config(state=tk.NORMAL)
            self.boton_eliminar.config(state=tk.NORMAL)
            # Guardar índice seleccionado
            self.indice_seleccionado = self.obtener_indice_por_id(seleccion[0])
        else:
            # Deshabilitar botones si no hay selección
            self.boton_completar.config(state=tk.DISABLED)
            self.boton_eliminar.config(state=tk.DISABLED)
            self.indice_seleccionado = None

    def marcar_completada(self):
        if self.indice_seleccionado is not None:
            tarea = self.tareas[self.indice_seleccionado]
            id_item = tarea["id"]

            # Cambiar estado
            if tarea["completada"]:
                nuevo_estado = "Pendiente"
                tarea["completada"] = False
            else:
                nuevo_estado = "Completada ✓"
                tarea["completada"] = True

            # Actualizar en la lista visual
            self.lista_tareas.item(id_item, values=(nuevo_estado, tarea["texto"]))

            # Cambiar el estilo según el estado
            if tarea["completada"]:
                self.lista_tareas.item(id_item, tags=("completada",))
            else:
                self.lista_tareas.item(id_item, tags=(""))

    def eliminar_tarea(self):
        if self.indice_seleccionado is not None:
            # Obtener ID del elemento a eliminar
            id_item = self.tareas[self.indice_seleccionado]["id"]

            # Eliminar de la lista visual
            self.lista_tareas.delete(id_item)

            # Eliminar de la lista interna
            self.tareas.pop(self.indice_seleccionado)

            # Resetear selección
            self.indice_seleccionado = None

            # Desactivar botones
            self.boton_completar.config(state=tk.DISABLED)
            self.boton_eliminar.config(state=tk.DISABLED)

    def obtener_indice_por_id(self, id_item):
        for i, tarea in enumerate(self.tareas):
            if tarea["id"] == id_item:
                return i
        return None

    def confirmar_salida(self):
        if messagebox.askokcancel("Salir", "¿Deseas cerrar la aplicación?"):
            self.root.destroy()

def main():
    root = tk.Tk()
    app = AplicacionTareas(root)
    root.mainloop()

if __name__ == "__main__":
    main()