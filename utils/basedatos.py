import os


def registro():
    """
    Lectura de los nombres de las canciones almacenadas en la base de datos
    """
    dirFichero = "data/patrones/fingerprints/BASE_DATOS.txt"
    a = []
    with open(dirFichero, 'r') as reader:
        for line in reader:
            print(line)
            _line = line.split('\n')[0]
            a.append(_line)

    return a


def add_registro(name):

    dirFichero = "data/patrones/fingerprints/BASE_DATOS.txt"
    f = open (dirFichero, "a")
    line = name + "\n"
    f.write(line)
    f.close()