##muestra los nombre en orden alfabetico de los alumnos con la segunda calificacion mas baja
if __name__ == '__main__':
    puntajes = []
    numero_minimo = []
    for _ in range(int(input())):
        
        name = input()
        score = float(input())
        numero_minimo.append(score)
        
        puntajes.append([name,score])
    
    numero_minimo = float(min(numero_minimo))
    nombres = []
    
       

    for i in range(len(puntajes)):
        if numero_minimo < puntajes[i][1]:
            nombres.append(puntajes[i])
            
            if len(nombres) >  1:
                
                if nombres[len(nombres)-1][1] > nombres[len(nombres)-2][1]:
                    nombres.pop(len(nombres)-1)
                elif nombres[len(nombres)-1][1] < nombres[len(nombres)-2][1]:
                    nombres.pop(len(nombres)-2)
                    
    
    for i in sorted(nombres):
        print(i[0])
            
