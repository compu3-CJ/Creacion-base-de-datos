import tkinter as tk
from tkinter import filedialog

def seleccionar_archivos():
    """
    Abre una ventana emergente para seleccionar uno o varios archivos.
    Retorna una lista con las rutas de los archivos seleccionados.
    """
    # 1. Inicializamos Tkinter y ocultamos la ventana raíz
    root = tk.Tk()
    root.withdraw()

    # 2. Aseguramos que la ventana aparezca frente a las demás
    root.attributes('-topmost', True)

    # 3. Abrimos el diálogo (askopenfilenames permite selección múltiple)
    # Puedes filtrar por extensiones específicas en 'filetypes'
    rutas = filedialog.askopenfilenames(
        title="Selecciona los archivos para el algoritmo",
        filetypes=(("Archivos de datos", "*.csv *.txt *.xlsx *.xlsm"), ("Todos los archivos", "*.*"))
    )

    # 4. Destruimos la instancia de root para liberar memoria
    root.destroy()

    # Convertimos la tupla resultante en una lista para facilitar su uso
    return list(rutas)


