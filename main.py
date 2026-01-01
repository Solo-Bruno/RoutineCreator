from connection import Connection
import tables
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from controller.exersiceController import ExcerciseController
from seeds.seed import Seed
from controller.routineController import routineController
from controller.dayController import DayController
from controller.day_exersiceController import DayExersiceController
from typing import List


def main():
    conn = Connection.conn
    cursor = conn.cursor()

    rout_con = routineController(conn)
    exer_con = ExcerciseController(conn)
    dey_con = DayController(conn)
    day_exercise = DayExersiceController(conn)


    "Init tables"

    tables.initialization(conn, cursor)
    Seed(conn).init()

    def crear_rutina():

        seleccionados = [nombre for nombre, var in dict_dias.items() if var.get()]
        routine = rout_con.crearRutina(input_nombre.get(), seleccionados)
        misDIas = dey_con.findDayByRoutineId(routine)
        renderizar_pestanas_rutina(misDIas, routine)
        root.current_routine_id = routine
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


    def actualizar_tabla(event):
        categoria_seleccionada = combo_filtro.get()
        datos_para_mostrar = exer_con.findByTypeExcercise(categoria_seleccionada)
        for item in tabla_selector.get_children():
            tabla_selector.delete(item)

        for fila in datos_para_mostrar:
            fila_con_accion = list(fila)  + ["✅ Agregar"]
            tabla_selector.insert('', tk.END, values=fila_con_accion)

    tablas_por_dia = {}

    def renderizar_pestanas_rutina(dias_seleccionados: List[str], routine_id: int):
        for tab in notebook_dias.tabs():
            notebook_dias.forget(tab)
        tablas_por_dia.clear()

        for dia in dias_seleccionados:
            tab_dia = ttk.Frame(notebook_dias, padding="10")
            notebook_dias.add(tab_dia, text=dia[1])

            tab_dia.columnconfigure(0, weight=1)
            tab_dia.rowconfigure(1, weight=1)

            ttk.Label(tab_dia, text=f"Rutina para el día: {dia[1]}", font=("Arial", 11, "bold")).grid(row=0, column=0,
                                                                                                   pady=10)
            cols_all = ("exercise_name", "series", "reps", "id_dia", "exercise_id", "day_exercise_id", "set_id", "Borrar")
            tabla_dia = ttk.Treeview(tab_dia, columns=cols_all, show="headings")

            columnas_visibles = {
                "exercise_name": "Ejercicio",
                "series": "Series",
                "reps": "Reps",
                "Borrar": "Acción"
            }

            for col, nombre in columnas_visibles.items():
                tabla_dia.heading(col, text=nombre)
                tabla_dia.column(col, width=100, anchor="center")

            tabla_dia.grid(row=1, column=0, sticky="nsew")

            columnas_ocultas = ("id_dia", "exercise_id", "day_exercise_id", "set_id")

            for col in columnas_ocultas:
                tabla_dia.heading(col, text="")
                tabla_dia.column(col, width=0, stretch=tk.NO)

            tabla_dia.grid(row=1, column=0, sticky="nsew")

            tabla_dia.bind("<ButtonRelease-1>", eliminar_day_exercise)

            tablas_por_dia[dia[1]] = {
                "id_dia": dia[0],
                "widget": tabla_dia,
                "routine_id": routine_id,
            }


    def cargar_ejercicio(inforeps, exercise_id, exercise_name):
        id_pestania_activa = notebook_dias.select()
        if not id_pestania_activa: return
        nombre_dia_actual = notebook_dias.tab(id_pestania_activa, "text")
        info_dia = tablas_por_dia.get(nombre_dia_actual)
        tabla_objetivo = info_dia["widget"]

        obj = day_exercise.insert(info_dia["id_dia"], exercise_id, inforeps["reps"],inforeps["series"], inforeps["peso"])

        valores_tupla = (
            exercise_name,
            obj["series"],
            obj["repeticiones"],
            info_dia["id_dia"],
            exercise_id,
            obj["day_exercise_id"],
            obj["set_id"],
            "❌"
        )

        tabla_objetivo.insert('', tk.END, values=valores_tupla)




    def accion_completado(event):
        item_id = tabla_selector.identify_row(event.y)
        if(item_id == "" or item_id == None): return
        valores = tabla_selector.item(item_id, 'values')
        excercise_id = valores[0]
        inforeps = abrir_modal_almacenar(valores[1])
        if inforeps != None:
            cargar_ejercicio(inforeps, excercise_id, valores[1])




    def abrir_modal_almacenar(ejercicio_nombre):
        modal = tk.Toplevel(root)
        modal.title("Capturar Datos")
        width, height = 400, 350
        main_x = root.winfo_x()
        main_y = root.winfo_y()
        main_width = root.winfo_width()
        main_height = root.winfo_height()
        pos_x = main_x + (main_width // 2) - (width // 2)
        pos_y = main_y + (main_height // 2) - (height // 2)
        modal.geometry(f"{width}x{height}+{pos_x}+{pos_y}")
        modal.grab_set()

        ttk.Label(modal, text=f"Datos para: {ejercicio_nombre}", font=("Arial", 10, "bold")).pack(pady=10)
        series_var = tk.IntVar(value=4)
        reps_var = tk.IntVar(value=12)
        peso_var = tk.IntVar(value=20)

        ttk.Label(modal, text="Series:").pack()
        ttk.Entry(modal, textvariable=series_var).pack(pady=5)
        ttk.Label(modal, text="Repeticiones:").pack()
        ttk.Entry(modal, textvariable=reps_var).pack(pady=5)
        ttk.Label(modal, text="Peso:").pack()
        ttk.Entry(modal, textvariable=peso_var).pack(pady=5)

        confirmado = tk.BooleanVar(value=False)

        def guardar():
            confirmado.set(True)
            modal.destroy()

        ttk.Button(modal, text="Guardar", command=guardar).pack()
        root.wait_window(modal)

        if confirmado.get():
            return {
                "series": series_var.get(),
                "reps": reps_var.get(),
                "peso": peso_var.get(),
            }
        else:
            return None


    def eliminar_day_exercise(event):
        tabla = event.widget
        item_id = tabla.identify_row(event.y)
        if(item_id == "" or item_id == None): return
        values = tabla.item(item_id, 'values')
        try:
            day_exercise.delete(values[5],values[6])
            tabla.delete(item_id)
        except Exception as e:
            raise e

    def genereted_PDF():

        routine_id = root.current_routine_id
        print(routine_id)
        ret = rout_con.obtener_datos_rutina_completa(routine_id)
        print(ret)


    """
    def cambio_de_pagina(event):
        # Obtiene el ID de la pestaña actualmente seleccionada
        indice_actual = notebook.index(notebook.select())

        if indice_actual == 0:
            print("Navegando a la pestaña: Inicio")
        elif indice_actual == 1:
            print("Navegando a la pestaña: Datos")
    
    datos = {
            id_routina
            name
            "days": {
                "day_exercise":{
                exersice_name
                series
                repeticiones
                }
            }
        }
    
    """
    # Datos a cargar
    tipo = ["PECTORALES", "PIERNAS", "GLÚTEOS", "TRICEPS", "ESPALDA", "BÍCEPS", "TRAPECIOS", "ABDOMINALES"]

    # ----------------------------------------------------------------------
    # CONFIGURACIÓN DE LA INTERFAZ (UI)
    # ----------------------------------------------------------------------
    # 1. Inicialización de la ventana principal
    root = tk.Tk()
    root.title("Gestor de Rutinas")
    root.geometry("1200x600")

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

    tabla_selector.bind("<ButtonRelease-1>", accion_completado)

    # --- PANEL DERECHO: Pestañas de Días (Verde/Naranja en tu diagrama) ---

    notebook_dias = ttk.Notebook(frame_nueva_rutina)
    notebook_dias.grid(row=0, column=1, sticky="nsew")

    btn_pdf = ttk.Button(frame_nueva_rutina, text="PDF", command=genereted_PDF)
    btn_pdf.grid(row=1, column=1, sticky="nsew")

    root.mainloop()


if __name__ == "__main__":
    main()