def punto_equilibrio():
    print("\n--- Punto de Equilibrio ---")
    costo_fijo = float(input("Ingrese el costo fijo: "))
    costo_variable = float(input("Ingrese el costo variable: "))
    precio_venta = float(input("Ingrese el precio de venta: "))
    punto_equilibrio = costo_fijo / (precio_venta - costo_variable)
    resultado = round(punto_equilibrio, 2)
    print("\n\033[1;32mEl punto de equilibrio es: ", resultado, "\033[0;m")
    Menu_punto_equilibrio()

def Menu_punto_equilibrio():
    while True:
        print("\n--- Punto de Equilibrio ---")
        print("1. Calcular punto de equilibrio")
        print("2. Regresar al menu principal\n")
        opcion = int(input("Ingrese una opcion: "))
        if opcion == 1:
            punto_equilibrio()
        elif opcion == 2:
            break
        else:
            print("Opcion no valida")

if __name__ == "__main__":
    Menu_punto_equilibrio()