Estadística Descriptiva e Inferencial
=======================

Medidas Descriptivas
--------------------

media, mediana, moda, varianza, desviación estándar

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

2)

.. code Python

   x = [56, 55, 60, 55, 59, 61, 60, 62, 59, 62, 57, 59, 67, 52, 65, 62, 60, 56, 66, 67]

   print('media= ' + str(np.mean(x)))
   print('mediana= ' + str(np.median(x)))
   print('varianza= ' + str(np.round(np.var(x),2)))
   print('desviación estándar= ' + str(np.round(np.std(x),2)))



