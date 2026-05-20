def bisiesto(year):
    # un año es bisiesto si cumple alguna de estas dos condiciones:
    # a) divisible por 4 pero NO por 100
    # b) divisible por 400 (excepcion de la excepcion)
    condicion_a = year % 4 == 0 and year % 100 != 0
    condicion_b = year % 400 == 0

    if condicion_a or condicion_b:
        print(f"{year}: es bisiesto")
    else:
        print(f"{year}: no es bisiesto")

bisiesto(2024)   # es bisiesto
bisiesto(1900)   # no es bisiesto (div por 100, no por 400)
bisiesto(2000)   # es bisiesto (div por 400)
bisiesto(2025)   # no es bisiesto