import re
from . import correcion_cambio as cc


def nombres_en_Mayus(data):
    cod = ["LT","Lt","MT","Mt","BT","Bt"]
    for i in cod:
        if i in data[0:5]:
            if '-' in data:
                # Caso con 2 guiones: dividir por el 2do guion
                sub_string = data.split("-")
                if len(sub_string) > 2 :
                    parts = data.split('-', 2)
                    return f"{parts[0]}-{parts[1]}-{parts[2].upper()}"
                else:
                    # Caso con guion: dividir por el primer guion
                    parts = data.split('-', 1)
                    return f"{parts[0]}-{parts[1].upper()}"
            # Caso código seguido de espacio y paréntesis
            match = re.match(r"^([A-Za-z0-9/]+)\s+(.*)", data)    
            if match:
                codigo, descripcion = match.groups()
                return f"{codigo} {descripcion.upper()}"
        
    return data.upper()

# Ingresar a los nombres
import copy

def cambio_nombres(lista_original):
    lista = copy.deepcopy(lista_original)
    lista2 = []
    for local in lista:
        lista2 = []
        for i in range(len(local[1])):            
            local[1][i] = nombres_en_Mayus(local[1][i])
            if "PRINCIPAL" in local[1][i]:
                local[1][i] = local[1][i].replace("-CONTROL PRINCIPAL", "")
                local[1][i] = local[1][i].replace("CONTROL PRINCIPAL-", "")
                local[1][i] = local[1][i].replace(" CONTROL PRINCIPAL", "")
                local[1][i] = local[1][i].replace("-PRINCIPAL", "")
                local[1][i] = local[1][i].replace(" PRINCIPAL", "")
                local[1][i] = local[1][i].replace("_PRINCIPAL", "")
            if "BACK UP" not in  local[1][i] :
                if "BACKUP" not in  local[1][i] :
                    if "PRACK" in local[1][i]:
                        local[1][i] = "RACK REFRIGERACIÓN"
                        
                    local[1][i] = local[1][i].replace("+", "/")
                    
                    for j in cc.cambios:
                        local[1][i] = local[1][i].replace(j[0],j[1])
                    
                    lista2 += [local[1][i]]
            
        local[1] = lista2
    return lista #,lista3