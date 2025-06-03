from funciones import sacar_promedio,limpia_decimales


try:

    while True:
        print("Saque su promedio: ")
        print("Primero ingrese sus notas")
        print("Luego ingrese el % de cada una de ellas")
        print("Comencemos")

        n1 = float(input("Ingrese la primera nota: "))
        porc1 = input(f"Su primera nota es: {n1} , ingrese el % de esta: ")
        n2 = float(input("Ingrese la segunda nota: "))
        porc2 = input(f"Su segunda nota es: {n2} , ingrese el % de esta: ")
        n3 = float(input("Ingrese la tercera nota: "))
        porc3 = input(f"Su tercera nota es: {n3} , ingrese el % de esta: ")
        n4 = float(input("Ingrese la cuarta nota: "))
        porc4 = input(f"Su cuarta nota es: {n4} , ingrese el % de esta: ")

        promedio = sacar_promedio(n1,n2,n3,n4,porc1,porc2,porc3,porc4)

        if promedio > 6.0:
            print(f"Promedio sobresaliente")
        elif promedio < 6.0 and promedio <= 55.0:
            print(f"Promedio alto")

        #print(f"Su promedio es: {promedio}")

except ValueError:
    print("Solo se permite numeros , intento nuevamente")
