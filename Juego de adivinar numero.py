import random

def adivina():
    objetivo  = random.randint(1, 100)
    MAX       = 10
    turno     = 1

    print(f"Tengo un numero entre 1 y 100. Tienes {MAX} intentos.")

    while turno <= MAX:
        restantes = MAX - turno + 1
        intento   = int(input(f"Turno {turno}/{MAX} ({restantes} restantes): "))

        if intento == objetivo:
            print(f"Correcto! Lo lograste en el turno {turno}.")
            return
        
        pista = "sube" if intento < objetivo else "baja"
        print(f"  {intento} no es. El numero {pista}.")
        turno += 1

    print(f"Se acabaron los intentos. El numero era {objetivo}.")

adivina()