import random

def main():
    # Ingreso de datos del usuario
    while True:
        try:
            rango_min = int(input("Ingresa el primer número (mínimo): "))
            rango_max = int(input("Ingresa el segundo número (máximo): "))
            if rango_min < rango_max:
                break 
            
            else:
                print("El primer número debe ser menor que el segundo. Intenta nuevamente.")
        except ValueError:
            print("Por favor, ingresa números enteros válidos.")

    # Generación de un número aleatorio en el rango
    numero_aleatorio = random.randint(rango_min, rango_max)

    # Ajuste del número aleatorio: lo dividimos entre 4 y redondeamos al múltiplo de 4 más cercano
    numero_ajustado = round(numero_aleatorio / 4) * 4

    # Imprimir número ajustado (esto es para prueba, puedes eliminarlo después)
    print(f"(Para prueba, el número ajustado es: {numero_ajustado})")

    # Intentos del usuario
    intentos = 3
    for intento in range(1, intentos + 1):
        try:
            usuario_intento = int(input(f"Intento {intento}: Ingresa un número para adivinar: "))
            
            if usuario_intento == numero_ajustado:
                print("¡Felicitaciones, adivinaste al primer intento!")
                break
            elif intento == 1:
                print("¡Incorrecto! El número es mayor o menor.")
            elif intento == 2:
                if usuario_intento < numero_ajustado:
                    print("El número es mayor.")
                else:
                    print("El número es menor.")
            else:
                print(f"Game Over. El número era: {numero_ajustado}")
                break
        except ValueError:
            print("Por favor, ingresa un número entero válido.")

if __name__ == "__main__":
    main()


