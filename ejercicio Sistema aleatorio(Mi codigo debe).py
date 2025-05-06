from os import system

# Numero 1 (Inicio del limite)

system("cls")
Porcentaje = 0.1

print('Hola, defina un rango de numeros')

N01 = int(input('Ingrese el primer numero: '))
print('Primer numero:', N01)

if N01 > 0 and N01 <100:
    print('¡Correcto!')
else:
    print('Numero invalido....... Intente nuevamente.')
    system("cls")

# Numero 2 (Final del limite)

N02 = int(input('Ingrese otro numero mayor al anterior: '))

if N02 <= N01:
    print('Numero incorrecto...')
    system("cls")
else:
    print('Rangos definidos')

print('Ahora realizare el calculo')
Por1 = Porcentaje * N01
Por2 = Porcentaje * N02

print(Por1)
print(Por2)

Suma = Por1 + Por2
print('El resultado de la suma es:', Suma)