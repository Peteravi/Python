#Funciones son bloques con codigos reutilizables
#parametros son variables con la que podemos introducir datos en las funciones
 #argumentos son los datos que se encuentran en los parametros

 #Argumentos posicionales=van por orden de posicion en la declaracion de los parametros.
 #Argumentos de clave = van en cualquier orden 

 #FUNCION 
def saludar ():
    nombre = input("INTRODUZACA SU NOMBRE \n")
    print(f"MUY BUENAS,{nombre}!")
saludar()

#FUNCION CON UN SOLO PARAMETRO

def saludar1(nombre):
    print(f"¡Muy buenas ,{nombre}!")
saludar1("peter")
saludar1("carlos")
saludar1("alisson")

#FUNCION CON MULTIPLES PARAMETROS
def saludar2(nombre,edad):
    print(f"¡Muy buenas,{nombre}!")
    print(f"usted tiene {edad}años.")
saludar2 ("PETER",23)

#para mostrar dato en consola print
#para utilizar valores que devuelvan una funcion se utiliza return

def suma (num1 , num2):
    return  num1 + num2
resultado= suma(10 , 50 )
print(resultado)


def color ():
    c = input("INTRODUCE UN COLOR \n")
    print (f"TU COLOR ES ,{c}!")
color()


  