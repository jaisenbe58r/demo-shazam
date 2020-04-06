import numpy
import pandas as pd
import os

import librosa
from matplotlib import pyplot as plt, ticker as plticker, colors as colors, cm, patches
import librosa.display
from scipy.signal import argrelextrema

import msvcrt
from utils.parser import arguments

from utils.audio import *
from utils.Sazham import *
from utils.basedatos import *


def grabacion(filename, seconds):

    print("Presione 'r' para empezar la grabación...")
    key = None
    while key != b'r':
        key = msvcrt.getch()

    record_v1(seconds, filename)
    

def play(filename):

    print("Presione 'p' para reproducir el audio...")
    key = None
    while key != b'p':
        key = msvcrt.getch()

    play_audio(filename)


def crear_fingerprint(filename, filename_fp, name, test=False):

    dfC, XdbC, PCi_max = create_fingerprint(filename, display=True, test=False, n_fft=2048, hop_length=512, percentil=90, 
                tmax=3, tmin=1, f_max=500, f_min=0, delim_freq = 5)
    print(".... Fingerprint creada")

    if not test:
        dfC.to_csv(filename_fp)
        print(".... Fingerprint almacenada en: ", filename_fp)
        add_registro(name)
        print(".... Fingerprint añadido en Base de Datos: ", name)

    return dfC


def Busqueda_matching(dfC):

    lista = registro()
    test_fp_filename = os.path.join("data","patrones","fingerprints")
    resultados = []

    for elemento in lista:

        archivo = test_fp_filename+ "/" + elemento + ".csv"
        df = pd.read_csv(archivo)

        ratio, _, _ = total_matching(df, dfC, display=False)

        resultados.append(ratio)

    id_Result_final = numpy.where(resultados == max(resultados))

    return lista[id_Result_final], resultados[id_Result_final]




if __name__ == "__main__":
    
    args = arguments()
    data_filename = os.path.join("data","patrones","files")
    fingerprint_filename = os.path.join("data","patrones","fingerprints")
    test_filename = os.path.join("data","test")
    test_fp_filename = os.path.join("data","test","fp")


    if args.modo == 'play':

        print("******************************************************")
        print("******************  Play Music ***********************")
        print("******************************************************")
        filename = data_filename + "/" + args.name + ".wav"
        print("Escuchando: ", args.name, " ...")
        play(filename)

    elif args.modo == 'record':

        print("******************************************************")
        print("****************** Record music **********************")
        print("******************************************************")
        filename = data_filename + "/" + args.name + ".wav"
        print("Grabando: ", args.name, " ...")
        grabacion(filename, seconds=60)

    elif args.modo == 'fingerprint':

        print("******************************************************")
        print("****************** FINGERPRINT ***********************")
        print("******************************************************")
        filename = os.path.join(data_filename, args.name + ".wav")
        filename_fp = fingerprint_filename + "/" + args.name + ".csv"
        print("Grabando para FINGERPRINT: ", args.name, " ...")
        grabacion(filename, seconds=60)
        print("Grabacion finalizada, Se procede a crear la huella...")
        crear_fingerprint(filename, filename_fp, args.name)


    elif args.modo == 'eval':
        print("******************************************************")
        print("******************* Shazam RUN ***********************")
        print("******************************************************")
        filename = test_filename + "/" + args.name + ".wav"
        filename_fp = test_fp_filename + "/" + args.name + ".csv"
        print("Grabando: ", args.name, " ...")
        grabacion(filename, seconds=10)
        print("Generando fingerprint del audio grabado ...")
        dfB = crear_fingerprint(filename, filename_fp, args.name, test=True)
        item, score = Busqueda_matching(dfB)
        print("-------------------------------------------------------")
        print("Resultado: \n")
        print("Cancion: ", item, "\n")
        print("Score: ", item, "\n")

    elif args.modo == "prueba":
        pass
