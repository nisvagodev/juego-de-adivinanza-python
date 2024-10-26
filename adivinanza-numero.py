import random


def juegoAdivinanza():
    # Generando un número aleatorio del 1 al 100
    numero_secreto = random.randint(1, 100)
    intentos = 0
    adivinado = False

    print("¡Bienvenido a adivinanza de número!")
    print("Debes adivinar un número entre el 1 al 100")
    print("¡Intenta adivinarlo!")

    while not adivinado:
        # Solicitando el número
        adivinanza = input("Introduce un número del 1 al 100: ")

        # Verificar que la entrada sea un número
        if adivinanza.isdigit():
            adivinanza = int(adivinanza)
            intentos += 1

            if adivinanza < numero_secreto:
                print(f"El número secreto es mayor a {adivinanza}")
            elif adivinanza > numero_secreto:
                print(f"El número secreto es menor a {adivinanza}")
            else:
                print(f"¡Felicidades, has ganado! {
                      adivinanza} es el número secreto y lo has logrado en {intentos} intentos")
        else:
            print("Por favor, introduce un número válido del 1 al 100")


juegoAdivinanza()
