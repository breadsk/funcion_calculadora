from funciones import calcular

try:    

    num1 = int(input("Ingrese el primer valor: "))
    num2 = int(input("Ingrese el segundo valor: "))

    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    operacion = input("Ingrese la operacion a realizar: ")
    

    resultado = calcular(num1,num2,operacion)
            

    print(f"El resultado es: {resultado}")
except ValueError:
    print("Solo se permite numeros , intento nuevamente")
except ZeroDivisionError:
    print("No se puede dividir por cero")