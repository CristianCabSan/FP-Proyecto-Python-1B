import csv
from disney import clasificaciones, lee_fichero, dinero_generado, generos, dinero_por_genero, porcentaje_clasificacion
peliculas = lee_fichero(".\data\disney.csv")

def test_lee_fichero(fichero):
    LISTA_TUPLAS = lee_fichero(fichero)
    print("Leidos", len(LISTA_TUPLAS),"registros.")
    print('Los tres primeros registros son:',LISTA_TUPLAS[:3])
    print('Los tres ultimos registros son:',LISTA_TUPLAS[-3:])


def test_dinero_generado(peliculas, k=1000):
    print("Las peliculas que han generado mas de", k ," millones de dolares son:")
    print(*dinero_generado(peliculas, k), sep="\n")

def test_generos(peliculas):
    print("Estos son los distintos generos en las peliculas lanzadas por disney", generos(peliculas))

def test_dinero_por_genero(peliculas, genero=None):
    if genero == None:
        listag = list(generos(peliculas))
        lista = dinero_por_genero(peliculas)
        n = 0
        for g in lista:
            print(str(listag[n]) + ":" , lista[n])
            n += 1
    else:
        print(genero + ":", dinero_por_genero(peliculas, genero))  


def test_porcentaje_clasificacion(peliculas, clasificacion=None):
    if clasificacion == None:
        listac = list(clasificaciones(peliculas))
        lista = porcentaje_clasificacion(peliculas)
        n = 0
        for g in lista:
            print(str(listac[n]) + ":" , lista[n],"%")
            n += 1
    else:
        print(clasificacion + ":", porcentaje_clasificacion(peliculas, clasificacion), "%")  


print("Lee fichero")
test_lee_fichero(".\data\disney.csv")
print("----------")
print("Dinero generado")
test_dinero_generado(peliculas)
print("----------")
print("Generos")
test_generos(peliculas)
print("----------")
print("Dinero por genero")
test_dinero_por_genero(peliculas)
test_dinero_por_genero(peliculas, "Comedy")
print("----------")
print("Porcentaje clasificacion")
test_porcentaje_clasificacion(peliculas, "G")
test_porcentaje_clasificacion(peliculas)