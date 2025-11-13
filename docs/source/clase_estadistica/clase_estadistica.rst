Estadística Descriptiva e Inferencial
=======================

Medidas Descriptivas
--------------------

media, mediana, moda, varianza, desviación estándar, minimo, maximo

histograma, simetria

Ejemplos:

1)

.. code:: Python

   import numpy as np

   x = [57, 62, 51, 59, 51, 52, 57, 45, 45, 65, 53, 63, 51, 54, 58, 43, 49, 64, 57, 60]

   print('media= ' + str(np.mean(x)))
   print('mediana= ' + str(np.median(x)))
   print('varianza= ' + str(np.round(np.var(x),2)))
   print('desviación estándar= ' + str(np.round(np.std(x),2)))
   print('mínimo= ' + str(np.min(x)))
   print('máximo= ' + str(np.max(x)))

2)

.. code:: Python

   x = [56, 55, 60, 55, 59, 61, 60, 62, 59, 62, 57, 59, 67, 52, 65, 62, 60, 56, 66, 67]

   print('media= ' + str(np.mean(x)))
   print('mediana= ' + str(np.median(x)))
   print('varianza= ' + str(np.round(np.var(x),2)))
   print('desviación estándar= ' + str(np.round(np.std(x),2)))
   print('mínimo= ' + str(np.min(x)))
   print('máximo= ' + str(np.max(x)))

**Cómo Hacer un Histograma?????**

.. code:: Python

   edades = [12, 15, 13, 12, 18, 20, 19, 20, 13, 12, 13, 17, 15, 16, 13, 14, 13, 17, 19]

   intervalos = [(10, 13), (13, 16), (16, 19), (19, 22)]

   mapa_edades = dict(zip(intervalos, [0] * len(intervalos)))

   for edad in edades:
	for intervalo in mapa_edades:
		if intervalo[0] <= edad < intervalo[1]:
			mapa_edades[intervalo] += 1
			break

   for valor in sorted(mapa_edades):
	print(f'{valor}: {"*" * mapa_edades[valor]}')


.. code:: Python

   import matplotlib.pyplot as plt
 
   valores = [23,22,28,32,24,28,32,15,26,22,24,24,26,28,32,41,20,39,51,18,23,28,26,34,17]
   plt.hist(valores)
   plt.show()

**Poligono de Frecuencias**

.. code:: Python

   import matplotlib.pyplot as plt
   import numpy as np

   datos = np.random.randint(0, 100, 50)

   frecuencias, bordes, patches = plt.hist(datos, bins=10, edgecolor='black')

   centros_intervalo = 0.5 * (bordes[:-1] + bordes[1:])

   plt.plot(centros_intervalo, frecuencias, marker='o')

   plt.xlabel("Valores")
   plt.ylabel("Frecuencia")
   plt.title("Polígono de Frecuencia")

   plt.show()


**Crear un boxplot**

.. code:: Python

   import matplotlib.pyplot as plt
   import numpy as np

   data = [np.random.normal(0, std, 100) for std in range(1, 4)]

   plt.boxplot(data)

   plt.title("Box Plot Example")
   plt.xlabel("Data Sets")
   plt.ylabel("Values")

   plt.show()

**Grafica de Barras**

.. code:: Python

   import matplotlib.pyplot as plt

   x = ["A", "B", "C"]
   y = [3, 5, 1]
   error = [0.8, 0.4, 0.2]

   plt.bar(x = x, height = y, yerr = error, capsize = 10, ecolor = "r")
   plt.show()

Intervalo de de Confianza
------------------------

**El intervalo de confianza (IC)** es un rango estadístico que estima el valor real de un parámetro 
poblacional, como la media poblacional, con una probabilidad específica. Proporciona un rango donde es 
probable que se encuentre el valor real, según los datos de la muestra. El nivel de confianza (p. ej., 95 
%) indica la certeza de que el valor real se encuentra dentro de este rango. 

**Fórmula:**

.. math::

   \text{Intervalo de confianza} = \bar{x} \pm t \times \left ( \frac{s}{n} \right )

* ``x``: media muestral
* ``t``: valor t que corresponde al nivel de confianza
* ``s``: desviación estándar de la muestra
* ``n``: tamaño de la muestra

**Usando scipy.stats.t.interval**

Este método requiere proporcionar el nivel de confianza, la media muestral, la desviación estándar 
muestral y el tamaño de la muestra. Es especialmente útil para muestras pequeñas donde se desconoce la 
desviación estándar poblacional y se desea estimar el rango en el que se encuentra la media verdadera, con 
un nivel de confianza específico.

.. code:: Python

   import numpy as np
   import scipy.stats as stats

   d = [12, 15, 14, 10, 13, 17, 14, 15, 16, 14]
   cl = 0.95 # confidence level

   ci = stats.t.interval(confidence_level, df=len(d)-1, loc=np.mean(d), scale=np.std(d, ddof=1) / np.sqrt(len(d)))
   print(ci)

