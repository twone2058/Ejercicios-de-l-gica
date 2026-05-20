import math

def primo(n):
    # por definicion, los primos son enteros mayores que 1
    if n < 2:
        return False

    # solo revisamos hasta la raiz cuadrada
    # si n tiene un divisor mayor que sqrt(n), el otro es menor que sqrt(n)
    # y ya lo habriamos encontrado antes
    tope = int(math.sqrt(n))

    for divisor in range(2, tope + 1):
        if n % divisor == 0:
            return False

    return True

# mostrar todos los primos menores que 50
primos = [x for x in range(2, 50) if primo(x)]
print(primos)
# [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]