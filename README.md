# Laboratorio 5 - PySpark - RDDs

Llenar los siguientes campos:

Nombre:

Código:

# Descripción

El objetivo de este laboratorio es familiarizarse con el uso de PySpark para el procesamiento de datos en paralelo.

# Docker

Para facilitar la instalación de PySpark, se provee un docker-compose.yml que levanta un contenedor con Jupyter Notebook y PySpark instalado.

Para levantar el contenedor, ejecutar:

```bash
docker-compose up -d
```


# Datasets

Para descargar el dataset de este laboratorio, hacer correr el script ubicado en `scripts/dataset_downloader.py`.
Para correr el script, es necesario especificar el directorio donde se quiere guardar el dataset. Por ejemplo, para descargar el dataset en el directorio `datasets`:

```bash
python scripts/dataset_downloader.py -o ../datasets
```


## Dataset 1 - Shakespeare
Este dataset contiene las obras de Shakespeare. Cada línea del archivo contiene una palabra de una obra de Shakespeare. El archivo se encuentra en el directorio `data/tiny-shakespeare`.

## Dataset 2 - Airline on-time data
Data Expo 2009: Airline on time data, para mas informacion ver el siguiente enlace:
https://dataverse.harvard.edu/dataset.xhtml?persistentId=doi:10.7910/DVN/HG7NV7

Cada archivo, que representa un año, contiene información sobre los vuelos de la aerolínea. Cada línea del archivo contiene información sobre un vuelo. La información de cada vuelo está separada por comas. La información de cada vuelo contiene los siguientes campos:

* **Year**: 1987-2008
* **Month**: 1-12
* **DayofMonth**: 1-31
* **DayOfWeek**: 1 (Monday) - 7 (Sunday)
* **DepTime**: actual departure time (local, hhmm)
* **CRSDepTime**: scheduled departure time (local, hhmm)
* **ArrTime**: actual arrival time (local, hhmm)
* **CRSArrTime**: scheduled arrival time (local, hhmm)
* **UniqueCarrier**: unique carrier code
* **FlightNum**: flight number
* **TailNum**: plane tail number
* **ActualElapsedTime**: in minutes
* **CRSElapsedTime**: in minutes
* **AirTime**: in minutes
* **ArrDelay**: arrival delay, in minutes
* **DepDelay**: departure delay, in minutes
* **Origin**: origin IATA airport code
* **Dest**: destination IATA airport code
* **Distance**: in miles
* **TaxiIn**: taxi in time, in minutes
* **TaxiOut**: taxi out time in minutes
* **Cancelled**: was the flight cancelled? (1 = yes)
* **CancellationCode**: reason for cancellation (A = carrier, B = weather, C = NAS, D = security)
* **Diverted**: 1 = yes, 0 = no
* **CarrierDelay**: in minutes
* **WeatherDelay**: in minutes
* **NASDelay**: in minutes
* **SecurityDelay**: in minutes
* **LateAircraftDelay**: in minutes