def convertir_longitud(cantidad, modo):
    # factor de conversion: 1 metro equivale a 3.28084 pies
    FACTOR = 3.28084

    if modo == "m2ft":
        resultado = cantidad * FACTOR
        unidad_salida = "pies"
    elif modo == "ft2m":
        resultado = cantidad / FACTOR
        unidad_salida = "metros"
    else:
        print(f'Modo desconocido: "{modo}". Usa "m2ft" o "ft2m".')
        return

    print(f"{cantidad} -> {round(resultado, 4)} {unidad_salida}")

convertir_longitud(1.80, "m2ft")   # 1.8 -> 5.9055 pies
convertir_longitud(6, "ft2m")      # 6 -> 1.8288 metros
convertir_longitud(5, "km2m")      # modo desconocido