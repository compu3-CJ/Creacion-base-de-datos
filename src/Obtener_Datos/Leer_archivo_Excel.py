import pandas as pd

def leer_excel_a_dataframe(lista_archivo, hoja=None):
    """
    Lee múltiples archivos Excel y los fusiona en un solo DataFrame.

    Parámetros:
    lista_archivo (list): Lista de rutas de archivos Excel.
    hoja (str | int | None): Nombre o índice de la hoja.

    Retorna:
    pd.DataFrame
    """
    dataframes = []

    for ruta_archivo in lista_archivo:
        try:
            df = pd.read_excel(ruta_archivo, sheet_name=hoja)
            dataframes.append(df)

        except Exception as e:
            print(f"❌ Error leyendo {ruta_archivo}: {e}")

    if not dataframes:
        raise ValueError("No se pudo leer ningún archivo Excel.")

    # Fusión vertical (mismas columnas)
    if len(dataframes) > 1:
        df_final = pd.concat(dataframes, ignore_index=True)
        return df_final
    else:
        return dataframes[0]