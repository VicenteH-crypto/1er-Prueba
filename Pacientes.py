
 # Ejercicio Pacientes

print('Hola')
Nombre = input('Ingrese su nombre: ')
Nombre = Nombre.upper()

print('Sea bienvenido', Nombre,'A la clinica')

while True:
    try:
        cantidad = int(input('Ingrese el numero de personas registradas: '))
        print('Pacientes registrados', cantidad)
        break
    except ValueError:
        print('Debes ingresar numeros enteros, intenta nuevamente')

# Solicitamos los datos de cada pacientes

for i in range(cantidad):
    # Nombre
    while True:
        try:
            nombre = input(f'Ingrese el nombre del paciente {i+1}: ')
            print('Nombre:', nombre)
            break
        except ValueError:
            print('No puede ingresar números, intente nuevamente')

    while True:
        # Edad
        try:
            Edad = int(input(f'Ingrese la edad del paciente {i+1}: '))
            print('Edad:', Edad)
            break
        except ValueError:
            print('Solo números enteros, intenta nuevamente')

    while True:
        # R.U.T
        try:
            RUT = float(input(f'Ingrese el r.u.t del paciente {i+1}: '))
            print('r.u.t:', RUT)
            break
        except ValueError:
            print('El r.u.t ingresado no es valido, intenta nuevamente.')

    while True:
        # Sintomas presentes
        try:
            Sintomas = input(f'Ingrese el sintoma presente del paciente {i+1}: ')
            print('sintomas:', Sintomas)
            break
        except ValueError:
            print('El sintoma no existe, nuevamente intente')

    while True:
        # Tipo de vacuna
        try:
            Tipo_vacuna = input(f'Indique si el paciente algun tipo de vacuna {i+1}: ')
            print('tipo de sistoma:', Tipo_vacuna)
            break
        except ValueError:
            print('ERROR... solo su puede escribir')

print(f'Información contenida: '
                  f'{nombre} de {Edad}, '
      f'r.u.t: {RUT}, '
      f'Sintomas: {Sintomas}, Tipo de vacuna: {Tipo_vacuna}')
