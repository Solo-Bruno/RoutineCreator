from connection import Connection
import tables
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

def main():
    conn = Connection.conn
    cursor = conn.cursor()


    "Init tables"
    #tables.initialization(conn, cursor)
    # ----------------------------------------------------------------------
    # CONFIGURACIÓN DE LA INTERFAZ (UI)
    # ----------------------------------------------------------------------
    # 1. Inicialización de la ventana principal
    ventana = tk.Tk()
    ventana.title("Creador de rutinas")
    ventana.geometry("1200x850") # Tamaño inicial de la ventana

    main_frame = ttk.Frame(ventana, padding="15 15 15 15")
    main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

    ttk.Label(main_frame, text="Dia:").grid(
        row=1, column=0, padx=5, pady=5, sticky=tk.W
    )

    dias = ['Lunes', 'Martes',  'Miercoles', 'Jueves', 'Viernes']

    combo_grupo = ttk.Combobox(main_frame, values=dias, width=28)
    combo_grupo.grid(row=1, column=1, padx=5, pady=5, sticky=(tk.W, tk.E))
    combo_grupo.set("Seleccione...")


    ventana.mainloop()


if __name__ == "__main__":
    main()