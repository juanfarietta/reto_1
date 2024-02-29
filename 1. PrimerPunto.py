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
        resultado = None
        return("Operador no válido")

    return resultado

numero1 = float(input("Ingrese el primer número: "))
numero2 = float(input("Ingrese el segundo número: "))
operador = input("Ingrese el caracter de la operación que desea realizar: (+, -, *, /): ")

resultado = operacion_basica(numero1, numero2, operador)
if resultado is not None:
    print("El resultado es:", resultado)