colores = ["rojo", "azul", "verde","amarillo"]
#saltar bucle 
print("LISTADO DE COLORES")

for color in colores:
    if color =="azul" or color =="verde":
        print("se ha saltado un valor")
        continue
    print(f"-color {color}.")

#romper el bucle

colores = ["rojo", "azul", "verde","amarillo"]
print("LISTADO DE COLORES")
for color in colores:    
    if color == "azul":
        print("se ha roto el bucle ")
        break
    print(f"-color{color}.")


#While

#i=1
#while i < 5:
    #print(f"elvalor del bucle es:{i}")
    #i+=1 #incremento del while
    #i-=1 #decremento del while


#-----------------------------------

for i in range (7,15):
    print(f"el valor del bucle es: {i}.")



    j= 7
    while i <=14:
         print(f"elvalor del bucle es:{i}.")
         i+=1
         