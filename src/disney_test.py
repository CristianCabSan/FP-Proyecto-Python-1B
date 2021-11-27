import csv
from disney import lee_fichero, dinero_generado, generos, dinero_por_genero

def test_lee_fichero(fichero):
    LISTA_TUPLAS = lee_fichero(fichero)
    print("Leídos", len(LISTA_TUPLAS),"registros.")
    print('Los tres primeros registros son:',LISTA_TUPLAS[:3])
    print('Los tres últimos registros son:',LISTA_TUPLAS[-3:])


def test_dinero_generado(k=1000):
    print("Las peliculas que han generado mas de", k ," millones de dolares son:")
    print(*dinero_generado(k), sep="\n")

def test_generos():
    lista = lee_fichero(".\data\disney.csv")
    print("Estos son los distintos generos en las peliculas lanzadas por disney", generos())

def test_dinero_por_genero(genero=0):
    if genero == 0:
        listag = list(generos())
        lista = dinero_por_genero()
        n = 0
        for g in lista:
            print(str(listag[n]) + ":" , lista[n])
            n += 1
    else:
        print(genero + ":", dinero_por_genero(genero))  



test_lee_fichero(".\data\disney.csv")
test_dinero_generado()
test_generos()
test_dinero_por_genero()
test_dinero_por_genero("Comedy")
