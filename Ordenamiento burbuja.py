def ordenar_burbuja(datos, ascendente=True):
    arreglo = datos[:]     # trabajamos sobre una copia, no el original
    largo   = len(arreglo)

    for pasada in range(largo - 1):
        # cada pasada "burbujea" el mayor (o menor) hacia el final
        # en la pasada k, los ultimos k elementos ya estan en su lugar
        for pos in range(largo - pasada - 1):
            izq = arreglo[pos]
            der = arreglo[pos + 1]

            hay_que_cambiar = izq > der if ascendente else izq < der
            if hay_que_cambiar:
                arreglo[pos], arreglo[pos + 1] = der, izq

    return arreglo

nums = [42, 7, 19, 3, 55]
print(ordenar_burbuja(nums))                    # [3, 7, 19, 42, 55]
print(ordenar_burbuja(nums, ascendente=False)) # [55, 42, 19, 7, 3]
print(nums)                                     # [42, 7, 19, 3, 55] sin cambios