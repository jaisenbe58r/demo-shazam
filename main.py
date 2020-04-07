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

    if not test:
        dfC, _, _ = create_fingerprint(filename, display=False, test=False, n_fft=2048, hop_length=512, percentil=90, 
                tmax=3, tmin=1, f_max=500, f_min=0, delim_freq = 5)
    else:
        dfC, _, _ = create_fingerprint(filename, name=name, display=True, test=False, n_fft=2048, hop_length=512, percentil=90, 
                tmax=3, tmin=1, f_max=500, f_min=0, delim_freq = 5)
    print(".... Fingerprint creada")

    if not test:
        dfC.to_csv(filename_fp)
        print(".... Fingerprint almacenada en: ", filename_fp)
        add_registro(name)
        print(".... Fingerprint añadido en Base de Datos: ", name)

    return dfC


def Busqueda_matching(dfC, min_match = 5):

    lista = registro()
    test_fp_filename = os.path.join("data","patrones","fingerprints")
    resultados = []

    for elemento in lista:

        archivo = test_fp_filename+ "/" + elemento + ".csv"
        df = pd.read_csv(archivo)

        ratio, _, _ = total_matching(df, dfC, elemento, display=False, min_match = min_match)

        resultados.append(ratio)  
    
    if len(resultados)>0 and sum(resultados)>0.0:
        na_result = numpy.array(resultados)
        id_Result_final = numpy.where(na_result == max(na_result))[0][0]

        _match = lista[id_Result_final]
        _coincidencias = resultados[id_Result_final]
        _score = round(_coincidencias/sum(resultados), 2)

        _scores_aux = resultados/sum(resultados)
        _scores = [round(i, 2) for i in _scores_aux]

        _resultados = [int(i) for i in resultados]

        _result = list(zip(lista, _scores, _resultados))
    
    else:
        _match, _scores, _resultados = "Sin Coincidencias", 0.0, [0]
        _score, _result = 0.0, 0.0

        _result = (_match, _scores, _resultados)    

    return _match, _score, _result



def resultados(result, display = True, direct = "output"):

    def takeSecond(elem):
        return elem[1]

    _result = sorted(result, key=takeSecond)
    lista, _scores, _resultado = zip(*_result)

    if not lista[0]==None:
        fig, ax = plt.subplots()
        plt.barh(lista, _scores)
        ax.set_ylabel('Canciones')
        ax.set_xlabel('Puntuación')
        ax.set_title('Resultados del matching')
        fig.tight_layout()

        if display:
            plt.show()
        else:
            filename = direct + "/" + "Resultado" + ".png"
            plt.savefig(filename)



if __name__ == "__main__":
    
    args, argparser = arguments()
    data_filename = os.path.join("data","patrones","files")
    fingerprint_filename = os.path.join("data","patrones","fingerprints")
    test_filename = os.path.join("data","test")
    test_fp_filename = os.path.join("data","test","fp")


    if args.modo == 'play':

        print("******************************************************")
        print("******************  Play Music ***********************")
        print("******************************************************")
        if args.direct == "Default":
            print("Cargado el audio: ", args.name, " ...")
            filename = data_filename + "/" + args.name + ".wav"
        else:
            print("Cargado el audio: ", args.direct, " ...")
            filename = args.direct
        
        play(filename)

    elif args.modo == 'record':

        print("******************************************************")
        print("****************** Record music **********************")
        print("******************************************************")
        filename = "output/records" + "/" + args.name + ".wav"
        print("Grabando: ", args.name, " ...")
        grabacion(filename, seconds=args.time)

    elif args.modo == 'fingerprint':

        print("******************************************************")
        print("****************** FINGERPRINT ***********************")
        print("******************************************************")
        filename = os.path.join(data_filename, args.name + ".wav")
        filename_fp = fingerprint_filename + "/" + args.name + ".csv"
        print("Grabando para FINGERPRINT: ", args.name, " ...")
        grabacion(filename, seconds=args.time)
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
        item, score, result = Busqueda_matching(dfB, min_match=5)
        print("-------------------------------------------------------")
        print("Resultado: ")
        if not item == "Sin Coincidencias":
            print("Canción: ", item)
            print("Score: ", score)
            print("General: ", result)
            print("-------------------------------------------------------")
            print("\n")
            if args.display=="Y":
                resultados(result, display = True)
            else:
                resultados(result, display = False)
        else:
            print("ERROR: No se han encontrado coincidencias")
            print("-------------------------------------------------------")
            print("\n")

    elif args.modo == 'lista':

        print("******************************************************")
        print("***************** BASE DE DATOS **********************")
        print("******************************************************")
        lista = registro()
        for i in range(len(lista)):
            aux = len(str(i+1))
            if aux < 2:
                print(i+1, "  ", lista[i])
            elif aux < 3:
                print(i+1, " ", lista[i])
            else:
                print(i+1, "", lista[i])

        
    elif args.modo == "help":
        argparser.print_help()
