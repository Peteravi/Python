edad= int (input("POR FAVOR INTRODUCE TU EDAD :"))
respuesta = None

if edad >=18 :
    print("Es mayor de edad, puede comprar alcohol .¿CUAL DESEA? Introduzca un numero de opcion." )
    respuesta= input("1.ron.\n 2.whisky\n 3.Pedrito \n ")


if respuesta == "1" :
    print("Ha elegido comprar ron Gracias por su compra")
elif respuesta =="2":
    print ("Ha elegido comprar Whisky Gracias por su compra") 
elif respuesta =="3":
    print ("Ha elegido comprar pedrito Gracias por su compra") 

else:
    print("ALERTA! ERES MENOR DE EDAD , NO INGIERAS ALCOHOL , QUIERETE")
