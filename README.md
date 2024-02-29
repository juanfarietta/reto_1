# Reto 1
## Primer Código
Crear una función que realice operaciones básicas (suma, resta, multiplicación, división) entre dos números, según la elección del usuario, la forma de entrada de la función será los dos operandos y el caracter usado para la operación. entrada: (1,2,"+"), salida (3).
```
#Se crea la función para la realización de operaciones básicas
def operacion_basica(numero1, numero2, operador):
    if operador == "+":
        resultado = numero1 + numero2
    elif operador == "-":
        resultado = numero1 - numero2
    elif operador == "*":
        resultado = numero1 * numero2
    elif operador == "/":
        resultado = numero1 / numero2
    else:
#Se retorna un mensaje de error si el operador no es válido
        resultado = None
        return("Operador no válido")

    return resultado

#Se solicitan los datos al usuario
numero1 = float(input("Ingrese el primer número: "))
numero2 = float(input("Ingrese el segundo número: "))
operador = input("Ingrese el caracter de la operación que desea realizar: (+, -, *, /): ")

#Se imprime el resultado de la operación
resultado = operacion_basica(numero1, numero2, operador)
if resultado is not None:
    print("El resultado es:", resultado)
```
Para la realización de este código, primero, se crea la función para la realización de las operaciones básicas, estas son la suma, la resta, la multiplicación y la división; y son representadas por los símbolos +, -, *, /, respectivamente. En caso de que se ingrese un carácter no válido, aparecerá el mensaje del error. Posteriormente, se solicitan los números y el operador al usuario. Y finalmente, se obtiene el resultado.
## Segundo Código
Realice una función que permita validar si una palabra es un palíndromo. Condición: No se vale hacer slicing para invertir la palabra y verificar que sea igual a la original.
```
#Determinar palíndromos
def palindromo(palabra):
#El "lower" convierte todos los carácter en minúsculas
    palabra = palabra.lower()
    longitud_palabra = len(palabra)
#Simetricamente se comparan los caracteres de la palabra
    for i in range(longitud_palabra):
        if palabra[i] != palabra[longitud_palabra-1-i]:
            return False
    return True

#Se solicita la palabra al usuario
def entrada():
    palabra = input("Ingrese una palabra: ")
    if palindromo(palabra):
        print("La palabra es un palíndromo")
    else:
        print("La palabra no es un palíndromo")
entrada()
```
Inicialmente se crea la función, se convierten todos los carácteres en minúsculas por medio del "lower", dado que python detecta las mayúsculas como carácteres diferentes a las minúsculas y sin este comando se el código no funcionaría de manera adecuada. Después se determina la longitud de la palabra. Posteriormente, con el "for i in range" la función se encarga de comparar el primer carácter con el último, el segundo con el penúltimo, y así sucesivamente de manera simétrica. Para finalizar, se le pide al usuario que ingrese una palabra, se comprueba si es o no un palíndromo, y se le indica al usuario.
## Tercer Código
Escribir una función que reciba una lista de números y devuelva solo aquellos que son primos. La función debe recibir una lista de enteros y retornar solo aquellos que sean primos.
```
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
            print("Ingrese un número válido.")

numeros = ingresar_lista()
primos = primos_en_lista(numeros)
print("Números primos en la lista:", primos)
```
Se inicia con la creación de la función para determinar si es primo. A través del "if numero <= 1:" se verifica si el número es 1 o menor, dado que los números primos son aquellos enteros positivos mayores que 1 y que tienen exactamente dos divisores positivos, el 1 no contaría como primo. Con el "if numero <= 3:" se determina a los números 2 y 3 como primos ya que aunque estos no cumplen el patrón de común divisibilidad, sí son primos. Con la función "if numero % 2 == 0 or numero % 3 == 0:" se verifica la divisibilidad entre 2 y 3. Al igual con la siguiente función, ya que con esta se verifica la divisibilidad entre 5 y 7. Para continuar, se crean las funciones para que en el resultado de la lista solo se pongan los primos y la función para ingresar la lista de números. Finalmente, se colocan las funciones para que el usuario termine la lista escribiendo 'fin', y la función "num.isdigit():" con la cual se verifica si sí se trata de un número.
## Cuarto Código
Escribir una función que reciba una lista de números enteros y retorne la mayor suma entre dos elementos consecutivos.
```
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
```
Para este código, se inicia creando la función, y verificando que la lista creada tenga por lo menos 2 elementos. Se crea la variable "mayor_suma", la cual se inicia con la suma de los dos primeros elementos de la lista. Después se recorre la lista a través de la función "for i in range(1, len(lista) - 1):" esto permite que se creen sumas nuevas entre todos los elementos consecutivos, y con esto ya dado, en caso de que alguna de las nuevas sumas de consecutivos sea mayor que las demás, pasará a ser la nueva "mayor_suma". Se crea la función para la lista de números y se imprime el resultado.
## Quinto Código
Escribir una función que reciba una lista de string y retorne unicamente aquellos elementos que tengan los mismos caracteres. e.g. entrada: ["amor", "roma", "perro"], salida ["amor", "roma"]
```
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
```
Inicialmente, se crea la función para comparar las palabras dadas, con la función "for i in range(len(lista)):" se recorre la lista de palabras y se determina su longitud. A través de la función "sorted" ordena los carácteres de las palabras dadas, gracias a lo cual, el código verifica de una manera más sencilla la similitud entre las palabras dadas. Si la palabra de la lista si coincide con otra, se agrega al resultado final. Y para finalizar, al igual que en el punto 3 y 4, se crea la función para ingresar la lista y se imprime el resultado.
