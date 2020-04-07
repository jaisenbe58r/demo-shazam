# Demo-Shazam-App

Este proyecto pretende ser un ejercicio básico sobre la implementación un algoritmo basado en la app shazam.

El alcance del proyecto pretende poder escuchar un fragmento de audio (10seg) y poder hacer determinar una coincidencia con alguno de los audios almacenados en la base de datos. 

La finalidad de esta Base de Datos es la de almacenar los nombres de las canciones definidas como "patrones" con sus hellas musicales. A estas huellas musicales las llamamos "fingerprints" y son los espectogramas de audio generados con puntos representativos del audio, es dicir, máximos locales del espectograma que guardamos en la base de datos como puntos de interes. 

En la siguiente imagen podemos observar un espectograma de una de las canciones de referencia con un periodo de tempo de 60 segundos:

![Fingerprint Audio de referencia](/info/images/Patron.PNG)

En esta imagen se puede observar el espectograma del audio limpio, sin los máximos locales superpuestos sobre el espectograma:

![Fingerprint Audio de referencia](/info/images/espectograma.PNG)

El algoritmo se encarga de buscar relaciones de proximidad entre dos frecuencias, es decir, se almacenan parejas de frecuencias (seleccionadas como puntos característicos del espectograma) junto al desfase temporal entre estas dos. La información almacenada por audio de referencia será equivalente a un dataframe con 3 columnas, donde las dos primeras serán las frecuencias a relacionar y la tercera el desfase temporal. 

En la siguiente imagen se puede observar la información almacenada:

![Fingerprint Audio de referencia - base datos](/info/images/fingerprint_patron.PNG)

A continuacion se puede observar el espectograma del audio de evaluación que ha sido obtenido por la aplicación con un periodo de tiempo de 10 segundos:

![Fingerprint Audio a clasificar](/info/images/Default.png)

A partir del espectograma anterior se generará, de igual manera que antes, los datos de relación entre frecuencias caracteristicas:

![Fingerprint Audio de referencia - base datos](/info/images/fingerprint_eval.PNG)


Dado el fingerprint del audio a analizar, se realiza una búsqueda en la base de datos para cada uno de los audios de referencia almacenados. Con ello se identifican las parejas de frecuencias coincidentes y se realiza un conteo acumulativo de todas las coincidencias encontradas. 

A continuación se muestran las gráficas para una coincidencia, donde se puede observar claramente una diagonal de puntos a partir del segundo 27, que nos viene a decir que a partir de ese instante de tiempo el desfase temporal entre dos coincidencias es mucho menor. Así mismo, en el histograma de coincidencias se observa un acumulo de coincidencias en este periodo de tiempo.

![Resultados no coincidentes](/info/images/Safaera.png)

De lo contrario, sobre una gráfica de **no**-coincidencia, se puede ver claramente que la nube de puntos (coincidencias) está más dispersa, no siguiendo un patrón de coincidencia lineal respecto al tiempo como la gráfica anterior. Se puede observar un pico de acumulación de coincidencias sobre el segundo 45, al estar los puntos apilados respecto la coordenada "y" se podria decir que en este instante de tiempo ha habido varias coincidencias en varias frecuencias (acordes significativos coincidentes, mismas caracteristicas en un compás, mismo estilo musical, utilización del mismo efecto de sonido, etc...). Esto podría mejorarse en el algoritmo descartando los match que esten sobre la misma coordenada "y", es decir, que se produzcan en el mismo instante de tiempo.

![Resultados no coincidentes](/info/images/Falling.png)

Como curiosidad se puede observar también una diagonal sobre el segundo 15 con bastante coincidencias, esto se debe a una repetición del mismo fragmento, como por ejemplo, puede darse en un estribillo de una canción.


Por último en los resultados de cara al usuario, lo que sería el "front-end", se muestra por consola los siguientes outputs en caso de match:
```
-------------------------------------------------------
Resultado:
Canción:  Safaera
Score:  0.81
General:  [('HeyJude', 0.0, 0), ('TheBeachBoys', 0.0, 0), ('AmericanPie', 0.0, 0), 
('MyWay', 0.0, 0), ('IWantToBack', 0.0, 0), ('BlindingLights', 0.0, 0), 
('ToosieSlide', 0.0, 0), ('Roses-ImanbekRemix', 0.0, 0), ('DontStartNow', 0.0, 0), 
('DontStartNow', 0.0, 0), ('TheBox', 0.0, 0), ('DanceMonkey', 0.0, 0), ('Safaera', 0.81, 42), 
('Tusa', 0.0, 0), ('Astronomia', 0.0, 0), ('Resistire', 0.0, 0), ('UnaMalaghwayToHell', 0.19, 10),
('Falling', 0.0, 0), ('HighwayToHell', 0.19, 10)]
-------------------------------------------------------
```
Donde nos viene a decir que la canción detectada ha sido en este caso "Safaera" con un 81% de seguridad frente al resto de audios de la base de datos.

Tabién se muestra de manera más visual estos mismos resultados:

![Resultados no coincidentes](/info/images/Resultado.png)

Aquí se muestra un gráfico de barras con el porcentaje de seguridad frente al resto de canciones de manera mucho más visual e intuitiva para el usuario final.

Haciendo un guiño al periodo de crisis por el **Coronavirus** que estamos sufriendo, vamos a intentar detectar la canción ["Resistiré"](https://www.youtube.com/watch?v=K1rKj6XMt4Q) del Dúo Dinámico...

Como resultado obtenemos:

![Resultado Resistiré](/info/images/Resistire.png)

Y para el usuario final:

![Resultado Resistiré](/info/images/ResultadoResistire.png)


## Motivaciones

El proyecto esta basado en el ariticulo ["An Industrial-Strength Audio Search Algorithm"](https://www.ee.columbia.edu/~dpwe/papers/Wang03-shazam.pdf) publicado por Avery Li-Chun Wang.

También cabe destacar que me he basado en el siguiente [tutorial](https://musicinformationretrieval.com/index.html) para comprender el manejo de señales de audio desde python y que me han ayudado en gran medida con el desarrollo de gran parte de los módulos del proyecto.


## Comenzando 🚀

Estas instrucciones te permitirán obtener una copia del proyecto en funcionamiento en tu máquina local para propósitos de desarrollo y pruebas.

### Clonar el repositorio

Clonar el repositorio en una carpeta local de tu PC:

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
* playsound
* sounddevice
* pyaudio
* wave

Se puede instalar el paquete completo de dependencias de la siguiente manera:

```
pip install -r requirements.txt
```

Surge un problema en la instalación de pyaudio para versiones de python mayores a la 3.5.
En el siguiente [link](https://stackoverflow.com/questions/52283840/i-cant-install-pyaudio-on-windows-how-to-solve-error-microsoft-visual-c-14) podreis encontrar la solución para instalar el paquete de python.
También, como solución, podeis instalarlo desde el entorno de anaconda para el environment donde se va a desplegar la aplicación.


## Ejecutando la App ⚙️

La App está provista de varios modos de funcionamiento:

* "Play": Escuchar audios guardados en local.
* "Record": Prueba de grabación de audio.
* "Fingerprint": Creación de patrones de referencia para nuevos audios.
* "Evaluation": Analizar audio en tiempo real y dar los resultados de matching.
* "Base de Datos": Listar canciones de referencia almacenadas.

```
python main.py -h

_ Output: 

usage: ['main.py', '--modo', 'help'] [-h]
                                     [--modo {play,record,fingerprint,eval,lista,help}]
                                     [--name NAME] [--direct DIRECT]
                                     [--time TIME] [--display {Y,N}]

Parseador de argumentos

optional arguments:
  -h, --help            show this help message and exit
  --modo {play,record,fingerprint,eval,lista,help}
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

Se creara un archivo name.csv en la carpeta "data/patrones/fingerprints" y se añadira el nombre a la Base de datos [BASE_DATOS.txt ](BASE_DATOS.txt)


### Evaluación

Se procede a grabar 10segundos de audio y a continuación se generan los resultados. Los resultados apareceran directamente en la consola pero también se puede seleccionar el modo de visualización mediante el parseador "--display". Hay dos maneras de visualizar los resultados:

* Guardado de los histogramas de los resultados en un archivo ".png" en la carpeta "/output".
* Visualización en pantalla.

```
python main.py --modo eval --display N
```

### Lista

Este modo prende listar todas las canciones almacenadas en la base de datos.

```
python main.py --modo lista

_ _Output:

******************************************************
***************** BASE DE DATOS **********************
******************************************************
1    HeyJude
2    TheBeachBoys
3    AmericanPie
4    MyWay
5    IWantToBack
6    BlindingLights
7    ToosieSlide
8    Roses-ImanbekRemix
9    DontStartNow
10   TheBox
11   DanceMonkey
12   Safaera
13   Tusa
14   Astronomia
15   Resistire
16   UnaMala
17   Falling
18   HighwayToHell
```




## Contribuyendo 🖇️

* Si desea contribuir al código, crea un pull request.
* Si encuentra algún error, crea un issue.


## Wiki 📖

Puedes encontrar mucho más de cómo utilizar este proyecto en nuestra [Wiki](https://github.com/jaisenbe58r/demo-shazam/wiki)

## Versionado 📌

Se usa [SemVer](http://semver.org/) para el versionado. Para todas las versiones disponibles, mira los [tags en este repositorio](https://github.com/jaisenbe58r/demo-shazam/tags).

## Autores ✒️

* **Jaime Sendra Berenguer** - *Data Scientist* - [GitHub](https://github.com/jaisenbe58r) - [linkedin](https://www.linkedin.com/in/jaisenbe/)

También puedes mirar la lista de todos los [contribuyentes](https://github.com/jaisenbe58r/demo-shazam/graphs/contributors) quíenes han participado en este proyecto. 


## Licencia 📄

Este proyecto está bajo la Licencia MIT Lıcense - mira el archivo [LICENSE](LICENSE.md) para detalles


