
prestamos_mas_15_dias = 0
prestamos_menos_15_dias = 0

 # Ejercicio de los libros
Nombre = input('Ingrese su nombre: ')
Nombre = Nombre.upper()

print('Bienvenido a la biblioteca', Nombre)

 # Confirmación (Si/No)
respuesta = input('Desea registrar libro (Si/No): ')
if respuesta == 'si'.lower():
    while True:
        try:
            Cantidad_libro = int(input('Ingrese la cantidad de libros a registrar: '))
            break
        except ValueError:
            print('Por favor, ingrese solo números enteros')

    for i in range(Cantidad_libro):
        print(f'\nRegistro del libro {i+1}:')
        nombre_libro = input('Ingrese nombre del libro: ')

        while True:
            try:
                Cantidad_ejemplares = int(input('¿Cantidad de ejemplares a prestar: '))
                break
            except ValueError:
                print('Por faver, solo ingrese número enteros')

        while True:
            try:
                dias_prestamos = int(input('Indique los días de prestamos: '))
                break
            except ValueError:
                print('ERROR... solo puede ingresar números ENTEROS, intenta nuevamente.')

        if dias_prestamos > 15:
            prestamos_mas_15_dias += 1
            tipo_prestamo = 'Préstamo por más de 15 días'
        else:
            prestamos_menos_15_dias += 1
            tipo_prestamo = 'Prestamo por menos de 15 días'

    print(f'Libro: {nombre_libro}')
    print(f'Cantidad a prestar: {Cantidad_ejemplares}')
    print(f'Tipo de préstamo: {tipo_prestamo}')

    print(f'\ntotal de libros prestados por más de 15 días: {prestamos_mas_15_dias}')
    print(f'\ntoatl de livros prestados por menos de 15 días: {prestamos_menos_15_dias}')

else:
    print('Fin del programa, adios')