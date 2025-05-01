#Ejercicio compra de Python

print('Hola, bienvenido a mi pequeño negocio!')

print('1.- Manzanas')
print('2.- Plátanos')
print('3.- Leche')
print('4.- Almendras')
print('5.- paquete de avena')

productos = [ ]
for i in range(2):
    productos.append(input(f"Añade el producto #{i+1}: "))

print('Tus productos son: ', productos)

while True:
    mod = int(input('¿Cuál de los productos quiere cambiar? (Eliga el numero): ')) - 1
    if 0 <= mod < len(productos):
        productos[mod] = input('Nuevo nombre del producto: ')
        break
    else:
        print('Numero invalido, Elegi un numero entre 1 y', len(productos))

while True:
    elim = int(input('¿Cual es el productos que quieres eliminar? (Eliga el  numero): ')) - 1
    if 0 <= elim < len(productos):
        elim_productos = productos.pop(elim)
        print('Producto eliminado:', elim_productos)
        break
    else:
        print('Numero invalido, elige otro numero de entre 1 y', len(productos))

print('Productos finales: ', productos)
print('Tenga buen dia :)')