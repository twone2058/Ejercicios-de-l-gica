import calendar

def ver_mes(mes, anio):
    # validamos antes de llamar a la libreria
    if not (1 <= mes <= 12) or anio < 1:
        print(f"Fecha invalida: mes={mes}, anio={anio}")
        return

    # por defecto calendar muestra semanas de lun a dom
    calendar.setfirstweekday(0)   # 0 = lunes

    nombre_mes = calendar.month_name[mes]
    print(f"  {nombre_mes} {anio}")
    print("  Lu Ma Mi Ju Vi Sa Do")

    # monthcalendar devuelve una lista de semanas
    # cada semana es una lista de 7 dias (0 significa que el dia no pertenece al mes)
    for semana in calendar.monthcalendar(anio, mes):
        linea = ""
        for dia in semana:
            if dia == 0:
                linea += "   "         # espacio para dias fuera del mes
            else:
                linea += f"{dia:3d}"   # numero alineado en 3 caracteres
        print(f"  {linea}")

ver_mes(8, 2025)
print()
ver_mes(2, 2024)   # febrero en año bisiesto