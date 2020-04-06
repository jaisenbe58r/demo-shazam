
import os
import sys
import argparse


def arguments():
    # Parseador de argumentos
    argparser = argparse.ArgumentParser(sys.argv, description="Parseador de argumentos")


    argparser.add_argument(
        "--modo",
        choices=['play','record', 'fingerprint', 'eval', 'prueba'],
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
    

    args = argparser.parse_args()


    return args
