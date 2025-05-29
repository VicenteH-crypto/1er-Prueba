
import time

 # Ejercicio Áreas de los Triángulos

 # Damos la bienvenida
print('Hola, hoy día calculare el área de varios triángulos')

 # Pedimos las medidas
Altura_triangulo = float(input('Medida Altura: '))
print(Altura_triangulo,'cm')

Base_triangulo = float(input('Medida Base: '))
print(Base_triangulo,'cm')

 # Opciones
print('1.- Equilatero')
print('2.- Isósceles')
print('3.- Escaleno')
print('4.- Acutángulo')
print('5.- Rectángulo')
print('6.- Obtusángulo')

while True:
    try:
        Opcion = int(input('Elegi una opción (Numero): '))
        if Opcion > 0 and Opcion <= 6:
            break
        else:
            print('Error, el numero fuera del rango')
    except ValueError:
        print('ERROR... El número debe ser un entero, intenta otra vez')

match Opcion:
    case 1:
        print('Eligio el triángulo Equilatero')
    case 2:
        print('Eligio el triángulo Isósceles')
    case 3:
        print('Eligio el triángulo Escaleno')
    case 4:
        print('Eligio el triángulo Acutángulo')
    case 5:
        print('Eligio el triángulo Rectángulo')
    case 6:
        print('Eligio el triángulo Obstusángulo')

print('Ahora realizare el calculo')
time.sleep(5)
print(f'({Altura_triangulo} x {Base_triangulo}) / 2 =')
time.sleep(2)

 # Realiza el calculo (Área)
Area = (Base_triangulo * Altura_triangulo) / 2
print(Area, 'cm²')
time.sleep(2)

print('El área del triángulo que usted eligio es:', Area, 'cm²')

