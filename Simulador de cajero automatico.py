def cajero_automatico():
    cuenta     = {"saldo": 500.0, "retirado_hoy": 0.0}
    TOPE_DIARIO = 500.0

    while True:
        print("\n[1] Saldo  [2] Depositar  [3] Retirar  [4] Salir")
        op = input(">> ").strip()

        if op == "1":
            print(f"  Saldo disponible: ${cuenta['saldo']:,.2f}")

        elif op == "2":
            monto = float(input("  Cantidad a depositar: $"))
            if monto > 0:
                cuenta["saldo"] += monto
                print(f"  Deposito de ${monto:,.2f} registrado.")
            else:
                print("  El monto debe ser positivo.")

        elif op == "3":
            monto   = float(input("  Cantidad a retirar: $"))
            nuevo_retiro = cuenta["retirado_hoy"] + monto

            if monto <= 0:
                print("  El monto debe ser positivo.")
            elif monto > cuenta["saldo"]:
                print("  Saldo insuficiente.")
            elif nuevo_retiro > TOPE_DIARIO:
                margen = TOPE_DIARIO - cuenta["retirado_hoy"]
                print(f"  Limite diario: puedes retirar hasta ${margen:,.2f} mas hoy.")
            else:
                cuenta["saldo"]         -= monto
                cuenta["retirado_hoy"]  += monto
                print(f"  Retiro de ${monto:,.2f} completado.")

        elif op == "4":
            print("  Sesion cerrada.")
            break
        else:
            print("  Opcion no reconocida.")

cajero_automatico()