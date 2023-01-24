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
        print('3. Cuatrimestral')
        print('4. Cuatrimestral')
        print('5. Trimestral')
        print('6. Bimestral')
        print('7. Mensual')
        print('8. Quincenal')
        print('9. Regresar al menu anterior\n')
        opcion = int(input('Ingrese opcion: '))
        if opcion == 1:
            Anual()
        elif opcion == 2:
            Semestral()
        elif opcion == 3:
            Cuatrimestral()
        elif opcion == 4:
            Cuatrimestral()
        elif opcion == 5:
            Trimestral()
        elif opcion == 6:
            Bimestral()
        elif opcion == 7:
            Mensual()
        elif opcion == 8:
            Quincenal()
        elif opcion == 9:
            break
        else:
            print('Opcion no valida')

if __name__ == "__main__":
    Menu_conversor()


