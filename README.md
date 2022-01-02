# Proyecto del Primer Cuatrimestre Fundamentos de Programación (Curso  21/22)

Autor: Cristian Caballero Sánchez

Este proyecto se realiza a manera de trabajo entregable para la clase de FP de primer año de Ingenieria Informatica de Computadores.
Para este proyecto se ha escogido un dataset referente a peliculas de disney, el cual contiene informacion especifica de cada pelicula
incluyendo datos como la fecha de salida o los ingresos generados con ellas.

## Estructura de las carpetas

* **/src**: Contiene los diferentes módulos de Python que conforman el proyecto.
  * <disney.py>: Módulo principal del proyecto
  * <disney_test.py>: Módulo para la prueba de funciones

* **/data**: Contiene el dataset del proyecto
  * <disney.csv>: Fichero con información sobre las peliculas de Disney.
    
## Estructura del fichero

El dataset está compuesto por 6 columnas para cada pelicula, con la siguiente descripción:

* **movie_title**: de tipo **str**, Titulo de la pelicula
* **release_date**: de tipo **datetime**, Fecha de estreno
* **genre**: de tipo **str**, Género de la pelicula
* **mpaa_rating**: de tipo **str**, Clasificación por edades
* **total_gross**: de tipo **int**, Dinero total generado con la pelicula
* **inflation_adjusted_gross**: de tipo **int**, Dinero total generado con la pelicula ajustado a la inflacion

## Tipos implementados

* "Info": Esta tupla contiene la forma del fichero y es usado en la funcion "leer_fichero" tiene la siguiente estructura:

`Info = namedtuple("Info","movie_title, release_date, genre, mpaa_rating, total_gross, inflation_adjusted_gross")`

con los siguientes tipos:

`Info = namedtuple("Info","str, datetime, str, str, int, int")`

## Funciones implementadas

### Modulo Disney

#### Entrega 2

* **Bloque 1**
  * **lee_fichero(fichero)** Dado un fichero devuelve una lista de tuplas categorizando las distintas columnas del fichero.

* **Bloque 2**
  * **dinero_generado(k)** Dado k (en miles de dolares y con valor predeterminado 1000) devuelve una lista de tuplas de las peliculas que han generado mas que k (A partir del valor ajustado a inflacion) donde cada tupla contiene el nombre y el dinero generado de dichas peliculas.
  * **generos(registros)** Muestra todos los generos de las peliculas lanzadas por Disney (disponibles en el fichero)

* **Bloque 3**
  * **dinero_por_genero(registros, genero)** Devuelve el promedio del dinero generado(ajustado a inflación) de las peliculas de un genero, en caso de no indicarse genero se calcula el promedio de todos los generos (por lo que en este caso devuelve una lista de valores)
  * **porcentaje_clasificacion(registros, clasificacion)** Dada una clasificacion devuelve el porcentaje de peliculas con esa clasificacion, si no se determina una clasificacion se devuelve una lista con los porcentajes que representan las distintas clasificaciones. (El fichero posee 513 peliculas)
  * **clasificaciones(registros)**: Devuelve un conjunto con las distintas clasificaciones (Funcion auxiliar creada para porcentaje_clasificacion)

#### Entrega 3

* **Bloque 4**
  * **mayor_pelicula_genero(registros,genero,orden=True)** Dado un genero y con un orden por defecto de True, devuelve la pelicula con mayor ingresos del genero dado en caso de que orden sea False devolvera la pelicula con menor ingresos del genero dado.

* **Bloque 5**
  * **diccionario_anyos(registros)** Devuelve un diccionario cuyas claves son los diferentes anyos del fichero y sus respectivos valores son listas que contienen los nombres de las peliculas estrenadas ese anyo
  * **intervalo_ingresos(registros)** Devuelve un diccionario cuyas claves son intervalos de dolares generados y cuyos valores son una lista de tuplas de las peliculas que corresponden a cada intervalo en el que la lista contiene el nombre de la pelicula y el dinero generado por esta. Ademas los valores estan ordenados de mayor a menor segun la cantidad de dinero generado. El valor n con una valor por defecto de 3 determinara la longitud maxima de cada lista de tuplas.

### Modulo Disney_test
En este modulo se han definido las seguientes funciones, cada uno en referencia a una funcion del modulo "Disney" teniendo el mismo nombre
que las del modulo mencionado pero con el prefijo "test_".
* **test_lee_fichero(fichero)**
* **test_dinero_generado(registros,k)**
* **test_generos(registros)**
* **test_dinero_por_genero(registros,genero)**
* **test_porcentaje_clasificacion(registros,clasificacion)**
* **test_mayor_pelicula_genero(registros,genero,orden)**
* **test_diccionario_anyos(registros,anyo)**
* **test_intervalo_ingresos(registros, intervalo)**