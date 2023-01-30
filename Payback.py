import functools as ft
import math as mt
def Payback_contable():
    inv = float(input('Ingrese el monto de la inversión inicial: '))
    flujo_e = [float(x) for x in input('Ingrese los flujos de efectivo para cada año separados por espacios: ').split(' ')]
    acumulativo = []
    i = 0
    while i < len(flujo_e):
        acumulativo.append(sum(flujo_e[:i+1]))
        if acumulativo[i] >= inv:
            year = i + (inv - sum(flujo_e[:i])) / flujo_e[i]
            break
        i += 1
    b= print("El número de años que se tardará en recuperar la inversión inicial es {} años".format(round(year, 2)))
    return b

def Payback_descontado():
    inv=float(input('Ingrese el monto de la inversión inicial:'))
    flujo_e=[float(x) for x in input('Ingrese los flujos de efectivo para cada año separados por espacios: ').split(' ')]
    desc_flujo=[x for x in range(0,len(flujo_e))]
    desc_tasa=float(input("Introducir tasa de descuento:"))
    dif=[]
    acumulativo=[]
    i=0
    while i<len(flujo_e):
        desc_flujo[i]=flujo_e[i]/pow(1+(desc_tasa/100),i+1)
        dif.append(inv-ft.reduce(lambda x,y:x+y,desc_flujo))
        acumulativo.append(ft.reduce(lambda x,y:x+y,desc_flujo))
        i+=1
        dif=list(map(lambda x:x>=0,dif))
        def minimum(lst):
            i=lst.index(min(lst))
            return i+1
        year=minimum(dif)+(inv-acumulativo[minimum(dif)-1])/desc_flujo[minimum(dif)-1]
    a=print("El número de años que se tardará en recuperar la inversión inicial es {} años".format(round(year,2)))
    return a 

def Menu_payback():
    while True:
        print("\n1. Calcular Payback Contable")
        print("2. Calcular Payback Descontado")
        print("3. Regresar al menu menu anterior\n")
        opcion = int(input("Ingrese una opcion: "))
        if opcion == 1:
            Payback_contable()
        elif opcion == 2:
            Payback_descontado()
        elif opcion == 3:
            break
        else:
            print("Opcion no valida")

if __name__ == "__main__":
    Menu_payback()
