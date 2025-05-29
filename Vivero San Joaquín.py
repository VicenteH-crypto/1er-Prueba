
 # Pedimos los datos
nombre = input('Hola, ingrese su nombre: ').upper()
edad = input('Ahora, indique la edad: ')
print('Bienvenido al Vivero de San Joaquín', nombre)

while True:
    confirmacion = input('¿Desea llevarse alguna flor? (Si/No): ')
    if confirmacion.lower() == 'si':
        print('Elija la flor')

        # Opciones
        flores = [
            "Rosas blancas, Precio: $2000",
            "Matta, Precio: $2000",
            "La Orquídea, Precio: $3000",
            "El Copihue, Precio: $10000",
            "Rosas Rojas, Precio: $7000",
            "Girasol, Precio: $2500",
            "Lirio, Precio: $3500",
            "Margaritas, Precio: $1500",
            "Tulipanes, Precio: $4000",
            "Claveles, Precio: $2200"
        ]

        for i, flor in enumerate(flores, start=1):
            print(f"{i}. {flor}")

        while True:
            try:
                numero_flor = int(input('¿Cuál flor desea llevar (número): '))
                if 1 <= numero_flor <= 10:
                    print('Usted se llevará:', flores[numero_flor - 1])
                    break
                else:
                    print('Por favor, elija un número válido entre 1 y 10.')
            except ValueError:
                print('Solo NÚMEROS ENTEROS, intenta nuevamente...')

        # Almacenar la elección en el archivo
        with open("inventario_vivero.txt", "a") as archivo:
            archivo.write(f"{nombre} eligio: {flores[numero_flor - 1]}\n")

        while True:
            respuesta = input("¿Quieres continuar? ('Si' para continuar, 'No' para salir): ")
            if respuesta.lower() == 'si':
                print("Siga comprando...")
                break  # Sal del bucle interno para volver a preguntar por flores
            else:
                print("Programa terminado...")
                break  # Sal del bucle externo

    else:
        print('Fin del programa... Gracias por su tiempo.')
        break