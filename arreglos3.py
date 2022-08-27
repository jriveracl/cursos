edades = [15,20,30,40,50,60,70]

print("la cantidad de elementos en el arreglo son de " + str(len(edades)))
mi_edad = edades[1]
print(mi_edad)

print("mi edad es " + str(mi_edad))

#append 
edades.append(15)
print(edades)

#count
cuantos = edades.count(15)
print(cuantos)

#index
posicion = edades.index(30)
print(posicion)

#insert
numero = 99
edades.insert(3, numero)
print(edades)

#pop
ultimo_elemento = edades.pop()
print("ultimo elemento:" + str(ultimo_elemento))
print(edades)

#remove
edades.remove(99)
print(edades)

#reverse
edades.reverse()
print(edades)

#surt
edades.sort()
print(edades)

#recorre el arreglo se utiliza el for
for i in edades:
    print(i)
for i in range(len(edades)):
    print(i)
for i in range(len(edades)):
    print("la edad en la posicion "+ str(i) + " es: " + str(edades[i]))














