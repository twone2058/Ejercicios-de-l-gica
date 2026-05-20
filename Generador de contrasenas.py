import random, string

def nueva_clave(largo=10, usar_simbolos=True, usar_numeros=True, usar_mayus=True):
    # base: siempre incluimos minusculas
    fuente    = list(string.ascii_lowercase)
    garantia  = []   # al menos un caracter de cada tipo activado

    if usar_mayus:
        fuente   += list(string.ascii_uppercase)
        garantia.append(random.choice(string.ascii_uppercase))

    if usar_numeros:
        fuente   += list(string.digits)
        garantia.append(random.choice(string.digits))

    if usar_simbolos:
        fuente   += list(string.punctuation)
        garantia.append(random.choice(string.punctuation))

    # completamos hasta el largo pedido con caracteres aleatorios del pool