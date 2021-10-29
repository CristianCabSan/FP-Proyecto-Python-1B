# Proyecto del Primer Cuatrimestre Fundamentos de Programación (Curso  21/22)

Autor: Cristian Caballero Sánchez

Este proyecto se realiza a manera de trabajo entregable para la clase de FP de primer año de Ingenieria Informatica de Computadores.
Para este proyecto se ha escogido un dataset referente a peliculas de disney, el cual contiene informacion especifica de cada pelicula
incluyendo datos como la fecha de salida o los ingresos generados con ellas.

Disclaimer: A la hora de la realizacion de esta versión el proyecto se encuentra en una fase temprana por lo que este archivo README esta muy poco detallado y algunas partes aun continuan en su forma generica. A medida que avancen las etapas del proyecto se actualizara este documento.
## Carpeta src

* **/src**: Contiene los diferentes módulos de Python que conforman el proyecto.
  * <disney.py>: Módulo principal del proyecto
  * <disney_test.py>: Módulo para la prueba de funciones

* **/data**: Contiene el dataset del proyecto
  * <disney.csv>: Fichero con información sobre las peliculas de Disney.
    
## Estructura del fichero

El dataset está compuesto por 6 columnas para cada pelicula, con la siguiente descripción:

* <movie_title>: de tipo <str>, Titulo de la pelicula
* <release_date>: de tipo <str>, Fecha de estreno
* <genre>: de tipo <str>, Género
* <mpaa_rating>: de tipo <str>, Clasificación por edades
* <total_gross>: de tipo <int>, Dinero total generado con la pelicula
* <inflation_adjusted_gross>: de tipo <int>, Dinero total generado con la pelicula ajustado a la inflacion

## Tipos implementados

* "Info": Esta tupla contiene la forma del fichero y es usado en la funcion "leer_fichero"
## Funciones implementadas

### \<modulo Disney\>

* **<lee_fichero(fichero)>**: Lee los datos del fichero y devuelve una lista de tuplas con los datos del fichero.
Entrada: fichero en formato csv y codificacion utf-8
Salida: lista de tuplas cuyo elementos son "movie_title, release_date, genre, mpaa_rating, total_gross, inflation_adjusted_gross"


### \<modulo Disney_test\>
En este modulo se han definido las seguientes funciones, cada uno en referencia a una funcion del modulo "Disney" teniendo el mismo nombre
que las del modulo mencionado pero con el prefijo "test_".
* **<test_lee_fichero(fichero)>**
 