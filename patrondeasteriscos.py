def dibujar_triangulo(altura, invertido=False):
    # generamos la secuencia de filas segun la orientacion
    filas = range(altura, 0, -1) if invertido else range(1, altura + 1)

    for ancho in filas:
        print("* " * ancho)   # asterisco con espacio para que se vea mejor

print("-- normal --")
dibujar_triangulo(4)
# *
# * *
# * * *
# * * * *

print("-- invertido --")
dibujar_triangulo(4, invertido=True)
# * * * *
# * * *
# * *
# *