import csv
from collections import namedtuple
from datetime import datetime


Info = namedtuple("Info","movie_title, release_date, genre, mpaa_rating, total_gross, inflation_adjusted_gross")

# --------------------------------Bloque 1-------------------------------------

def lee_fichero(fichero):
    """
    Esta funcion recibe un fichero como entrada y devuelve como salida "registros", una lista de tuplas
    la cual tiene por elemento de cada tupla las diferentes columnas de nuestro fichero disney.csv
    
    Entrada:
    -fichero(en formato csv y encoding utf-8)
    Salida:
    -registros: Lista de tupla que ha dividido las columnas del fichero en las categorias movie_title, release_date, genre, mpaa_rating, total_gross, inflation_adjusted_gross
    """

    with open(fichero, encoding="utf-8") as f:
        lector = csv.reader(f)
        next(lector)
        registros=[]
        for movie_title, release_date, genre, mpaa_rating, total_gross, inflation_adjusted_gross in lector:

            tupla = Info(movie_title, datetime.strptime(release_date, "%Y-%m-%d"), genre, mpaa_rating, int(total_gross), int(inflation_adjusted_gross))
            registros.append(tupla)
    return(registros)

registros = lee_fichero(".\data\disney.csv")

# --------------------------------Bloque 2-------------------------------------

def dinero_generado(registros, k=1000):
    """
    (Filtrar la lista con los registros por alguno/s de los campos (que se cumpla determinada condición))

    Esta funcion recibe un valor k como entrada y devuelve una lista cuyos inflation_adjusted_gross
    son mayores a k

    Entrada:
    -k(int): Valor en miles de dolares y con valor predeterminado 1000
    Salida:
    -Lista con las peliculas que cumplen el requisito
    """
    k = k*1000000
    lista = [(p.inflation_adjusted_gross, p.movie_title) for p in registros if p.inflation_adjusted_gross > k]
    lista.sort(reverse = True)
    return lista

def generos(registros):
    """
    (Obtener un conjunto con alguno de los campos)
    
    Devuelve un conjunto con todos los generos de peliculas lanzadas por Disney (Las disponibles en el fichero)
    """
    listag = {(p.genre) for p in registros}
    return listag

# --------------------------------Bloque 3-------------------------------------

def dinero_por_genero(registros, genero=None):
    """
   (Calcular el promedio de alguna propiedad numérica de los registros que cumplan determinada condición)

    Devuelve el promedio del dinero generado(ajustado a inflación) de las peliculas de un mismo genero
    
    Entrada:
    -genero(str): Debe coincidir con uno de los generos del fichero,
    como valor predeterminado tiene 0 lo que hace este proceso con todos los generos
    Salida:
    Hay dos opciones de salida,
    -si genero = 0, Se devuelve una lista con el promedio del dinero generado por cada genero en orden alfabetico
    -si genero coincide con alguno de los generos del fichero, Devuelve un float con el promedio de dinero de las peliculas de ese genero
    """

    if genero == None:
        listag = list(generos(registros))
        lista = []
        for g in listag:
            listas = [(p.inflation_adjusted_gross) for p in registros if p.genre == g]
            lista.append(round(sum(listas)/len(listas),2))
        return lista
    else:
        lista = [(p.inflation_adjusted_gross) for p in registros if p.genre == genero]
        return round(sum(lista)/len(lista),2)

def clasificaciones(registros):
    "Funcion auxiliar para porcentaje_clasificacion"
    clasificaciones = {(p.mpaa_rating) for p in registros}
    return clasificaciones


def porcentaje_clasificacion(registros, clasificacion=None):
    """
    (Calcular un valor como resultado de aplicar una función matemática a determinado campo de los registros
    que cumplen una condición)

    Devuelve el porcentaje de peliculas con una determinada clasificacion
    
    Entrada:
    -clasificacion(str): Debe coincidir con una de las clasificaciones del fichero,
    como valor predeterminado tiene None lo que hace este proceso con todos los generos
    Salida:
    Hay dos opciones de salida,
    -si clasificacion = None, Se devuelve una lista con los porcentajes de las distintas clasificaciones
    -si clasificacion coincide con alguno de las clasificaciones del fichero, Devuelve un float con el porcentaje de peliculas con esa clasificacion
    """
    leidos = len(registros)
    clasif = list(clasificaciones(registros))
    if clasificacion == None:
        porcentaje = []
        for e in clasif:
            numero = len([(p.mpaa_rating) for p in registros if p.mpaa_rating == e])
            porcentaje.append(round((numero/leidos)*100 , 2))
    elif clasificacion in clasif:
        numero = len([(p.mpaa_rating) for p in registros if p.mpaa_rating == clasificacion])
        porcentaje = round((numero/leidos)*100, 2)
    return porcentaje

# --------------------------------Bloque 4-------------------------------------

def mayor_pelicula_genero(registros,genero,orden=True):
    """
    (Obtener el registro (o algunos campos del registro) que contiene el valor máximo o mínimo de un campo
    determinado, de los registros que cumplen determinada condición)

    Devuelve el nombre e ingresos (ajustados a inflacion) de la pelicula con mayor/menor ingresos de un genero determinado

    Entrada:
    -genero(str): Determina las peliculas de las que compararemos sus ingresos
    -orden(bool): Por defecto en True muestra la pelicula con mayor ingresos y en False muestra la pelicula con menor ingresos
    Salida:
    -Devuelve una tupla con el nombre e ingresos de dicha pelicula
    """
    lista = ([p.movie_title, p.inflation_adjusted_gross] for p in registros if p.genre == genero)
    if orden == True:
        return max(lista, key=lambda x:x[1])
    else:
        return min(lista, key=lambda x:x[1])

# --------------------------------Bloque 5-------------------------------------

def mayor_peliculas_anyo(registros,anyo,n,orden=True):
    """
    (Obtener una lista de registros (o algunos campos del registro) ordenada con los n registros con mayor (o
    menor) valor en un campo determinado. Donde “n” es un parámetro que debe recibir la función.)  

    Devuelve nombre e ingresos (ajustados a inflacion) de las n peliculas con mayor/menor ingresos de un anyo determinado

    Entrada:
    -anyo(int): Determina las peliculas de las que compararemos sus ingresos
    -n: Determina la cantidad de peliculas a mostrar
    -orden(bool): Por defecto en True muestra las n peliculas ordenadas segun ingresos en orden descendente y en False muestra las n peliculas ordenadas segun ingresos
    en orden ascendente
    Salida:
    -Devuelve una lista con una cantidad menor o igual a n (Dependiendo si hay suficientes peliculas en ese anyo) de tuplas ordenadas segun ingresos donde cada tupla incluye
    nombre de la pelicula e ingresos ajustados a inflacion.
    """
    lista = ([p.movie_title, p.inflation_adjusted_gross] for p in registros if p.release_date.year == anyo)
    if orden==True:
        return sorted(lista, key=lambda x:x[1], reverse=False)[:n]
    else:
        return sorted(lista, key=lambda x:x[1])[:n]

# --------------------------------Bloque 6-------------------------------------
def diccionario_anyos(registros):
    """
    (Obtener un diccionario que permita agrupar, los registros que cumplen determinada condición, por algún
    campo (clave). A cada clave se le hará corresponder una lista con los registros que contienen esa clave)

    Devuelve un diccionario donde cada key es un anyo y su valor es una lista con los titulos de las peliculas estrenadas
    en ese anyo
    """

    dicc = dict()
    for p in registros:
        if p.release_date.year not in dicc:
            u = {p.release_date.year:[p.movie_title]}
            dicc.update(u)
        else:
            u = {p.release_date.year:dicc[p.release_date.year].append(p.movie_title)}
    return dicc

def intervalo_ingresos(registros):
    """
    (Obtener un diccionario que permita agrupar, los registros que cumplen determinada condición, por algún
    campo (clave) y que haga corresponder a cada clave una lista, con los “n” registros, ordenados de mayor a   
    menor o de menor a mayor por algún campo que no sea la clave)

    Devuelve un diccionario cuyas claves son intervalos de dolares generados (menos de 1 millon, de 1 a 10 millones, de 11 a 50 millones, de 51 a 100 millones, de 101 a 1000 millones
    y mas de 1000 millones) y cuyos valores son una lista de tuplas de las peliculas que corresponden a cada intervalo en el que la lista contiene el nombre de la pelicula y el dinero
    generado por esta. Ademas los valores estan ordenador de mayor a menor segun la cantidad de dinero generada
    """
    dicc = dict()
    menos1 = [] ; de1a10 = [] ; de11a50 = [] ; de51a100 = [] ;de101a1000 = [] ; mas1000 = []
    for p in registros:
        #------------------------------------------------------------------------------------------------------------
        if p.inflation_adjusted_gross < 1000000:
            menos1.append((p.movie_title, p.inflation_adjusted_gross))
            dicc["Menos de 1 millon"] = sorted(menos1, key=lambda x:x[1], reverse=True)
        #------------------------------------------------------------------------------------------------------------
        elif p.inflation_adjusted_gross < 11000000:
            de1a10.append((p.movie_title, p.inflation_adjusted_gross))
            dicc["Entre 1 y 10 millones"] = sorted(de1a10, key=lambda x:x[1], reverse=True)
        #------------------------------------------------------------------------------------------------------------
        elif p.inflation_adjusted_gross < 51000000:
            de11a50.append((p.movie_title, p.inflation_adjusted_gross))
            dicc["Entre 11 y 50 millones"] = sorted(de11a50, key=lambda x:x[1], reverse=True)
        #------------------------------------------------------------------------------------------------------------
        elif p.inflation_adjusted_gross < 101000000:
            de51a100.append((p.movie_title, p.inflation_adjusted_gross))
            dicc["Entre 51 y 100 millones"] = sorted(de51a100, key=lambda x:x[1], reverse=True)
        #------------------------------------------------------------------------------------------------------------
        elif p.inflation_adjusted_gross < 1000000000:
            de101a1000.append((p.movie_title, p.inflation_adjusted_gross))
            dicc["Entre 101 y 1000 millones"] = sorted(de101a1000, key=lambda x:x[1], reverse=True)
        #------------------------------------------------------------------------------------------------------------
        elif p.inflation_adjusted_gross > 1000000000:
            mas1000.append((p.movie_title, p.inflation_adjusted_gross))
            dicc["Mas de 1000 millones"] = sorted(mas1000, key=lambda x:x[1], reverse=True)
        #------------------------------------------------------------------------------------------------------------
    return dicc
