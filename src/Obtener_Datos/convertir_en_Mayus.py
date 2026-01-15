import re
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