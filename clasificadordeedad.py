def etapa_de_vida(edad):
    if edad < 0:
        return "valor no valido"

    # los rangos estan en orden ascendente
    # Python para en el primer elif que se cumpla, asi que no se solapan
    if   edad <= 2:  etapa = "infante"
    elif edad <= 12: etapa = "nino"
    elif edad <= 17: etapa = "adolescente"
    elif edad <= 64: etapa = "adulto"
    else:            etapa = "senior"

    return f"{edad} anos -> {etapa}"

for e in [1, 8, 15, 35, 72]:
    print(etapa_de_vida(e))