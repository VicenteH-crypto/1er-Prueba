import random

# Avance dia hoy

print('Sea bienvenido a ¡encuentra el digito!')
print('Usted creara un rango, y tendra que adivinar un numero aleatorio')

N01 = int(input('Ingrese el primer digito: '))
N02 = int(input('Ingrese otro digito: '))

if N02 <= N01:
    print('Error... El numero debe ser MAYOR al anterior')
else:

    Numero = random.randint(N01, N02)

for Intento in range(1, 4): # 3 intentos
    while True:
        try:
            Adivinaste = int(input(f'Intento {Intento}: ingresa un numero ramdon: '))
            break
        except ValueError:
            print('Ingresa un numero entero: ')

if Adivinaste == Intento:
          print(f'¡Adivinaste! El numero era {Numero}')
          breakpoint()
else:
    if Intento < 3: # Si aún quedan intentos
        if Adivinaste < Numero:
            print('El numero es mayor')
        else:
            print('El numero es menor')
    else: # Si se acabaron los intentos
        print(f'¡PERDISTE! el numero era {Numero}')