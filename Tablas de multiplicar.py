def tabla_de(numero):
    print(f"  Tabla del {numero}")
    print("  " + "-" * 18)
    for multiplicador in range(1, 11):
        resultado = numero * multiplicador
        # :2d alinea el numero en 2 caracteres para que la tabla quede recta
        print(f"  {numero} x {multiplicador:2d} = {resultado:3d}")

def todas(desde=1, hasta=10):
    # permite imprimir un rango personalizado, por defecto del 1 al 10
    for n in range(desde, hasta + 1):
        tabla_de(n)
        print()

tabla_de(9)
# o para todas:
# todas()