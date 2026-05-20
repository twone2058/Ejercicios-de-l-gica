def imc(peso_kg, altura_m):
    if peso_kg <= 0 or altura_m <= 0:
        print("Peso y altura deben ser valores mayores que cero.")
        return

    indice = round(peso_kg / altura_m ** 2, 2)

    # tabla de categorias segun la OMS
    if   indice < 18.5: categoria = "bajo peso"
    elif indice < 25.0: categoria = "peso normal"
    elif indice < 30.0: categoria = "sobrepeso"
    else:               categoria = "obesidad"

    print(f"Peso: {peso_kg} kg | Altura: {altura_m} m")
    print(f"IMC : {indice} ({categoria})")

imc(68, 1.72)   # 22.99 -> peso normal
imc(95, 1.68)   # 33.66 -> obesidad
imc(48, 1.70)   # 16.61 -> bajo peso