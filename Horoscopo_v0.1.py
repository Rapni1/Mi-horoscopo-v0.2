#Horoscopo Python V0.2 - Mi primer proyecto en python.
#Autor: Rapni
def obtener_signo(mes, dia):
    datos_signos = [
        (1, 19, "Capricornio"), (2, 18, "Acuario"), (3, 20, "Piscis"),
        (4, 19, "Aries"), (5, 20, "Tauro"), (6, 20, "Géminis"),
        (7, 22, "Cáncer"), (8, 22, "Leo"), (9, 22, "Virgo"),
        (10, 22, "Libra"), (11, 21, "Escorpio"), (12, 21, "Sagitario")
    ]

    if dia <= datos_signos[mes-1][1]:
        return datos_signos[mes-1][2]
    else:
        return datos_signos[mes % 12][2]

print("--- PROYECTO HORÓSCOPO PYTHON V0.2 ---")

while True:
    try:
        dia_nac = int(input("\nIngrese su día de nacimiento (1-31): "))
        mes_nac = int(input("Ingrese su mes de nacimiento (1-12): "))

        
        if 1 <= mes_nac <= 12 and 1 <= dia_nac <= 31:
            resultado = obtener_signo(mes_nac, dia_nac)
            print(f"✨ Tu signo es: {resultado} ✨")
            
            
            continuar = input("\n¿Quieres consultar otro? (s/n): ").lower()
            if continuar != 's':
                print("¡Adiós! 👋")
                break 
        else:
            print("❌ Error: Fecha fuera de rango (Mes 1-12, Día 1-31).")

    except ValueError:
        print("❌ Error: Por favor, ingresa solo números enteros.")
