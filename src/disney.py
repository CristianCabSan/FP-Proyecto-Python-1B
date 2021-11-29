import csv
from collections import namedtuple
from datetime import datetime


Info = namedtuple("Info","movie_title, release_date, genre, mpaa_rating, total_gross, inflation_adjusted_gross")

def lee_fichero(fichero):
    """
    Esta funcion recibe un fichero como entrada y devuelve como salida "datos", una lista de tuplas
    la cual tiene por elemento de cada tupla las diferentes columnas de nuestro fichero disney.csv
    
    Entrada:
    -fichero(en formato csv y encoding utf-8)
    Salida:
    -datos: Lista de tupla que ha dividido las columnas del fichero en las categorias movie_title, release_date, genre, mpaa_rating, total_gross, inflation_adjusted_gross
    """

    with open(fichero, encoding="utf-8") as f:
        lector = csv.reader(f)
        next(lector)
        datos=[]
        for movie_title, release_date, genre, mpaa_rating, total_gross, inflation_adjusted_gross in lector:

            tupla = Info(movie_title, datetime.strptime(release_date, "%Y-%m-%d"), genre, mpaa_rating, int(total_gross), int(inflation_adjusted_gross))
            datos.append(tupla)
    return(datos)


info_disney = lee_fichero(".\data\disney.csv")


def dinero_generado(k=1000):
    """
    Esta funcion recibe un valor k como entrada y devuelve una lista cuyos inflation_adjusted_gross
    son mayores a k

    Entrada:
    -k(int): Valor en miles de dolares y con valor predeterminado 1000
    Salida:
    -Lista con las peliculas que cumplen el requisito
    """
    peliculas = lee_fichero(".\data\disney.csv")
    k = k*1000000
    lista = [(p.movie_title, p.inflation_adjusted_gross) for p in peliculas if p.inflation_adjusted_gross > k]
    lista.sort(reverse = True)
    return lista


def generos():
    """
    Devuelve una lista todos los generos de peliculas lanzadas por Disney (Las disponibles en el fichero)
    """
    peliculas = lee_fichero(".\data\disney.csv")
    listag = {(p.genre) for p in peliculas}
    return listag


def dinero_por_genero(genero=None):
    """
    Devuelve el promedio del dinero generado(ajustado a inflación) de las peliculas de un mismo genero
    
    Entrada:
    -genero(str): Debe coincidir con uno de los generos del fichero,
    como valor predeterminado tiene 0 lo que hace este proceso con todos los generos
    Salida:
    Hay dos opciones de salida,
    -si genero = 0, Se devuelve una lista con el promedio del dinero generado por cada genero en orden alfabetico
    -si genero coincide con alguno de los generos del fichero, Devuelve un float con el promedio de dinero de las peliculas de ese genero
    """
    
    
    peliculas = lee_fichero(".\data\disney.csv")
    if genero == None:
        listag = list(generos())
        lista = []
        for g in listag:
            listas = [(p.inflation_adjusted_gross) for p in peliculas if p.genre == g]
            lista.append(round(sum(listas)/len(listas),2))
        return lista
    else:
        lista = [(p.inflation_adjusted_gross) for p in peliculas if p.genre == genero]
        return round(sum(lista)/len(lista),2)

def clasificaciones():
    peliculas = lee_fichero(".\data\disney.csv")
    clasificaciones = {(p.mpaa_rating) for p in peliculas}
    return clasificaciones


def porcentaje_clasificacion(clasificacion=None):
    """
    Devuelve el porcentaje de peliculas con una determinada clasificacion
    
    Entrada:
    -clasificacion(str): Debe coincidir con una de las clasificaciones del fichero,
    como valor predeterminado tiene None lo que hace este proceso con todos los generos
    Salida:
    Hay dos opciones de salida,
    -si clasificacion = None, Se devuelve una lista con los porcentajes de las distintas clasificaciones
    -si clasificacion coincide con alguno de las clasificaciones del fichero, Devuelve un float con el porcentaje de peliculas con esa clasificacion
    """
    
    peliculas = lee_fichero(".\data\disney.csv")
    leidos = len(peliculas)
    clasif = list(clasificaciones())
    if clasificacion == None:
        porcentaje = []
        for e in clasif:
            numero = len([(p.mpaa_rating) for p in peliculas if p.mpaa_rating == e])
            porcentaje.append(round((numero/leidos)*100 , 2))
    elif clasificacion in clasif:
        numero = len([(p.mpaa_rating) for p in peliculas if p.mpaa_rating == clasificacion])
        porcentaje = round((numero/leidos)*100, 2)
    return porcentaje
