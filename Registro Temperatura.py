
import time

 # Ejercicio Registro de Temperatura

print('Buen dia o7')

while True:
    try:
        N_temperatura = int(input('Ingrese la temperatura actual: '))
        if N_temperatura >= -50 and N_temperatura <= 50:
            print('Temperatura registrada existosamente')
            break
        else:
            print('Error: temperatura fuera del rango, intente nuevamente...')
    except ValueError:
        print('ERROR... debe ingresar un número entero valido. Intente hasta que sea valido')

time.sleep(5)
print(f'La temperatura es de {N_temperatura}°c')
time.sleep(3)
print('Cierre del programa, !Hasta luego¡')