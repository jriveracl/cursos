a = [[1,2,3], [4,5,6], [7,8,9]]

array_datos = [[]]

array_datos[0].append("fernando colmenares")
array_datos[0].append(56)
array_datos[0].append("medellin")
array_datos[0].append("le gusta la comida")

array_datos.append([])

array_datos[1].append("juan carlos")
array_datos[1].append(26)
array_datos[1].append("EE.UU")
array_datos[1].append("le gusta el arroz")

array_datos.append([])

array_datos[2].append("maria paula")
array_datos[2].append(18)
array_datos[2].append("cucuta")
array_datos[2].append("le gusta ir a la iglesia")

#print("la cantidad de datos en el arreglo es de " + str(len(array_datos)))


for i in range(len(array_datos)):
    print(array_datos[i][0])
    print(array_datos[i][1])
    print(array_datos[i][2])
    print(array_datos[i][3])




