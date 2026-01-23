import pandas as pd
from difflib import SequenceMatcher  # Para similitud fuzzy (opcional)

# Función para calcular similitud (0-1, donde 1 es idéntico)
def similitud(a, b):
    return SequenceMatcher(None, a.lower(), b.lower()).ratio()

def procesar_similitudes(df, datos_modificados, usar_fuzzy=False, umbral_fuzzy=0.8):
    """
    Procesa DATOS_MODIFICADOS comparándolo con df, y crea un DataFrame normalizado como base de datos.
    
    Parámetros:
    - df: DataFrame con columnas 'REGION', 'FORMATO', 'NOMBRE LOCAL'.
    - datos_modificados: Lista de listas como descrita.
    - usar_fuzzy: Booleano para usar similitud fuzzy en lugar de coincidencia exacta.
    - umbral_fuzzy: Umbral mínimo de similitud (0-1) para considerar coincidencia.
    
    Retorna:
    - Un DataFrame con columnas: 'REGION', 'FORMATO', 'NOMBRE_LOCAL', 'EQUIPO'.
    - Lista modificada (para referencia).
    """
    
    # Paso 1: Crear un diccionario indexado por 'NOMBRE LOCAL' (normalizado a minúsculas)
    df_indexado = {}
    for _, row in df.iterrows():
        formato = row[df.columns[1]].strip().lower().replace(" ", "")
        local = row[df.columns[2]].strip().lower().replace(" ", "")
        nombre_normalizado = formato+local
        df_indexado[nombre_normalizado] = {
            'REGION': row['REGION'],
            'FORMATO': row['FORMATO'],
            'NOMBRE_LOCAL': row['NOMBRE LOCAL']
        }
    # Paso 2: Procesar DATOS_MODIFICADOS
    datos_modificados_procesados = []
    for local in datos_modificados:
        nombre_original = local[0].strip()
        nombre_normalizado = local[0].strip().lower().replace(" ", "")
        equipos = local[1]  # Lista de equipos

        # Buscar coincidencia
        encontrado = False
        if usar_fuzzy:
            # Buscar la mejor coincidencia fuzzy
            mejor_similitud = 0
            mejor_clave = None
            for clave in df_indexado:
                sim = similitud(nombre_normalizado, clave)
                if sim > mejor_similitud and sim >= umbral_fuzzy:
                    mejor_similitud = sim
                    mejor_clave = clave
            if mejor_clave:
                info = df_indexado[mejor_clave]
                nueva_pos_0 = [info['REGION'], info['FORMATO'], info['NOMBRE_LOCAL']]
                encontrado = True
        else:
            # Coincidencia exacta
            if nombre_normalizado in df_indexado:
                info = df_indexado[nombre_normalizado]
                nueva_pos_0 = [info['REGION'], info['FORMATO'], info['NOMBRE_LOCAL']]
                encontrado = True
        
        if encontrado:
            datos_modificados_procesados.append([nueva_pos_0, equipos])
        else:
            print(f"Advertencia: No se encontró coincidencia para '{nombre_original}'. Dejando sin cambios.")
            datos_modificados_procesados.append(local)
    
    return datos_modificados_procesados
