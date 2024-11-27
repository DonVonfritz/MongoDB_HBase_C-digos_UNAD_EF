
#   Erick Fajardo

#   Proy PLANTAS EN RIESGO 

#   Realizar consultas de selección, filtrado y recorrido sobre los datos


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
    print(f"Error al consultar datos: {str})(e)