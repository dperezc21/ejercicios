caballos = ["Spirit","Troya","Pegazo","Imperiozo","Jumper","Babieca","Rocinante", "pegazo"]
caballos_pedro = {}
caballos_pablo = {}
resultado = ""


for caballo in caballos:

    victorias_ganadas = int(input("victorias de {}, a favor de pedro: ".format(caballo)))
    
    caballos_pedro[caballo[0]]=victorias_ganadas

print("")

for caballo in caballos:

    victorias_ganadas = int(input("victorias de {}, a favor de pablo: ".format(caballo)))
    
    caballos_pablo[caballo[0]]=victorias_ganadas

print(caballos_pedro)



for clave in caballos_pablo:
    if caballos_pablo[clave] == caballos_pedro[clave]:
        resultado += "z"
    elif caballos_pablo[clave] > caballos_pedro[clave]:
        resultado += "y"
    else:
        resultado += "x"


print(resultado)
