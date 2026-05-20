def contar_caracteres(frase):
    VOCALES = "aeiouaeiou"   # incluimos con y sin tilde por si acaso
    conteo  = {"vocales": 0, "consonantes": 0, "espacios": 0}

    for char in frase.lower():
        if char == " ":
            conteo["espacios"] += 1
        elif char in VOCALES:
            conteo["vocales"] += 1
        elif char.isalpha():
            conteo["consonantes"] += 1
        # puntuacion, numeros y otros: ignorados

    print(f'Texto: "{frase}"')
    for tipo, cantidad in conteo.items():
        print(f"  {tipo:12}: {cantidad}")

contar_caracteres("Ingenieria de software")
contar_caracteres("Python 3.x, es genial!")