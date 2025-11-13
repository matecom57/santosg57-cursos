Raices de ecuaciones
=====================

RaicesDeEcuaciones.pdf

**DEFINICIÓN:**

La raíz de una ecuación es aquel valor de la variable independiente que hace que el resultado de la 
ecuación sea cero o por lo menos se acerque a cero con una cierto grado de aproximación deseado (error 
máximo permitido).

**OBJETIVOS:**

Al terminar esta unidad de estudio, el estudiante estará en capacidad de:

• Aprender el concepto de raíz de una ecuación

• Comprender las distintas técnicas usadas para hallar raíces de ecuaciones

• Evaluar la confiabilidad de cada método

• Estar en capacidad de elegir el mejor método para aplicarlo en la solución de problemas de ingeniería, 
relacionados con la búsqueda de raíces de una ecuación.

1.1 MÉTODOS BASADOS EN INTERVALOS
---------------------------------

Su característica fundamental es que se elige un intervalo [a, b] dentro del cual se encuentre la raíz 
buscada. No hay una regla a seguir para la selección de este intervalo, sin embargo, se debe cumplir que 
en los extremos del intervalo la función cambie de signo lo cual que equivale a que: f(a)*f(b) < 0. Una 
primera aproximación a la solución se logra al elaborar un modelo gráfico de la ecuación y a partir de él, 
por simple inspección, seleccionar el intervalo más adecuado.

Figura 1. Raíces en diferentes intervalos.

Si al evaluar la función, en los extremo del intervalo elegido, presenta igual signo puede no existir 
raíces o existir un número impar de ellas. Si la función cambia de signo esto nos indica que al menos hay 
una raíz en dicho intervalo. Los casos que requieren análisis especial se presentan cuando la función 
tiene puntos tangentes al eje x o cuando tiene discontinuidades.

1.1.1 Criterio de convergencia.

Se considera que se ha encontrado una respuesta satisfactoria cuando el valor hallado para la variable 
faltante (x) cumple con alguno de los siguientes criterios:

.. math::

   |f(x)| < Tol; ó |\frac{|X_r -X_{r - 1}|}{|X_r|} < Tol 

Siendo Xr , y X r-1 los valores de las dos últimas iteraciones y Tol es el nivel máximo de error aceptado 
que se puede definir ya sea con base en el número de cifras significativas (NCS) Tol = 5x10 -(NCS+1) o en 
el número de cifras decimales (ND) que se desea obtener, Tol = 5x10-(ND+1) . Otro criterio para terminar 
el proceso es que se exceda el número máximo de iteraciones propuesto, en cuyo caso lo más probable es que 
la solución no esté convergiendo hacia un valor determinado (cada vez se aleja más del valor estimado), 
por lo tanto se debe probar con otra estrategia de solución o revisar muy bien lo cálculos matemáticos 
realizados para ver si no se están cometiendo errores en el proceso.

1.1.2 Método gráfico.

Lo esencial en este método es poder construir un modelo gráfico de la ecuación y luego por inspección 
estimar una aproximación a la raíz.

El mayor inconveniente de éste método es su poca precisión y exactitud. Sin embargo, hoy día se cuenta con 
excelentes herramientas de software para realizar rápidamente gráficas con un alto grado de realismo. El 
primer problema a resolver es ¿que intervalo usar para construir la gráfica? No hay regla que nos diga 
como hacerlo, por eso lo mejor es probar con varios intervalos hasta encontrar el más adecuado, no 
obstante es importante considerar las características particulares del problema que vamos a resolver, ya 
que eso nos dará una idea del rango de posibles soluciones, por ejemplo si queremos hallar una magnitud 
física como velocidad, distancia, masa, etc., sabemos que no tiene sentido probar con valores negativos, 
por lo tanto podemos graficar rangos a partir de cero.

Como ejemplo consideremos las funciones: f(x) = seno(3x) + Cos(x) y f(x) = e x – x -2. El conjunto de 
posibles valores que puede tomar x están en el intervalo (-∞, ∞), pero sabemos además que la primera 
función tiene período 2π, lo cual nos ayuda a limitar e intervalo a graficar.

Usando MatLab podemos graficar la primera función el intervalo [0, π] y la segunda en el intervalo [-4, 
4], para obtener un modelo gráfico como el de la figura 2.

