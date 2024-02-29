#Lista números primos
def es_primo(numero):
#Se verifica si el número es menor o igual a 1
    if numero <= 1:
        return False
#Se verifica si el número es 2 o 3
    if numero <= 3:
        return True
#Se verifica si el número es divisible por 2 o 3
    if numero % 2 == 0 or numero % 3 == 0:
        return False
#Se verifica si el número es divisible por 5 o 7
    i = 5
    while i * i <= numero:
        if numero % i == 0 or numero % (i + 2) == 0:
            return False
        i += 6
    return True

#Se crea la función para devolver a la lista los números primos
def primos_en_lista(lista):
    primos = []
    for num in lista:
        if es_primo(num):
            primos.append(num)
    return primos

#Se crea la función para ingresar la lista de números
def ingresar_lista():
    numeros = []
    while True:
#Se solicita al usuario el número o la palabra "fin" para finalizar
        num = input("Ingrese un número o 'fin' para finalizar: ")
        if num.lower() == 'fin':
            return numeros
        elif num.isdigit():
            numeros.append(int(num))
        else:
            print("Por favor, ingrese un número válido.")

# Se solicitan al usuario los números para la lista
numeros = ingresar_lista()
primos = primos_en_lista(numeros)
print("Números primos en la lista:", primos)