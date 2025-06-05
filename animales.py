
while True:
    try:
        cant = int(input("Ingrese la cantidad de animales a registrar: "))
        break
    except ValueError:
        print("Debe ingresar un número entero")

mas_de_5 = 0
menos_o_igual = 0

for _ in range(cant):
    raza = input("Ingrese la raza de su animal: ")
    valido = False
    while not valido:
        try:
            anios = int(input("Ingrese los años de su mascota: "))
            valido = True
        except ValueError:
            print("Edad debe ser número entero")
    if anios > 5:
        print(f"Raza mascota: {raza}")
        print("Su mascota debe tener vacunas tipo B")
        mas_de_5 += 1
    else:
        print(f"Raza mascota: {raza}")
        print("Su mascota debe tener vacunas tipo A")
        menos_o_igual += 1

print(f"Se registraron {mas_de_5} mascotas con mas de 5 años")
print(f"Se registraron {menos_o_igual} mascotas con menos de 5 años o igual")