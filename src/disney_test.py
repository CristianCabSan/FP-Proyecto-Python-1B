import csv
from disney import clasificaciones, diccionario_anyos, lee_fichero, dinero_generado, generos, dinero_por_genero, mayor_pelicula_genero, porcentaje_clasificacion, intervalo_ingresos
registros = lee_fichero(".\data\disney.csv")

def test_lee_fichero(fichero):
    LISTA_TUPLAS = lee_fichero(fichero)
    print("Leidos", len(LISTA_TUPLAS),"registros.")
    print('Los tres primeros registros son:',LISTA_TUPLAS[:3])
    print('Los tres ultimos registros son:',LISTA_TUPLAS[-3:])


def test_dinero_generado(registros, k=1000):
    print("Las peliculas que han generado mas de", k ," millones de dolares son:")
    print(*dinero_generado(registros, k), sep="\n")

def test_generos(registros):
    print("Estos son los distintos generos en las peliculas lanzadas por disney", generos(registros))

def test_dinero_por_genero(registros, genero=None):
    if genero == None:
        listag = list(generos(registros))
        lista = dinero_por_genero(registros)
        n = 0
        for g in lista:
            print(str(listag[n]) + ":" , lista[n])
            n += 1
    else:
        print(genero + ":", dinero_por_genero(registros, genero))  


def test_porcentaje_clasificacion(registros, clasificacion=None):
    if clasificacion == None:
        listac = list(clasificaciones(registros))
        lista = porcentaje_clasificacion(registros)
        n = 0
        for g in lista:
            print(str(listac[n]) + ":" , lista[n],"%")
            n += 1
    else:
        print(clasificacion + ":", porcentaje_clasificacion(registros, clasificacion), "%")  

def test_mayor_pelicula_genero(registros,genero,orden=True):
    pelicula = mayor_pelicula_genero(registros, genero, orden)
    if orden == True:
        print (f"La pelicula con mayor ingresos del genero {genero} es {pelicula[0]} con un ingreso de {pelicula[1]} dolares")
    else:
        print (f"La pelicula con menor ingresos del genero {genero} es {pelicula[0]} con un ingreso de {pelicula[1]} dolares")

def test_diccionario_anyos(registros, anyo):
    print(f"Las peliculas estrenadas en el anyo {anyo} por Disney fueron {diccionario_anyos(registros)[anyo]}")

def test_intervalo_ingresos(registros, intervalo="Menos de 1 millon"):
    print(f"Las peliculas que han generado {intervalo} de dolares y sus respectivos ingresos son {intervalo_ingresos(registros)[intervalo]}")

print("Lee fichero")
test_lee_fichero(".\data\disney.csv")
print("----------")
print("Dinero generado")
test_dinero_generado(registros)
print("----------")
print("Generos")
test_generos(registros)
print("----------")
print("Dinero por genero")
test_dinero_por_genero(registros)
test_dinero_por_genero(registros, "Comedy")
print("----------")
print("Porcentaje clasificacion")
test_porcentaje_clasificacion(registros, "G")
test_porcentaje_clasificacion(registros)
print("----------")
print("Mayor pelicula genero")
test_mayor_pelicula_genero(registros, "Musical")
test_mayor_pelicula_genero(registros, "Musical", False)
print("----------")
print("Diccionario anyos")
test_diccionario_anyos(registros,2015)
print("----------")
print("Intervalo ingresos")
test_intervalo_ingresos(registros)