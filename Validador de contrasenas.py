def revisar_clave(clave):
    fallas = []   # acumulamos los requisitos que no se cumplen

    if len(clave) < 8:
        fallas.append("debe tener al menos 8 caracteres")

    if sum(1 for c in clave if c.isupper()) == 0:
        fallas.append("falta al menos una mayuscula")

    if sum(1 for c in clave if c.islower()) == 0:
        fallas.append("falta al menos una minuscula")

    if sum(1 for c in clave if c.isdigit()) == 0:
        fallas.append("falta al menos un digito")

    if not fallas:
        print(f'"{clave}" es valida')
    else:
        print(f'"{clave}" tiene problemas:')
        for f in fallas:
            print(f"  - {f}")

revisar_clave("abc")
revisar_clave("segura99")
revisar_clave("ClaveOk7")