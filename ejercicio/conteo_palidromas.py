palabra = "holacomo"
    lista = []
    cont = 0

    def palindroma(string):
        lista = list(string)
        l = []
        for i in lista:
            l.insert(0,i)
        cadena = ''.join(l)

        if cadena == string:
            return True
        else:
            return False


    for i in range(len(palabra)+1):
        
        for j in range(len(palabra)+1):
            if palabra[i:j] != "":
                if palindroma( palabra[i:j]):
                    cont +=1
                    lista.append(palabra[i:j])

