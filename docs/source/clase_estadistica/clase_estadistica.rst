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
   print('varianza= ' + str(np.var(x)))
   print('desviación estándar= ' + str(np.std(x)))


