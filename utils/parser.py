
import os
import sys
import argparse


def arguments():
    # Parseador de argumentos
    argparser = argparse.ArgumentParser(sys.argv, description="Parseador de argumentos")


    argparser.add_argument(
        "--modo",
        choices=['play','record', 'fingerprint', 'eval', 'lista', 'help'],
        type=str,
        default="eval",
        help="Selección de modo de funcionamiento del programa",
    )
    argparser.add_argument(
        "--name",
        type=str,
        default="Default",
        help="Nombre del archivo",
    )
    argparser.add_argument(
        "--direct",
        type=str,
        default="Default",
        help="Ruta del archivo",
    )
    argparser.add_argument(
        "--time",
        type=int,
        default=60,
        help="Tiempo de grabacion",
    )
    argparser.add_argument(
        "--display",
        choices=["Y", "N"],
        type=str, 
        default="N", 
        help="Visualizacion de Resultados"
    )
    args = argparser.parse_args()


    return args, argparser
