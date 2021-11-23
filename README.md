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

* **movie_title**: de tipo **str**, Titulo de la pelicula
* **release_date**: de tipo **str**, Fecha de estreno
* **genre**: de tipo **str**, Género de la pelicula
* **mpaa_rating**: de tipo **str**, Clasificación por edades
* **total_gross**: de tipo **int**, Dinero total generado con la pelicula
* **inflation_adjusted_gross**: de tipo **int**, Dinero total generado con la pelicula ajustado a la inflacion

## Tipos implementados

* "Info": Esta tupla contiene la forma del fichero y es usado en la funcion "leer_fichero"
## Funciones implementadas

### \<modulo Disney\>

* **<lee_fichero(fichero)>**: Lee los datos del fichero y devuelve una lista de tuplas con los datos del fichero.
Entrada: Fichero en formato csv y codificacion utf-8
Salida: Lista de tuplas (movie_title, release_date, genre, mpaa_rating, total_gross, inflation_adjusted_gross)
* **<dinero_generado(k)>**: Devuelve una lista con todas las peliculas cuyos beneficios ajustados a la inflacion son mayores que una cantidad dada
Entrada:k(int): Dinero (en millones de dolares) generado por la pelicula minimos para entrar en la lista, el valor predeterminado es de 1 billón (mil millones) de dolares
Salida: Lista con las peliculas con un inflation_adjusted_gross mayor a k
* **<generos()>**: Muestra todos los generos de las peliculas lanzadas por Disney
Salida: Un conjunto con los diferentes generos de las peliculas
* **<dinero_por_genero(genero)>**: Devuelve el promedio del dinero generado(ajustado a inflación) de las peliculas de un mismo genero
Entrada:
-genero(str): Debe coincidir con uno de los generos del fichero,
como valor predeterminado tiene 0 lo que hace este proceso con todos los generos
Salida: Hay dos opciones de salida,
-Si genero = 0, Se devuelve una lista con el promedio del dinero generado por cada genero en orden alfabetico
-Si genero coincide con alguno de los generos del fichero, Devuelve un float con el promedio de dinero de las peliculas de ese genero

### \<modulo Disney_test\>
En este modulo se han definido las seguientes funciones, cada uno en referencia a una funcion del modulo "Disney" teniendo el mismo nombre
que las del modulo mencionado pero con el prefijo "test_".
* **<test_lee_fichero(fichero)>**
* **<test_dinero_generado()>**
* **<test_generos()>**
* **<test_dinero_por_genero(genero)>**
 