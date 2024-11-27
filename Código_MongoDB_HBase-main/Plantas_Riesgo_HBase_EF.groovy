

import happybase
import pandas as pd

Proyecto HBase: Gestión de Datos sobre Plantas en Riesgo en Colombia

1. Creación de la Tabla en HBase

Creo una tabla en HBase que almacenará información sobre las plantas en riesgo de extinción en Colombia. 
Utilizare un conjunto de datos que contiene información relevante sobre diversas especies de vegetación Colombiana.

Definición de la Tabla

Nombre de la tabla: plantas_en_riesgo

Familias de columnas:

informacion_basica: Contendrá datos generales sobre cada planta.
nombre_comun: Nombre común de la planta.
nombre_cientifico: Nombre científico de la planta.
familia: Familia a la que pertenece la planta.
caracteristicas: Contendrá características específicas de las plantas.
altura: Altura promedio de la planta.
habitat: Tipo de hábitat donde se encuentra la planta.
estado_conservacion: Estado de conservación según la legislación colombiana.
distribucion: Contendrá información sobre la distribución geográfica.
region: Regiones de Colombia donde se encuentra la planta.
coordenadas: Coordenadas geográficas de la planta.
Comando para crear la tabla en HBase

create 'plantas_en_riesgo', 'informacion_basica', 'caracteristicas', 'distribucion'


2. Operaciones en HBase

Cargar los Datos en la Tabla de HBase
Para cargar los datos en la tabla plantas_en_riesgo, utilizaremos un archivo CSV que contiene la información de las plantas. A continuación, se muestra un ejemplo de cómo insertar datos en la tabla.

put 'plantas_en_riesgo', '1', 'informacion_basica:nombre_comun', 'Orquídea'
put 'plantas_en_riesgo', '1', 'informacion_basica:nombre_cientifico', 'Orchidaceae'
put 'plantas_en_riesgo', '1', 'informacion_basica:familia', 'Orquídeas'
put 'plantas_en_riesgo', '1', 'caracteristicas:altura', '1.5 m'
put 'plantas_en_riesgo', '1', 'caracteristicas:habitat', 'Bosques húmedos'
put 'plantas_en_riesgo', '1', 'caracteristicas:estado_conservacion', 'En peligro'
put 'plantas_en_riesgo', '1', 'distribucion:region', 'Amazonas'
put 'plantas_en_riesgo', '1', 'distribucion:coordenadas', '3.4653, -70.5335'

2.1 Consultas de Selección, Filtrado y Recorrido

Para realizar consultas sobre los datos, se pueden utilizar los siguientes comandos:

Seleccionar todos los datos de una planta específica:

get 'plantas_en_riesgo', '1'

Filtrar plantas por estado de conservación:

scan 'plantas_en_riesgo', {FILTER => "PrefixFilter('En peligro')"}

Recorrer todas las plantas en riesgo:

scan 'plantas_en_riesgo'



2. Operaciones de Escritura (Inserción, Actualización y Eliminación)


2.2 Inserción de una nueva planta:


put 'plantas_en_riesgo', '2', 'informacion_basica:nombre_comun', 'Café'
put 'plantas_en_riesgo', '2', 'informacion_basica:nombre_cientifico', 'Coffea'

Actualización de una planta existente:

put 'plantas_en_riesgo', '1', 'caracteristicas:estado_conservacion', 'En peligro crítico'

Eliminación de una planta:

delete 'plantas_en_riesgo', '2'


3. Documentación

Estructura de la Tabla en HBase

La tabla plantas_en_riesgo está estructurada en tres familias de columnas que almacenan información básica, características y distribución geográfica de las plantas en riesgo. Cada fila en la tabla representa una especie de planta, identificada por su clave única.

Explicación de las Operaciones Realizadas en HBase y Resultados Obtenidos

Se llevaron a cabo diversas operaciones en la tabla plantas_en_riesgo, incluyendo la creación de la tabla, la carga de datos, consultas, y operaciones de escritura. Los resultados obtenidos permiten acceder a información detallada sobre las plantas en riesgo en Colombia, facilitando así la investigación y la toma de decisiones en materia de análisis y toma de desiciones.


