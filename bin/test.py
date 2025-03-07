with open("datos.txt", "r") as archivo:
    for linea in archivo:
        print(linea.strip())