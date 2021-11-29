import csv
from disney import clasificaciones, lee_fichero, dinero_generado, generos, dinero_por_genero, porcentaje_clasificacion

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


def test_porcentaje_clasificacion(clasificacion=0):
    if clasificacion == 0:
        listac = list(clasificaciones())
        lista = porcentaje_clasificacion()
        n = 0
        for g in lista:
            print(str(listac[n]) + ":" , lista[n],"%")
            n += 1
    else:
        print(clasificacion + ":", porcentaje_clasificacion(clasificacion), "%")  



#test_lee_fichero(".\data\disney.csv")
#test_dinero_generado()
#test_generos()
test_dinero_por_genero()
test_dinero_por_genero("Comedy")
test_porcentaje_clasificacion("G")
test_porcentaje_clasificacion()