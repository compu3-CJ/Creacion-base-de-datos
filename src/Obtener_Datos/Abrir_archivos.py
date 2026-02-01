import tkinter as tk
from tkinter import filedialog
import os
import glob

def obtener_archivos_carpeta(carpeta_path, extension='*'):
    """
    Obtiene todas las rutas de archivos en una carpeta específica.
    
    Parámetros:
    - carpeta_path (str): Ruta de la carpeta a buscar
    - extension (str): Extensión de archivos a buscar (por defecto '*' para todos)
                      Ejemplos: '*.csv', '*.txt', '*.xlsx'
    
    Retorna:
    - Lista de rutas completas de los archivos encontrados
    """
    if not os.path.exists(carpeta_path):
        raise FileNotFoundError(f"La carpeta no existe: {carpeta_path}")
    
    patron = os.path.join(carpeta_path, extension)
    archivos = glob.glob(patron)
    
    # Ordenar alfabéticamente
    archivos.sort()
    
    print(f"Se encontraron {len(archivos)} archivos en '{carpeta_path}':")
    for archivo in archivos:
        print(f"  - {os.path.basename(archivo)}")
    
    return archivos

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


