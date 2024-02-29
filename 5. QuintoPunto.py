#Función que retorna palabras con los mismos carácteres
#Se crea la función para comparar las palabras
def mismo_caracter(lista):
    resultados = []
#Se recorre la lista de palabras
    for i in range(len(lista)):
        palabra = lista[i]
#Sorted ordena los carácteres de la palabra
        caracteres = sorted(palabra)
        encontrado = False
        for j in range(i + 1, len(lista)):
            otra_palabra = lista[j]
            if len(otra_palabra) == len(palabra) and sorted(otra_palabra) == caracteres:
                encontrado = True
#Se agrega la palabra a la lista de resultados
        if encontrado:
            resultados.append(palabra)
    return resultados

#Se crea la función para ingresar la lista de palabras
def ingresar_lista():
    palabras = []
    continuar = True
    while continuar:
        palabra = input("Ingrese una palabra o 'fin' para terminar: ")
        if palabra.lower() == 'fin':
            continuar = False
        else:
            palabras.append(palabra)
    return palabras

palabras = ingresar_lista()
resultado = mismo_caracter(palabras)
print("Palabras con los mismos caracteres:", resultado)