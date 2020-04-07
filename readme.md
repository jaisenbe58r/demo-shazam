# Demo-Shazam-App

Este proyecto pretende ser un ejercicio básico sobre la implementación un algoritmo basado en la app shazam.

El alcance del proyecto pretende poder escuchar un fragmento de audio (10seg) y poder hacer "match" con alguno de los audios almacenados en la base de datos. 

Esta Base de datos, pretende almacenar los nombres de las canciones almacenadas como "patrones" con sus hellas musicales. A estas huellas musicales las llamamos "fingerprints" y son los espectogramas de audio generados con puntos representativos del audio, es dicir, máximos locales del espectograma que guardamos en la base de datos como puntos de interes. 

En la siguiente imagen podemos observar un espectograma de una de las canciones de referencia con un periodo de tempo de 60 segundos:

![Fingerprint Audio de referencia](/info/images/Patron.PNG)

El agoritmo se encarga de buscar relaciones de proximidad entre dos frecuencias, es decir, se almacenan parejas de frecuencias (seleccionadas como puntos caracteristicos del espectograma) junto al desfase temporal entre estas dos. La información almacenada por audio de referencia sera equivalente a un dataframe con 3 columns, donde las dos primeras seran las frecuencias a relacionar y la tercera el desfase temporal. 

En la siguiente imagen se puede observar la información almacenada:

![Fingerprint Audio de referencia - base datos](/info/images/fingerprint_patron.PNG)

A continuacion se puede observar el espectograma del audio a analizar que ha sido obtenido por la aplicación con un periodo de tiempo de 10 segundos:

![Fingerprint Audio a clasificar](/info/images/Default.png)

A partir del espectograma anterior se generará, de igual manera que antes, los datos de relación entre frecuencias caracteristicas:

![Fingerprint Audio de referencia - base datos](/info/images/fingerprint_eval.PNG)







## Motivaciones

El proyecto esta basado en el ariticulo "An Industrial-Strength Audio Search Algorithm" publicado por Avery Li-Chun Wang. Podéis leerlo en el siguiente enlace: [here](https://www.ee.columbia.edu/~dpwe/papers/Wang03-shazam.pdf)

Me he basado en el siguiente tutorial para comprender el manejo de señales de audio desde python:

[here](https://musicinformationretrieval.com/index.html)


## Comenzando 🚀

_Estas instrucciones te permitirán obtener una copia del proyecto en funcionamiento en tu máquina local para propósitos de desarrollo y pruebas._

### Colnar el repositorio

Clonar el repositorio en una carpeta local a tu workstation:

```
git clone https://github.com/jaisenbe58r/demo-shazam.git
```


### Pre-requisitos 📋

En El archivo requirements.txt se puede encontrar todas las dependencias:

* numpy
* pandas
* librosa
* matplotlib
* scipy
* msvcrt
* playsound
* sounddevice
* pyaudio
* wave

Se puede instalar el paquete completo de dependencias de la siguiente manera:

```
pip install -r requirements.txt
```



## Ejecutando la App ⚙️

La App está provista de varios mods de funcionamiento:

* "Play": Escuchar audios guardados en local.
* "Record": Prueba de grabación de audio.
* "Fingerprint": Creación de patrones de referencia para nuevos audios.
* "Evaluation": Analizar audio en tiempo real y dar los resultados de matching.

```
python main.py -h

**Output:** 

usage: ['main.py', '--modo', 'help'] [-h]
                                     [--modo {play,record,fingerprint,eval,help}]
                                     [--name NAME] [--direct DIRECT]
                                     [--time TIME] [--display {Y,N}]

Parseador de argumentos

optional arguments:
  -h, --help            show this help message and exit
  --modo {play,record,fingerprint,eval,help}
                        Selección de modo de funcionamiento del programa
  --name NAME           Nombre del archivo
  --direct DIRECT       Ruta del archivo
  --time TIME           Tiempo de grabacion
  --display {Y,N}       Visualizacion de Resultados
  ```

### Play

Escuchar audios guardados en local, en este caso se reproducira el archivo "data/test/Default.wav" con el siguiente comando:

```
python main.py --modo play --direct data/test/Default.wav
```

### Record

Prueba de grabación de audio. El audio se guardará en la carpeta "output/records". Se le puede asignar un nombre con el parseador "--name" y también se puede asignar el tiempo de grabación "--time" (por defecto es de 60seg).

```
python main.py --modo record --name Prueba --time 10
```


### Fingerprint

Añadir patrones a la Base de Datos. Se selecciona el nombre de la canción con el parseador "--name" y se selecciona el tiempo de grabación "--time" (por defecto en 60seg).

```
python main.py --modo fingerprint --name HighwayToHell --time 60
```

Se creara un archivo name.csv en la carpeta "data/patrones/fingerprints" y se añadira el nombre a la Base de datos (archivo BASE_DATOS.txt)


### Evaluación

Se procede a grabar 10segundos de audio y a continuación se generan los resultados. Los resultados apareceran directamente en la consola pero también se puede seleccionar el modo de visualización mediante el parseador "--display". Hay dos maneras de visualizar los resultados:

* Guardado de los histogramas de los resultados en un archivo ".png" en la carpeta "/output".
* Visualización en pantalla.

```
python main.py --modo eval --display N
```



## Contribuyendo 🖇️

* Si desea contribuir al código, crea un pull request
* Si encuentra algún error, crea un issue


## Wiki 📖

Puedes encontrar mucho más de cómo utilizar este proyecto en nuestra [Wiki](https://github.com/jaisenbe58r/demo-shazam/wiki)

## Versionado 📌

Se usa [SemVer](http://semver.org/) para el versionado. Para todas las versiones disponibles, mira los [tags en este repositorio](https://github.com/jaisenbe58r/demo-shazam/tags).

## Autores ✒️

* **Jaime Sendra Berenguer** - *Data Scientist* - [GitHub](https://github.com/jaisenbe58r) - [linkedin](https://www.linkedin.com/in/jaisenbe/)

También puedes mirar la lista de todos los [contribuyentes](https://github.com/jaisenbe58r/demo-shazam/graphs/contributors) quíenes han participado en este proyecto. 


## Licencia 📄

Este proyecto está bajo la Licencia MIT Lıcense - mira el archivo [LICENSE](LICENSE.md) para detalles


