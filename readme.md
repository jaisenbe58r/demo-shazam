# Demo-Shazam-App

Este proyecto pretende ser un ejercicio básico sobre la implementación un algoritmo basado en la app shazam.

El alcance del proyecto pretende poder escuchar un fragmento de audio (10seg) y poder hacer "match" con alguno de los audios almacenados en la base de datos. 

Esta Base de datos, pretende almacenar los nombres de las canciones almacenadas como "patrones" con sus hellas musicales. A estas huellas musicales las llamamos "fingerprints" y son los espectogramas de audio generados con puntos representativos del audio, es dicir, máximos locales del espectograma que guardamos en la base de datos como puntos de interes. En la siguiente imagen podemos observar un espectograma de una de las canciones de referencia:

![Fingerprint Audio de referencia](/info/images/Patron.PNG)

Como comentabamos

![Fingerprint Audio a clasificar](/info/images/Default.png)


## How is it work

Me he basado en el ariticulo "An Industrial-Strength Audio Search Algorithm" publicado por Avery Li-Chun Wang. Podéis leerlo en el siguiente enlace: [here](https://www.ee.columbia.edu/~dpwe/papers/Wang03-shazam.pdf)

Me he basado en el siguiente tutorial para comprender el manejo de señales de audio desde python:

[here](https://musicinformationretrieval.com/index.html)


## Comenzando 🚀

_Estas instrucciones te permitirán obtener una copia del proyecto en funcionamiento en tu máquina local para propósitos de desarrollo y pruebas._

Mira **Deployment** para conocer como desplegar el proyecto.


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

### Instalación 🔧

_Una serie de ejemplos paso a paso que te dice lo que debes ejecutar para tener un entorno de desarrollo ejecutandose_

_Dí cómo será ese paso_

```
Da un ejemplo
```

_Y repite_

```
hasta finalizar
```

_Finaliza con un ejemplo de cómo obtener datos del sistema o como usarlos para una pequeña demo_

## Ejecutando las pruebas ⚙️

_Explica como ejecutar las pruebas automatizadas para este sistema_

### Analice las pruebas end-to-end 🔩

_Explica que verifican estas pruebas y por qué_

```
Da un ejemplo
```

### Y las pruebas de estilo de codificación ⌨️

_Explica que verifican estas pruebas y por qué_

```
Da un ejemplo
```


## Contribuyendo 🖇️

* Si desea contribuir al código, crea un pull request
* Si encuentra algún error, crea un issue


## Wiki 📖

Puedes encontrar mucho más de cómo utilizar este proyecto en nuestra [Wiki](https://github.com/tu/proyecto/wiki)

## Versionado 📌

Usamos [SemVer](http://semver.org/) para el versionado. Para todas las versiones disponibles, mira los [tags en este repositorio](https://github.com/tu/proyecto/tags).

## Autores ✒️

* **Jaime Sendra Berenguer** - *Data Scientist* - [jaisenbe58r](https://github.com/jaisenbe58r) - [linkedin](www.linkedin.com/in/jaisenbe)

También puedes mirar la lista de todos los [contribuyentes](https://github.com/jaisenbe58r/demo-shazam/graphs/contributors) quíenes han participado en este proyecto. 


## Licencia 📄

Este proyecto está bajo la Licencia MIT Lıcense - mira el archivo [LICENSE.md](LICENSE.md) para detalles


