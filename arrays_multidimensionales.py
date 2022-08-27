a = [[1,2,3],[4,5,6],[7,8,9]]
print(a)

for i in range(len(a)):
    print(i)
    for j in range(len(a[i])):
        print(a[i][j])

arrays_datos = [[]]

arrays_datos[0].append("pepe")
arrays_datos[0].append("22")
arrays_datos[0].append("argentina")

arrays_datos.append([])

arrays_datos[1].append("juan jose")
arrays_datos[1].append("18")
arrays_datos[1].append("colombia")

arrays_datos.append([])

arrays_datos[2].append("juan camilo")
arrays_datos[2].append("22")
arrays_datos[2].append("colombia")

print(arrays_datos)
print("la cantidad de datos que hay es: " + str(len(arrays_datos)))