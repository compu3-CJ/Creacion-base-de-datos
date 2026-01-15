from . import correcion_cambio as cc


def procesar_Data(archivos):
    contenido = []
    for ruta in archivos:
        try:
            with open(ruta, "r",encoding='utf-8') as file:
                # Eliminar dobles saltos de linea
                datos = file.read().replace("\n\n","\n")
                # Separo contenido por cada salto de linea
                datos = datos.split("\n")
                # Extraigo los datos de nombre y equipos de la linea 2 y 4
                datos = datos[2:5:2]
                # Elimino ; del nombre del local
                datos[0] = datos[0].replace(";","")
                # Separo los nombres de los equipos con el caranter ';' y elimino ultimo espacio en blanco 
                for j in cc.correcciones:
                    if j in cc.correcciones[0:4]:
                        datos[1] = datos[1].replace(j, "-")
                    else:
                        datos[1] = datos[1].replace(j, "")
                
                for x in cc.cambios:
                    datos[1] = datos[1].replace(x[0], x[1])
                
                datos[1] = datos[1].split(";")
                datos[1].pop()
                
                # Modificar algo de cada nombre del equipo
                # for y in datos[1]:
                
                
                # Guardo los datos procesados
                contenido.append(datos)        
    
        except Exception as e:
            print(type(e).__name__, e)
    
    return contenido