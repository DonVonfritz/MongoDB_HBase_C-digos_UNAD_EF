

#   Erick Fajardo


#   Proy PLANTAS EN RIESGO 

#   Estructura General, Familias. 
#   Creación de la Tabla. 
#   Establecer Conexión.
#   Eliminar Tabla.
#   Crear Nueva Tabla con Nuevas Características.


#   La tabla endangered_plants en HBase tiene la siguiente estructura:


#   Familia de columnas basic:

family: familia de la planta
scientific_name: nombre científico de la planta
common_names: nombres comunes de la planta

Familia de columnas threats:
national_threat_2002_2007: amenaza a nivel nacional en 2002-2007
national_threat_resolution_2010: resolución de amenaza a nivel nacional en 2010
national_threat_resolution_2014: resolución de amenaza a nivel nacional en 2014

Familia de columnas years:
1993: evaluación en 1993
2001: evaluación en 2001
2002: evaluación en 2002
2003: evaluación en 2003
2006: evaluación en 2006


#Paso 1: Creación de la tabla en HBase

import happybase
import pandas as pd

# Bloque principal de ejecución
try:
    # 1. Establecer conexión con HBase
    connection = happybase.Connection('localhost')
    print("Conexión establecida con HBase")
    
    # 2. Crear la tabla con las familias de columnas
    table_name = 'endangered_plants'
    families = {
        'basic': dict(),  # información básica de la planta
        'threats': dict(),  # información sobre amenazas
        'years': dict()  # información sobre años de evaluación
    }
    
    # Eliminar la tabla si ya existe
    if table_name.encode() in connection.tables():
        print(f"Eliminando tabla existente - {table_name}")
        connection.delete_table(table_name, disable=True)
    
    # Crear nueva tabla
    connection.create_table(table_name, families)
    table = connection.table(table_name)
    print("Tabla 'endangered_plants' creada exitosamente")
    
except Exception as e:
    print(f"Error al crear la tabla: {str(e)}")
finally:
    connection.close()
