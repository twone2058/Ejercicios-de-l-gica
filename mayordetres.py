def encontrar_mayor(valores):
    tope = max(valores)
    empates = valores.count(tope)

    # mostramos un mensaje distinto si hay empate
    if empates > 1:
        print(f"Mayor: {tope}  ({empates} valores comparten el maximo)")
    else:
        print(f"Mayor: {tope}")

encontrar_mayor([3, 18, 7])    # Mayor: 18
encontrar_mayor([10, 10, 4])   # Mayor: 10  (2 valores comparten el maximo)
encontrar_mayor([5, 5, 5])     # Mayor: 5   (3 valores comparten el maximo)