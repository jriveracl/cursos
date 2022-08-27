archivo = open("archivo.txt" , "w")
n = 0 
while n < 5:
    texto = input("dame un texto")
    archivo.write("texto", + "/n")
    n += 1
archivo.close()
