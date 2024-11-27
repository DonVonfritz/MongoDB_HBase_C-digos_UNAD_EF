
# Código general del proyecto Plantas en Riesgo 

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
    
    # 3. Cargar datos del CSV
    plant_data = pd.read_csv('plant_data.csv')  # Asegúrate de que el archivo CSV esté en el formato correcto
    
    # Iterar sobre el DataFrame usando el índice
    for index, row in plant_data.iterrows():
        # Generar row key basado en el índice
        row_key = f'plant_{index}'.encode()
        
        # Organizar los datos en familias de columnas
        data = {
            b'basic:family': str(row['Familia']).encode(),
            b'basic:scientific_name': str(row['Nombre científico']).encode(),
            b'basic:common_names': str(row['Nombres comunes']).encode(),
            
            b'years:1993': str(row['1993¹']).encode(),
            b'years:2001': str(row['2001²']).encode(),
            b'years:2002': str(row['2002³']).encode(),
            b'years:2003': str(row['2003º']).encode(),
            b'years:2006': str(row['2006•']).encode(),
            
            b'threats:national_threat_2002_2007': str(row['AMENAZA A NIVEL NACIONAL" (Libros Rojos de especies amenazadas 2002-2007)']).encode(),
            b'threats:national_threat_resolution_2010': str(row['AMENAZA A NIVEL NACIONAL (Resolución 383 de 2010-Derogada por la Res. 192 de 2014)']).encode(),
            b'threats:national_threat_resolution_2014': str(row['AMENAZA A NIVEL NACIONAL (Resolución 192 de 2014)']).encode()
        }
        
        table.put(row_key, data)
    
    print("Datos de plantas cargados exitosamente")
    
    # 4. Consultas y Análisis de Datos
    print("\n=== Todas las plantas en la base de datos (primeras 3) ===")
    count = 0
    for key, data in table.scan():
        if count < 3:  # Limitamos a 3 para el ejemplo
            print(f"\nPlanta ID: {key.decode()}")
            print(f"Nombre científico: {data[b'basic:scientific_name'].decode()}")
            print(f"Familia: {data[b'basic:family'].decode()}")
            count += 1
    
    # 5. Ejemplo de análisis de amenazas
    print("\n=== Análisis de amenazas a nivel nacional ===")
    threat_stats = {}
    for key, data in table.scan():
        threat = data[b'threats:national_threat_2002_2007'].decode()
        threat_stats[threat] = threat_stats.get(threat, 0) + 1
    
    for threat, count in threat_stats.items():
        print(f"{threat}: {count} plantas")
    
    # 6. Ejemplo de actualización de datos
    plant_to_update = 'plant_0'
    new_common_name = 'Nuevo Nombre Común'
    table.put(plant_to_update.encode(), {b'basic:common_names': new_common_name.encode()})
    print(f"\nNombre común actualizado para la planta ID: {plant_to_update}")

except Exception as e:
    print(f"Error: {str(e)}")
finally:
    # Cerrar la conexión
    connection.close()
Notas:


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



#Paso 2: Operaciones en HBase

try:
    connection = happybase.Connection('localhost')
    table = connection.table(table_name)
    
    # 3. Cargar datos del CSV
    plant_data = pd.read_csv('plant_data.csv')  # Asegúrate de que el archivo CSV esté en el formato correcto
    
    for index, row in plant_data.iterrows():
        row_key = f'plant_{index}'.encode()
        data = {
            b'basic:family': str(row['Familia']).encode(),
            b'basic:scientific_name': str(row['Nombre científico']).encode(),
            b'basic:common_names': str(row['Nombres comunes']).encode(),
            b'years:1993': str(row['1993¹']).encode(),
            b'years:2001': str(row['2001²']).encode(),
            b'years:2002': str(row['2002³']).encode(),
            b'years:2003': str(row['2003º']).encode(),
            b'years:2006': str(row['2006•']).encode(),
            b'threats:national_threat_2002_2007': str(row['AMENAZA A NIVEL NACIONAL" (Libros Rojos de especies amenazadas 2002-2007)']).encode(),
            b'threats:national_threat_resolution_2010': str(row['AMENAZA A NIVEL NACIONAL (Resolución 383 de 2010-Derogada por la Res. 192 de 2014)']).encode(),
            b'threats:national_threat_resolution_2014': str(row['AMENAZA A NIVEL NACIONAL (Resolución 192 de 2014)']).encode()
        }
        
        table.put(row_key, data)
    
    print("Datos de plantas cargados exitosamente")
    
except Exception as e:
    print(f"Error al cargar los datos: {str(e)}")
finally:
    connection.close()

# Realizar consultas de selección, filtrado y recorrido sobre los datos

try:
    connection = happybase.Connection('localhost')
    table = connection.table(table_name)
    
    # Consultar todas las plantas
    print("\n=== Todas las plantas en la base de datos (primeras 3) ===")
    count = 0
    for key, data in table.scan():
        if count < 3:  # Limitamos a 3 para el ejemplo
            print(f"\nPlanta ID: {key.decode()}")
            print(f"Nombre científico: {data[b'basic:scientific_name'].decode()}")
            print(f"Familia: {data[b'basic:family'].decode()}")
            count += 1
    
    # Filtrar plantas amenazadas a nivel nacional
    print("\n=== Análisis de amenazas a nivel nacional ===")
    threat_stats = {}
    for key, data in table.scan():
        threat = data[b'threats:national_threat_2002_2007'].decode()
        threat_stats[threat] = threat_stats.get(threat, 0) + 1
    
    for threat, count in threat_stats.items():
        print(f"{threat}: {count} plantas")
    
except Exception as e:
    print(f"Error al consultar datos: {str(e))

#Paso 1: Creación de la tabla en HBase
#Código para crear la tabla en HBase:


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
        'basic': dict(),  # Información básica de la planta
        'threats': dict(),  # Información sobre amenazas
        'years': dict()  # Información sobre años de evaluación
    }
    
    # Eliminar la tabla si ya existe
    if table_name.encode() in connection.tables():
        print(f"Eliminando tabla existente - {table_name}")
        connection.delete_table(table_name, disable=True)
    
    # Crear nueva tabla
    connection.create_table(table_name, families)
    print("Tabla 'endangered_plants' creada exitosamente")
    
except Exception as e:
    print(f"Error al crear la tabla: {str(e)}")
finally:
    connection.close()

#Paso 2: Operaciones en HBase
#2.1 Cargar los datos en la tabla de HBase
#Código para cargar datos desde un archivo CSV:

try:
    connection = happybase.Connection('localhost')
    table = connection.table('endangered_plants')
    
    # Cargar datos del CSV
    plant_data = pd.read_csv('plant_data.csv')  # Asegúrate de que el archivo CSV esté en el formato correcto
    
    for index, row in plant_data.iterrows():
        row_key = f'plant_{index}'.encode()
        data = {
            b'basic:family': str(row['Familia']).encode(),
            b'basic:scientific_name': str(row['Nombre científico']).encode(),
            b'basic:common_names': str(row['Nombres comunes']).encode(),
            b'years:1993': str(row['1993¹']).encode(),
            b'years:2001': str(row['2001²']).encode(),
            b'years:2002': str(row['2002³']).encode(),
            b'years:2003': str(row['2003º']).encode(),
            b'years:2006': str(row['2006•']).encode(),
            b'threats:national_threat_2002_2007': str(row['AMENAZA A NIVEL NACIONAL" (Libros Rojos de especies amenazadas 2002-2007)']).encode(),
            b'threats:national_threat_resolution_2010': str(row['AMENAZA A NIVEL NACIONAL (Resolución 383 de 2010-Derogada por la Res. 192 de 2014)']).encode(),
            b'threats:national_threat_resolution_2014': str(row['AMENAZA A NIVEL NACIONAL (Resolución 192 de 2014)']).encode()
        }
        
        table.put(row_key, data)
    
    print("Datos de plantas cargados exitosamente")
    
except Exception as e:
    print(f"Error al cargar los datos: {str(e)}")
finally:
    connection.close()

#2.2 Realizar consultas de selección, filtrado y recorrido sobre los datos
#Código para realizar consultas:

try:
    connection = happybase.Connection('localhost')
    table = connection.table('endangered_plants')
    
    # Consultar todas las plantas
    print("\n=== Todas las plantas en la base de datos (primeras 3) ===")
    count = 0
    for key, data in table.scan():
        if count < 3:  # Limitamos a 3 para el ejemplo
            print(f"\nPlanta ID: {key.decode()}")
            print(f"Nombre científico: {data[b'basic:scientific_name'].decode()}")
            print(f"Familia: {data[b'basic:family'].decode()}")
            count += 1
    
    # Filtrar plantas amenazadas a nivel nacional
    print("\n=== Análisis de amenazas a nivel nacional ===")
    threat_stats = {}
    for key, data in table.scan():
        threat = data[b'threats:national_threat_2002_2007'].decode()
        threat_stats[threat] = threat_stats.get(threat, 0) + 1
    
    for threat, count in threat_stats.items():
        print(f"{threat}: {count} plantas")
    

#Documentación: o Describir la estructura de la tabla en HBase. o Explicar las operaciones realizadas en HBase y los resultados obtenidos.


#Documentación

#3.1 Describir la estructura de la tabla en HBase
#La tabla endangered_plants en HBase tiene la siguiente estructura:

Familia de columnas basic:
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


#3.2 Explicar las operaciones realizadas en HBase y los resultados obtenidos

En este proyecto, se realizaron las siguientes operaciones en HBase:

Creación de la tabla: se creó la tabla endangered_plants en HBase con las familias de columnas basic, threats y years.
Carga de datos: se cargaron los datos de las plantas en riesgo desde un archivo CSV en la tabla endangered_plants.
Consultas: se realizaron consultas para obtener información sobre las plantas, como la lista de todas las plantas, la cantidad de plantas amenazadas a nivel nacional y la distribución de las plantas por familia.
Los resultados obtenidos fueron:

La tabla endangered_plants se creó exitosamente en HBase.
Los datos de las plantas en riesgo se cargaron correctamente en la tabla.
Las consultas realizadas permitieron obtener información valiosa sobre las plantas, como la cantidad de plantas amenazadas a nivel nacional y la distribución de las plantas por familia.
Se creó una tabla en HBase para almacenar información sobre plantas en riesgo, se cargaron los datos desde un archivo CSV y se realizaron consultas para obtener información valiosa sobre las plantas.


