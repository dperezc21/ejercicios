import textwrap

def merge_the_tools(string, k):
    lista = textwrap.fill(string,k)
    lista = lista.split('\n')
    
    for i in lista:
        print(function(i))
    
    
def function(lista):
    
    string = lista[0]
    for i in range(1,len(lista)):
        letra = lista[i-1]
        if letra != lista[i] and lista[i] not in string:
            string += lista[i]
        
    return string
