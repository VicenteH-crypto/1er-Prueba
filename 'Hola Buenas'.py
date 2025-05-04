
print('¡¡¡Hola buenas!!!')

print('1.- Opción')
print('2.- Opción')
print('3.- Opción')
print('4.- Opción')

Numero = int(input('Elige una opción del 1 al 4: '))

if Numero <=4 and Numero >=1:
    print('Numero valido')
else:
    print('Numero invalido... Ingrese otra vez')

if Numero == 1:
    print('Se ha ganado un saludo de parte de Messi :D')
elif Numero == 2:
    print('Se ha ganado un Good Bye :) ')
elif Numero == 3:
    print('Tendra que decirme su edad, o ingresar un edad cualquiera')
    Edad = int(input('Ingresela aqui: '))
    print('La edad:', Edad)

elif Numero == 4:
    print('Error de salida...')
else:
    print('Numero incorrecto... ')