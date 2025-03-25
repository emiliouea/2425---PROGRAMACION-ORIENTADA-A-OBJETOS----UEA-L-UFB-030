import tkinter as tk
from tkinter import ttk, messagebox
from tkcalendar import DateEntry
from datetime import datetime

class AgendaPersonal:
    def __init__(self, ventana):
        self.ventana = ventana
        self.ventana.title("Mi Agenda Personal")
        self.ventana.geometry("600x500")

        # Estilo para mejorar la apariencia
        self.estilo = ttk.Style()
        self.estilo.configure("TLabel", font=("Arial", 10))
        self.estilo.configure("TButton", font=("Arial", 10))

        # Lista de eventos
        self.eventos = []

        # Configuración de frames
        self.configurar_frames()
        self.configurar_componentes()

    def configurar_frames(self):
        # Frame para lista de eventos
        self.frame_lista = ttk.Frame(self.ventana, padding="10")
        self.frame_lista.pack(fill=tk.BOTH, expand=True)

        # Frame para entrada de datos
        self.frame_entrada = ttk.Frame(self.ventana, padding="10")
        self.frame_entrada.pack(fill=tk.X)

        # Frame para botones
        self.frame_botones = ttk.Frame(self.ventana, padding="10")
        self.frame_botones.pack(fill=tk.X)

    def configurar_componentes(self):
        # Árbol para mostrar eventos
        self.tree = ttk.Treeview(self.frame_lista,
                                 columns=("Fecha", "Hora", "Descripción"),
                                 show="headings")
        self.tree.heading("Fecha", text="Fecha")
        self.tree.heading("Hora", text="Hora")
        self.tree.heading("Descripción", text="Descripción")
        self.tree.pack(fill=tk.BOTH, expand=True)

        # Scrollbar para el árbol
        scrollbar = ttk.Scrollbar(self.frame_lista,
                                  orient=tk.VERTICAL,
                                  command=self.tree.yview)
        self.tree.configure(yscroll=scrollbar.set)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        # Etiquetas y entradas
        ttk.Label(self.frame_entrada, text="Fecha:").grid(row=0, column=0, sticky="w")
        self.fecha_entry = DateEntry(self.frame_entrada,
                                     width=12,
                                     background='darkblue',
                                     foreground='white',
                                     date_pattern='yyyy-mm-dd')
        self.fecha_entry.grid(row=0, column=1, padx=5, pady=5)

        ttk.Label(self.frame_entrada, text="Hora:").grid(row=1, column=0, sticky="w")
        self.hora_entry = ttk.Entry(self.frame_entrada, width=15)
        self.hora_entry.grid(row=1, column=1, padx=5, pady=5)
        self.hora_entry.insert(0, "HH:MM")

        ttk.Label(self.frame_entrada, text="Descripción:").grid(row=2, column=0, sticky="w")
        self.descripcion_entry = ttk.Entry(self.frame_entrada, width=40)
        self.descripcion_entry.grid(row=2, column=1, padx=5, pady=5)

        # Botones
        ttk.Button(self.frame_botones, text="Agregar Evento",
                   command=self.agregar_evento).pack(side=tk.LEFT, padx=5)

        ttk.Button(self.frame_botones, text="Eliminar Evento",
                   command=self.eliminar_evento).pack(side=tk.LEFT, padx=5)

        ttk.Button(self.frame_botones, text="Salir",
                   command=self.ventana.quit).pack(side=tk.RIGHT, padx=5)

    def agregar_evento(self):
        try:
            fecha = self.fecha_entry.get()
            hora = self.hora_entry.get()
            descripcion = self.descripcion_entry.get()

            # Validaciones básicas
            if not fecha or not hora or not descripcion:
                messagebox.showwarning("Datos Incompletos",
                                       "Por favor, complete todos los campos.")
                return

            # Validar formato de hora
            datetime.strptime(hora, "%H:%M")

            # Agregar evento a la lista y al TreeView
            evento = (fecha, hora, descripcion)
            self.eventos.append(evento)
            self.tree.insert("", "end", values=evento)

            # Limpiar entradas
            self.fecha_entry.set_date(datetime.now())
            self.hora_entry.delete(0, tk.END)
            self.hora_entry.insert(0, "HH:MM")
            self.descripcion_entry.delete(0, tk.END)

        except ValueError:
            messagebox.showerror("Error", "Formato de hora inválido. Use HH:MM")

    def eliminar_evento(self):
        # Obtener elemento seleccionado
        seleccion = self.tree.selection()

        if not seleccion:
            messagebox.showwarning("Selección",
                                   "Seleccione un evento para eliminar.")
            return

        # Confirmar eliminación
        respuesta = messagebox.askyesno("Confirmar",
                                        "¿Está seguro de eliminar el evento?")

        if respuesta:
            for item in seleccion:
                # Eliminar del TreeView
                self.tree.delete(item)

def main():
    root = tk.Tk()
    app = AgendaPersonal(root)
    root.mainloop()

if __name__ == "__main__":
    main()