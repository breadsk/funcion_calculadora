from random import randint

def calcular(num1,num2,operacion):
    if operacion == 1:
        return num1 + num2
    elif operacion == 2:
        return num1 - num2
    elif operacion == 3:
        return num1 * num2
    elif operacion == 4:
        return num1 // num2
    
def sacar_puntaje(porcentaje,puntaje):
    return (puntaje * porcentaje) / 100

def limpia_decimales(porcentaje):    
    porcentaje = "0."+ porcentaje
    porcentaje = float(porcentaje)
    return porcentaje

def sacar_promedio(nota1,nota2,nota3,nota4,porc1,porc2,porc3,porc4):
    nota_final = (nota1 * limpia_decimales(porc1)) + (nota2 * limpia_decimales(porc2)) + (nota3 * limpia_decimales(porc3)) + (nota4 * limpia_decimales(porc4))
    nota_final = round(nota_final,1)
    return nota_final

def rifa(n1,n2,n3,n4,n5):
    resultado = randint(1,5)
    if resultado == int(n1):
        return "Gano!!! "+ n1
    elif resultado == int(n2):
        return "Gano!!! "+ n2
    elif resultado == int(n3):
        return "Gano!!! "+ n3
    elif resultado == int(n4):
        return "Gano!!! "+ n4
    elif resultado == int(n5):
        return "Gano!!! "+ n5