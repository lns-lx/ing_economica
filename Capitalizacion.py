def Anual(n):
    return n

def Semestral(n):
    return n/2

def Cuatrimestral(n):
    return n/4

def Trimestral(n):
    return n/4

def Bimestral(n):
    return n/6

def Mensual(n):
    return n/12

def Quincenal(n):
    return n/24

def Menu_conversor():
    while True:
        print('\n--- Tipo de capitalizacion ---')
        print('1. Anual')
        print('2. Semestral')
        print('3. Trimestral')
        print('4. Bimestral')
        print('5. Mensual')
        print('6. Quincenal')
        print('7. Regresar al menu anterior\n')
        opcion = int(input('Ingrese opcion: '))
        n = float(input("Ingrese el valor a convertir: "))
        if opcion == 1:
            result = Anual(n)
        elif opcion == 2:
            result = Semestral(n)
        elif opcion == 3:
            result = Trimestral(n)
        elif opcion == 4:
            result = Bimestral(n)
        elif opcion == 5:
            result = Mensual(n)
        elif opcion == 6:
            result = Quincenal(n)
        elif opcion == 7:
            break
        else:
            print('Opcion no valida')
        print("Resultado:", result)

if __name__ == "__main__":
    Menu_conversor()
