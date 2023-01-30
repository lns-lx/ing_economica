def VAN(tasa,flujos):
  VA=0
  for j in range(len(flujos)):
    VA+=flujos[j]/(1+tasa)**j
  return VA

def TIR(flujos):
  ka=-.5 
  kc=10 
  inf=VAN(ka,flujos) 
  sup=VAN(kc,flujos) 
  if inf>=0 and sup<0:
    error=abs(inf-sup)
    while error>=1e-10:
      kb=(ka+kc)/2
      #print(kb)
      med=VAN(kb,flujos)
      if med<=0:
        kc=kb
      elif med>0:
        ka=kb
      inf=VAN(ka,flujos)
      sup=VAN(kc,flujos)
      error=inf-sup
    return kb
  else:
    return "sin TIR"

def Menu_TIR():
    while True:
        print("\n1. Calcular TIR")
        print("2. Regresar al menu principal\n")
        opcion = int(input("Ingrese una opcion: "))
        if opcion == 1:
            num_periods = int(input("Ingrese el número de flujos de caja: "))
            misFlujos2 = []
            for i in range(num_periods):
                misFlujos2.append(float(input("Ingrese el flujo de caja para el período {}: ".format(i+1))))
            print()
            print('TIR=',str(round(TIR(misFlujos2)*100,2))+'%')  
        elif opcion == 2:
            break
        else:
            print("Opcion no valida")

if __name__ == "__main__":
    Menu_TIR()
