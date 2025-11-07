print("Digite los siguientes datos:")
#Le pedimos al usuario que nos brinde la siguiente informacion
nombre = input("Escribe el nombre de tu producto :")
#Creamos un while true para generar un bucle para que cuando el usuario nos ponga un dato
#incorrecto se repita hasta que nos ponga un numero mayor a 0 o numeros 
while True:
#ponemos un bloque de try-except para que cuando nos digite un caracter que no sea de tipo int
#el programa no crashee ni de error si no que resuelva el problema
    try:
#Creamos la variable de precio para que el usuario nos ingrese el nombre del producto
        precio = float(input("Ingrese el precio de su producto: "))
#Creamos un codincional con la variable y que sea menor o igual a cero para que cuando 
#el usuario nos digite un valor igual o negativo el sistema le tire error y le mande un mensaje
        if precio <= 0:
            print("El precio debe ser un número mayor a 0, intente de nuevo.")
#Asignamos un continue para que el bucle continue hasta que el usuario ingrese un valor correcto
            continue
        print("El precio se ha registrado")
#Cuando el usuario ponga un digito o valor se rompa el blucle con un break
        break
#ponemos el except para cubir el bloque try para cuando el usuario ingrese un valor no valido
    except ValueError:
        print("Ingrese una cantidad válida, solo números!!")

#hacemos el mismo procedimiento con la variable cantidad
while True:
    try:
        cantidad = int(input("Ingrese la cantidad: "))
        if cantidad <= 0:
            print("La cantidad debe ser un número mayor a 0, intente de nuevo!!")
            continue
        print("La cantidad se ha registrado")
        break
    except ValueError:
        print("Ingrese una cantidad válida, solo números!!")

#Creamos una nueva variable que incluya el precio por la cantidad
costo_total = precio * cantidad
#Ahora hacemos un print con los datos que el usuario nos brindo y el total que le tocaria pagar
print(f"Producto: {nombre}", f"Precio: {precio}", f"Cantidad: {cantidad}", f"Total: {costo_total}")

#El programa tiene la funcion de pedirle los datos sobre un producto al usuario para al que final haga una operacion matematica (multiplicacion) de cuanta plata se necesitaria para llevar la cantidad productos deseada por el usuario

