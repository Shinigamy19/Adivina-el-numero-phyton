import random

def adivina_el_numero():
    numero_secreto = random.randint(0, 100)
    intentos = 5
    minimo = 0
    maximo = 100

    print("¡Bienvenido al juego de Adivina el Número!")
    print(f"Tienes {intentos} intentos para adivinar el número entre {minimo} y {maximo}.")

    while intentos > 0:
        entrada = input(f"Ingrese un número entre {minimo} y {maximo}: ")

        if not entrada.isdigit():
            print("Por favor, ingresa un número válido.")
            continue

        adivinanza = int(entrada)

        if adivinanza < minimo or adivinanza > maximo:
            print("Tu número está fuera del rango permitido.")
            continue

        if adivinanza == numero_secreto:
            print("¡Felicidades! Adivinaste el número.")
            break
        elif adivinanza < numero_secreto:
            print("El número secreto es MAYOR.")
            minimo = max(minimo, adivinanza + 1)
        else:
            print("El número secreto es MENOR.")
            maximo = min(maximo, adivinanza - 1)

        intentos -= 1
        print(f"Te quedan {intentos} intento(s).\n")

    else:
        print(f"¡Perdiste! El número era {numero_secreto}.")

# Ejecutar el juego
adivina_el_numero()
input("\nPresiona Enter para salir...")