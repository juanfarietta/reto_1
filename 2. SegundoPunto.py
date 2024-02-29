#Determinar palíndromos
def palindromo(palabra):
    palabra = palabra.lower()
    longitud_palabra = len(palabra)
    for i in range(longitud_palabra):
        if palabra[i] != palabra[longitud_palabra-1-i]:
            return False
    return True

def entrada():
    palabra = input("Ingrese una palabra: ")
    if palindromo(palabra):
        print("La palabra es un palíndromo")
    else:
        print("La palabra no es un palíndromo")
entrada()
