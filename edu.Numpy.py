# edu.Numpy
#Numpy basics (Conceptos básicos de Numpy)

"""HOLA, SOY ESTEBAN Y TE DOY LA BIENVENIDA A ESTE APUNTE BÁSICO DE NUMPY. Mensaje para los estudiantes/alumnos/interesados: 
En este caso he decidido comenzar con las bases de Numpy en el idioma castellano, 
pero no dudes en consultarme si tienen alguna duda sobre cómo sería en inglés. Además, tener en cuenta que se utiliza notación de punto 
para acceder a las funciones del paquete Numpy""" 
"""Hi!,I am Esteban. An english version of this material will be available too!"""

# Aprendiendo sobre el paquete Numpy (Num: Numerical, py, Python...). Numpy es una herramienta fundamental para la computación científica. 
# Como siempre, primero se procede a importar el paquete que será utilizado. En este caso, el alias estándar de Numpy es np:

import numpy as np                                                                                                                                                                                                

# Para crear un objeto del tipo array (AKA "a Numpy array") a partir de una lista de Python: 

v = np.array([1,2,3,4])    # he creado un arreglo unidimensional (1D, también denominado "vector") de cuatro elementos. 

#¿Como verificar que se ha creado un arreglo?, con la función type():

print(type(v))             # el código ejecutado debe mostrar el output: <class 'numpy.ndarray'>

print(v)                   # en este caso, el código ejecutado debe mostrar el output: [1 2 3 4]
 
# También se puede ver la forma del objeto creado (the shape of the array), con la funcion shape():

print(np.shape(v)) # el código ejecutado debe mostrar el output: (4,)

# Los arreglos también pueden ser bidimensionales (2D, también denominado "matriz"). Si se procede análogamente al caso anterior:
v2 = np.array([[5,6],[7,8]])
print(type(v2))          
print(v2)                  # en este caso, el código ejecutado debe mostrar una matriz de dos filas y dos columnas: [[5 6] 
#                                                                                                                   [7 8]]
print(np.shape(v2)) # el código ejecutado debe mostrar el output: (2, 2) , un tupla que indica 2 filas y 2 columnas. 

"""¿Cómo acceder a los valores del arreglo creado?: con índices enteros. En el caso de un vector, será suficiente UN entero; en                                                                                                                        
el caso de una matriz, será necesario especificar dos enteros:"""

print(v[0]) # se accede al primer elemento del vector v: 1
print(v[3]) # se accede al último elemento del vector v: 4

# A continuación, selecciono cada uno de los elementos de la matriz v2 mediante dos enteros: el 1° indica el número de fila y el 2°, de columna. 

print(v2[0,0]) # se accede al elemento de la primera fila y primera columna de v2, es decir: 5
print(v2[0,1])
print(v2[1,0])
print(v2[1,1])

print(v2[0,0] + v2[0,1]) # Operando con elementos de la matriz: aquí simplemente sumo los dos elementos de la primera fila. 
