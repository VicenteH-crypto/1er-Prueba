
 # Ejercicio de los productos fondas

# Función para solicitar cantidades
def solicitar_cantidad(producto):
    while True:
        try:
            cantidad = int(input(f"¿Cuántos {producto} desea?: "))
            if cantidad >= 0:
                return cantidad
            else:
                print("Se produjo un error al ingresar el número, intente nuevamente.")
        except ValueError:
            print("ERROR... el número debe ser entero válido")

# Precios de los productos
precio_empanada_pino = 2000
precio_empanada_queso = 1500
precio_choripan = 2500
precio_terremoto = 1000

# Solicitar cantidades al usuario
cantidad_empanada_pino = solicitar_cantidad("empanadas de pino")
cantidad_empanada_queso = solicitar_cantidad("empanadas de queso")
cantidad_choripan = solicitar_cantidad('choripanes')
cantidad_terremoto = solicitar_cantidad('terremotos')

# Calcular el total sin descuento
total = (
    cantidad_empanada_pino * precio_empanada_pino +
    cantidad_empanada_queso * precio_empanada_queso +
    cantidad_choripan * precio_choripan +
    cantidad_terremoto * precio_terremoto
)

# Aplicar descuentos según el total
if total > 20000:
    total *= 0.6  # 0.4 de descuento
    print("¡Enhorabuena! Has recibido un 40% de descuento.")
elif total > 10000:
    total *= 0.75  # 0.25 de descuento
    print("¡Enhorabuena! Has recibido un 25% de descuento.")
elif total > 0:
    print("¡Gracias por comprar aqui!")

# Mostrar el total a pagar
print(f"Total a pagar con descuento: ${total:.2f}")