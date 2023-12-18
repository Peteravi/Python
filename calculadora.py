import math
respuesta= input("1.Suma.\n 2.Resta\n 3.Multiplicacion \n 4.Division \n ")

if respuesta == "1" :
    print("HAS SELECCIONADO LA OPCION SUMA \n" )
    numero1=float(input("INGRESA EL PRIMER NUMERO:"))
    numero2=float(input("INGRESA EL SEGUNDO NUMERO:"))
    suma = numero1+numero2
    print("LA RESPUESTA ES:",suma)    
elif respuesta =="2":
    print ("HAS SELECCIONADO LA OPCION RESTA \n ")
    numero1=float(input("INGRESA EL PRIMER NUMERO:"))
    numero2=float(input("INGRESA EL SEGUNDO NUMERO:"))
    Resta = numero1-numero2
    print("LA RESPUESTA ES:",Resta)    
elif respuesta =="3":
    print ("HAS SELECCIONADO LA OPCION MULTIPLICACION \n ") 
    numero1=float(input("INGRESA EL PRIMER NUMERO:"))
    numero2=float(input("INGRESA EL SEGUNDO NUMERO:"))
    multiplicacion = numero1*numero2
    print("LA RESPUESTA ES:", multiplicacion) 
elif respuesta =="4":
    print ("HAS SELECCIONADO LA OPCION DIVISION ") 
    numero1=float(input("INGRESA EL PRIMER NUMERO:"))
    numero2=float(input("INGRESA EL SEGUNDO NUMERO:"))
    division = numero1/numero2
    print("LA RESPUESTA ES:", division) 

else:
    print("ALERTA! OPCION NO VALIDA")

