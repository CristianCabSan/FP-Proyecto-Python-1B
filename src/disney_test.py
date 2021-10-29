import csv
from disney import lee_fichero

def test_lee_fichero(fichero):
    LISTA_TUPLAS = lee_fichero(fichero)
    print("Leídos", len(LISTA_TUPLAS),"registros.")
    print('Los tres primeros registros son:',LISTA_TUPLAS[:3])
    print('Los tres últimos registros son:',LISTA_TUPLAS[-3:])

test_lee_fichero(".\data\disney.csv")