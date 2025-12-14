from connection import Connection
import tables
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

from seeds.seed import Seed
from classes.excercise import Excercise


def main():
    conn = Connection.conn
    cursor = conn.cursor()

    #Seed(conn).init()

    "Init tables"

    # tables.initialization(conn, cursor)

    def actualizar_tabla(event):
        categoria_seleccionada = combo_categorias.get()
        datos_para_mostrar = Excercise(conn).findByType(categoria_seleccionada)
        print("Categoria seleccionada: ", categoria_seleccionada)
        for item in tabla_datos.get_children():
            tabla_datos.delete(item)

        for fila in datos_para_mostrar:
            fila_con_accion = list(fila)  + ["✅ Agregar"]
            tabla_datos.insert('', tk.END, values=fila_con_accion)

    def accion_completado(event):

        item_id = tabla_datos.identify_row(event.y)
        columna_id = tabla_datos.identify_column(event.x)

        print("Actualizando tabla", item_id, columna_id)
        valores = tabla_datos.item(item_id, 'values')
        producto = valores[0]
        print("Producto: ", producto)
        print("Valor: ", valores)

    # ----------------------------------------------------------------------
    # CONFIGURACIÓN DE LA INTERFAZ (UI)
    # ----------------------------------------------------------------------
    # 1. Inicialización de la ventana principal
    ventana = tk.Tk()
    ventana.title("Creador de rutinas")
    ventana.geometry("1200x850") # Tamaño inicial de la ventana


    frame = ttk.Frame(ventana, padding="10")
    frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

    ventana.columnconfigure(0, weight=1)
    ventana.rowconfigure(0, weight=1)

    frame.columnconfigure(0, weight=1)
    frame.columnconfigure(1, weight=1)
    frame.rowconfigure(2, weight=1)

    style = ttk.Style()
    style.configure("Treeview.Heading", font=('Arial', 10, 'bold'))
    style.configure("Treeview", rowheight=25, font=('Arial', 10))

    tipo = ["PECTORALES", "PIERNAS", "GLÚTEOS", "TRICEPS", "ESPALDA", "BÍCEPS", "TRAPECIOS", "ABDOMINALES"]

    ttk.Label(frame, text="Selecciona un grupo Muscular:").grid(row=0, column=0, padx=5, pady=5, sticky='w')

    # 1. Combobox
    combo_categorias = ttk.Combobox(frame, values=tipo, state="readonly", width=25)
    combo_categorias.grid(row=0, column=1, padx=5, pady=5, sticky='ew')
    combo_categorias.set(tipo[0])

    combo_categorias.bind("<<ComboboxSelected>>", actualizar_tabla)

    columnas = ("Id","Nombre", "Tipo", "Imagen", "Action")




    tabla_datos = ttk.Treeview(frame, columns=columnas, show='headings', height=10)
    tabla_datos.grid(row=1, column=0, columnspan=2, padx=5, pady=10, sticky='nsew')
    tabla_datos.heading("Id", text="Id")
    tabla_datos.heading("Nombre", text="Nombre")
    tabla_datos.heading("Tipo", text="Tipo")
    tabla_datos.heading("Imagen", text="Imagen")
    tabla_datos.heading("Action", text="Tick Correcto")

    tabla_datos.column("Id", width=0, stretch=tk.NO)
    tabla_datos.column("Imagen", width=0, stretch=tk.NO)

    scrollbar = ttk.Scrollbar(frame, orient=tk.VERTICAL, command=tabla_datos.yview)
    scrollbar.grid(row=1, column=2, sticky='ns')
    tabla_datos.configure(yscrollcommand=scrollbar.set)

    frame.columnconfigure(1, weight=1)
    ventana.columnconfigure(0, weight=1)
    ventana.rowconfigure(0, weight=1)
    frame.rowconfigure(1, weight=1)

    tabla_datos.bind("<ButtonRelease-1>", accion_completado)

    ventana.mainloop()


if __name__ == "__main__":
    main()