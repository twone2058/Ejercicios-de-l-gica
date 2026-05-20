def verificar_paridad(n):
    # el resto de dividir entre 2 indica si es par o impar
    # esto funciona igual con negativos: -6 % 2 == 0, asi que es par
    resto = n % 2
    if resto == 0:
        return f"{n} es par"
    return f"{n} es impar"

print(verificar_paridad(8))    # 8 es par
print(verificar_paridad(13))   # 13 es impar
print(verificar_paridad(0))    # 0 es par
print(verificar_paridad(-5))   # -5 es impar