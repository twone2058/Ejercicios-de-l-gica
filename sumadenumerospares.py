# version for: range con paso 2 genera solo pares
def pares_con_for(limite):
    acumulado = 0
    for num in range(2, limite + 1, 2):
        acumulado += num
    print(f"[for]   suma de pares hasta {limite} = {acumulado}")

# version while: avanzamos manualmente de dos en dos
def pares_con_while(limite):
    acumulado = 0
    actual    = 2
    while actual <= limite:
        acumulado += actual
        actual    += 2
    print(f"[while] suma de pares hasta {limite} = {acumulado}")

pares_con_for(20)
pares_con_while(20)
# ambos: suma de pares hasta 20 = 110