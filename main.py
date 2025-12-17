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

    "Init tables"

    tables.initialization(conn, cursor)
    Seed(conn).init()

    def crear_rutina():
        seleccionados = [nombre for nombre, var in dict_dias.items() if var.get()]
        notebook.select(1)

    def evento_tabla(event):
        """#TODO Evento disparado al interactuar con la tabla"""
        pass

    def validar_seleccion(*args):

        hay_seleccion = any(var.get() for var in dict_dias.values())
        hay_nombre = len(nombre_rutina.get().strip()) > 0
        if hay_seleccion and hay_nombre:
            btn_nuevo.config(state="normal")
            label_nota.pack_forget()
        else:
            btn_nuevo.config(state="disabled")
            label_nota.pack()

    """"
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

    def cambio_de_pagina(event):
        # Obtiene el ID de la pestaña actualmente seleccionada
        indice_actual = notebook.index(notebook.select())

        if indice_actual == 0:
            print("Navegando a la pestaña: Inicio")
        elif indice_actual == 1:
            print("Navegando a la pestaña: Datos")
    
    """
    # Datos a cargar
    tipo = ["PECTORALES", "PIERNAS", "GLÚTEOS", "TRICEPS", "ESPALDA", "BÍCEPS", "TRAPECIOS", "ABDOMINALES"]

    # ----------------------------------------------------------------------
    # CONFIGURACIÓN DE LA INTERFAZ (UI)
    # ----------------------------------------------------------------------
    # 1. Inicialización de la ventana principal
    root = tk.Tk()
    root.title("Gestor de Rutinas")
    root.geometry("1000x600")

    notebook = ttk.Notebook(root)
    notebook.pack(expand=True, fill='both')

    frame_inicio = ttk.Frame(notebook, padding="20")
    notebook.add(frame_inicio, text="Inicio")

    # FRAME INICIO
    frame_inicio.columnconfigure(0, weight=1)
    frame_inicio.columnconfigure(1, weight=1)
    frame_inicio.rowconfigure(0, weight=1)

    # Izquierda
    container_izq = ttk.Frame(frame_inicio)
    container_izq.grid(row=0, column=0, sticky="n", pady=50)
    ttk.Label(container_izq, text="Bienvenido", font=("Arial", 18, "bold")).pack(anchor="w")

    ttk.Label(container_izq, text="Nombre de la nueva rutina:", font=("Arial", 10)).pack(anchor="w", pady=(20, 5))
    nombre_rutina = tk.StringVar()
    nombre_rutina.trace_add("write", validar_seleccion)

    input_nombre = tk.Entry(container_izq, textvariable=nombre_rutina, font=("Arial", 12))
    input_nombre.pack(anchor="w", pady=(0, 15), fill="x")

    ttk.Label(container_izq, text="Seleccione los días de entrenamiento:", font=("Arial", 10)).pack(anchor="w",
                                                                                                    pady=(15, 5))
    frame_dias = ttk.Frame(container_izq)
    frame_dias.pack(anchor="w", pady=10)
    nombres_dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes"]
    dict_dias = {}
    for dia in nombres_dias:
        var = tk.BooleanVar(value=False)
        dict_dias[dia] = var

        cb = ttk.Checkbutton(
            frame_dias,
            text=dia,
            variable=var,
            command=validar_seleccion
        )
        cb.pack(side="left", padx=5)

    btn_nuevo = ttk.Button(container_izq, text="Nueva rutina", command=crear_rutina, state="disabled")
    btn_nuevo.pack(anchor="w", pady=20, ipadx=10, ipady=5)

    label_nota = ttk.Label(container_izq, text=" ⚠️Debe ingresar un nombre y seleccionar por lo menos un dia",
                           foreground="red", font=("Arial", 10, "bold"))
    label_nota.pack(anchor="w")

    #Derecha
    container_der = ttk.Frame(frame_inicio)
    container_der.grid(row=0, column=1, sticky="nsew", padx=20)
    ttk.Label(container_der, text="Últimas rutinas", font=("Arial", 12, "bold")).pack(anchor="w", pady=(0, 10))
    columnas_rutina = ("ID", "Fecha", "Nombre", "Estado")
    tabla_rutinas = ttk.Treeview(container_der, columns=columnas_rutina, show='headings', height=10)

    tabla_rutinas.heading("ID", text="ID")
    tabla_rutinas.heading("Fecha", text="Fecha")
    tabla_rutinas.heading("Nombre", text="Nombre")
    tabla_rutinas.heading("Estado", text="Estado")
    tabla_rutinas.column("ID", width=0, stretch=tk.NO)
    tabla_rutinas.column("Fecha", width=100)
    tabla_rutinas.column("Nombre", width=150)
    tabla_rutinas.column("Estado", width=100)

    tabla_rutinas.pack(expand=True, fill='both')




    tabla_rutinas.bind("<<TreeviewSelect>>", evento_tabla)

    ## /////////////////////////////////////////////////////////////////////////////////##

    #Frame Rutina
    frame_nueva_rutina = ttk.Frame(notebook, padding="20")
    notebook.add(frame_nueva_rutina, text="Nueva Rutina")

    ttk.Label(frame_nueva_rutina, text="Formulario para crear nueva rutina", font=("Arial", 14)).pack()

    root.mainloop()


if __name__ == "__main__":
    main()