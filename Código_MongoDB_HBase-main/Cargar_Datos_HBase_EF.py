

#   Erick Fajardo


#   Proy PLANTAS EN RIESGO 


#Paso 2: Operaciones en HBase
#Cargar los datos en la tabla de HBase

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
