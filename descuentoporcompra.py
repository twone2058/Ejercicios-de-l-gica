def precio_con_descuento(total):
    if total < 0:
        print("El precio no puede ser negativo.")
        return

    # determinamos el porcentaje segun el monto
    if   total > 100: pct = 0.10
    elif total > 50:  pct = 0.05
    else:             pct = 0.00

    ahorro = total * pct
    final  = total - ahorro

    print(f"Precio original : ${total:.2f}")
    print(f"Descuento ({int(pct*100)}%)  : -${ahorro:.2f}")
    print(f"Total a pagar   : ${final:.2f}")

precio_con_descuento(120)
print()
precio_con_descuento(65)
print()
precio_con_descuento(40)