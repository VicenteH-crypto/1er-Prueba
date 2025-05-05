
# Ejercicio de la empresa "Certifica"

print('Bienvenido a Certifika, para su ingreso necesitamos saber su ultima calificación')

nombre_alumno = input('Ingresa su nombre: ')

nota = float(input('Ingresa la nota: '))

if nota >= 6.0:
    descuento = 20
    print('¡Felicidades! Obtienes un descuento del 20% por tu excelente desempeño.')
elif nota >= 5.0:
    descuento = 5
    print('¡Bien hecho! Recibes un descuento del 5%.')
elif nota >= 4.0:
    descuento = 10
    print('¡Buen trabajo! Obtienes un 10% de descuento.')
else:
    descuento = 0
    print('No cumple ningun requisito, Le invito seguir esforzandose o7')