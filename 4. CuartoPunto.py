#Mayor suma consecutiva de números en una lista
def mayor_suma_consecutiva(lista):
#Se verifica si la lista tiene al menos dos elementos
    if len(lista) < 2:
        return None
#Se crea la variable "mayor_suma" con los dos primeros digitos
    mayor_suma = lista[0] + lista[1]
#Se recorre la lista sumando los elementos consecutivos
    for i in range(1, len(lista) - 1):
        suma_nueva = lista[i] + lista[i + 1]
#Se compara si la suma actual es mayor a la mayor suma
        if suma_nueva > mayor_suma:
            mayor_suma = suma_nueva
    return mayor_suma

#Se crea la función para ingresar la lista de números
def ingresar_lista():
    numeros = []
    continuar = True
    while continuar:
        num = input("Ingrese un número o 'fin' para finalizar: ")
        if num.lower() == 'fin':
            continuar = False
        elif num.isdigit():
            numeros.append(int(num))
        else:
            print("Ingrese un número válido.")
    return numeros

numeros = ingresar_lista()
#Se imprime el resultado de la mayor suma consecutiva
resultado = mayor_suma_consecutiva(numeros)
if resultado is not None:
    print("La mayor suma entre dos números consecutivos es:", resultado)
else:
    print("La lista debe tener al menos dos números para calcular la suma")