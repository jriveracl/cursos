import numpy as np
# matrizes de ceros
ceros = np.zeros((4,3))
print(ceros)

#matrizes de unos
unos = np.ones((4,3))
print(unos)

#matrizes con numeros aleatorios
aleatorios = np.random.random((3,3))
print(aleatorios)

#matrizes vacias
vacia = np.empty((4,3))
print(vacia)

#matrizes con un solo numero de relleno
full = np.full((5,6),8)
print(full)

#matrizes con numeros espaciados
espacio1 = np.arange(0, 30, 5)
print(espacio1)

#matrizes con numeros espaciados
espacio2 = np.linspace(0,2,5)
print(espacio2)

#matriz idxentidad
identidad1 = np.eye(4,4)
print(identidad1)

#matriz identidad
identidad2 = np.identity(4)
print(identidad2)



