def serie_fibonacci(cantidad):
    if cantidad <= 0:
        print("Ingresa una cantidad positiva.")
        return

    anterior, actual = 0, 1

    for paso in range(cantidad):
        print(f"  termino {paso + 1}: {anterior}")
        # el siguiente termino es la suma de los dos anteriores
        anterior, actual = actual, anterior + actual

serie_fibonacci(7)
# termino 1: 0
# termino 2: 1
# termino 3: 1
# termino 4: 2
# termino 5: 3
# termino 6: 5
# termino 7: 8