import csv
from collections import namedtuple

Info = namedtuple("Info","movie_title, release_date, genre, mpaa_rating, total_gross, inflation_adjusted_gross")

def lee_fichero(fichero):
    """
    Esta funcion recibe un fichero como entrada y devuelve como salida "datos", una lista de tuplas
    la cual tiene por elemento de cada tupla las diferentes columnas de nuestro fichero disney.csv
    """
    with open(fichero, encoding="utf-8") as f:
        lector = csv.reader(f)
        next(lector)
        datos=[]
        for movie_title, release_date, genre, mpaa_rating, total_gross, inflation_adjusted_gross in lector:

            tupla = Info(movie_title, release_date, genre, mpaa_rating, int(total_gross), int(inflation_adjusted_gross))
            datos.append(tupla)
    return(datos)
    

Lista = lee_fichero(".\data\disney.csv")
