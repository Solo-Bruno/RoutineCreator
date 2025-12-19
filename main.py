from connection import Connection
import tables
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from controller.excersiceController import ExcerciseController
from seeds.seed import Seed
from controller.routineController import routineController
from controller.dayController import dayController
from typing import List


def main():
    conn = Connection.conn
    cursor = conn.cursor()

    rout_con = routineController(conn)
    excer_con = ExcerciseController(conn)
    dey_con = dayController(conn)

    "Init tables"

    tables.initialization(conn, cursor)
    Seed(conn).init()

    def crear_rutina():
        seleccionados = [nombre for nombre, var in dict_dias.items() if var.get()]
        routine = rout_con.crearRutina(input_nombre.get(), seleccionados)
        misDIas = dey_con.findDayByRoutineId(routine)
        print(misDIas)
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
        categoria_seleccionada = combo_filtro.get()
        datos_para_mostrar = excer_con.findByTypeExcercise(categoria_seleccionada)
        print("Categoria seleccionada: ", categoria_seleccionada)
        for item in tabla_selector.get_children():
            tabla_selector.delete(item)

        for fila in datos_para_mostrar:
            fila_con_accion = list(fila)  + ["✅ Agregar"]
            tabla_selector.insert('', tk.END, values=fila_con_accion)

    tablas_por_dia = {}

    def renderizar_pestanas_rutina(dias_seleccionados: List[str]):
        for tab in notebook_dias.tabs():
            notebook_dias.forget(tab)
        tablas_por_dia.clear()

        # 3. Crear una pestaña por cada día seleccionado
        for dia in dias_seleccionados:
            tab_dia = ttk.Frame(notebook_dias, padding="10")
            notebook_dias.add(tab_dia, text=dia)

            # Configurar layout de la pestaña
            tab_dia.columnconfigure(0, weight=1)
            tab_dia.rowconfigure(1, weight=1)

            ttk.Label(tab_dia, text=f"Rutina para el día: {dia}", font=("Arial", 11, "bold")).grid(row=0, column=0,
                                                                                                   pady=10)

            # Tabla interactiva para este día específico
            cols_rut = ("Ejercicio", "Series", "Reps", "Nota")
            tabla_dia = ttk.Treeview(tab_dia, columns=cols_rut, show="headings")

            for col in cols_rut:
                tabla_dia.heading(col, text=col)
                tabla_dia.column(col, width=80)

            tabla_dia.grid(row=1, column=0, sticky="nsew")

            # Guardamos la referencia de la tabla asociada a este día
            tablas_por_dia[dia] = tabla_dia

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

    """
    #Nuevo Frame
    frame_nueva_rutina.columnconfigure(0, weight=1)
    frame_nueva_rutina.columnconfigure(1, weight=1)
    frame_nueva_rutina.rowconfigure(0, weight=1)

    #Izquierda
    container_ejercicios = ttk.LabelFrame(frame_nueva_rutina, text=" Banco de Ejercicios ", padding="10")
    container_ejercicios.grid(row=0, column=0, sticky="nsew", padx=(0, 10))

    # Configuración interna del panel izquierdo
    container_ejercicios.columnconfigure(0, weight=1)
    container_ejercicios.rowconfigure(2, weight=1)
    ttk.Label(container_ejercicios, text="Grupo muscular:", font=("Arial", 10, "bold")).grid(row=0, column=0,
                                                                                             sticky="w", pady=5)

    combo_filtro = ttk.Combobox(container_ejercicios, values=tipo,
                                state="readonly")
    combo_filtro.grid(row=1, column=0, sticky="ew", pady=5)

    combo_filtro.bind("<<ComboboxSelected>>", actualizar_tabla)

    columnas = ("Id","Nombre", "Tipo", "Imagen", "Action")
    tabla_selector = ttk.Treeview(container_ejercicios, columns=columnas, show="headings", height=15)
    tabla_selector.heading("Id", text="Id")
    tabla_selector.heading("Nombre", text="Nombre")
    tabla_selector.heading("Tipo", text="Tipo")
    tabla_selector.heading("Imagen", text="Imagen")
    tabla_selector.heading("Action", text="Tick Correcto")
    tabla_selector.grid(row=2, column=0, sticky="nsew", pady=10)

    tabla_selector.column("Id", width=0, stretch=tk.NO)
    tabla_selector.column("Imagen", width=0, stretch=tk.NO)

    # --- PANEL DERECHO: Pestañas de Días (Verde/Naranja en tu diagrama) ---
    # Aquí creamos un Notebook interno que contendrá los días
    notebook_dias = ttk.Notebook(frame_nueva_rutina)
    notebook_dias.grid(row=0, column=1, sticky="nsew")
|   """
    root.mainloop()


if __name__ == "__main__":
    main()