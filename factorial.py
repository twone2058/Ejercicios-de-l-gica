def calcular_factorial(n):
    if n < 0:
        print("El factorial solo esta definido para enteros >= 0.")
        return

    # caso base: 0! = 1 por definicion matematica
    producto = 1

    for factor in range(2, n + 1):
        producto *= factor

        # limite artificial para simular overflow como en C o Java
        if producto > 10 ** 300:
            print(f"Overflow al calcular {n}! (supera 10^300)")
            return

    print(f"{n}! = {producto}")

calcular_factorial(0)    # 0! = 1
calcular_factorial(6)    # 6! = 720
calcular_factorial(12)   # 12! = 479001600
calcular_factorial(-1)   # error