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



