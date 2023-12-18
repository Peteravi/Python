#funcionan por claves y valores
#elementos del diccionario 
#nombre_diccionario={
# clave:valor,
#clave : valor,
# }
microsoft= {
"word":"procesador de texto",
"excel":"programa de plantilla",
"power" :  "programa para presentacion"
}

print(microsoft)
print(microsoft[ "word"])




diccionario ={
    1:"valor1",
    2: "valor2",
    3:"valor3",

}
print( diccionario )


#añadir elementos al diccionario 
microsoft= {
"word":"procesador de texto",
"excel":"programa de plantilla",
"power" :  "programa para presentacion",
}

microsoft[ "outlook"] = "administrador de correos"

print(microsoft[ "outlook"])



#diccionario vacio 
vacio ={}
print(vacio)


#vaciar el contenido del diccionario

inventario = {
    1:"espada",
    2:"escudo",
    3:"regenerador de escudo",
}
inventario={}
print=("inventario")


#bucles
microsoft= {
"word":"procesador de texto",
"excel":"programa de plantilla",
"power" :  "programa para presentacion",
}

for programa in microsoft:
    print(f"-{programa}")

#sets son listas desordenadas sin indice de posicion

animales_set={"perro","gato","iguana"}
print(animales_set)

