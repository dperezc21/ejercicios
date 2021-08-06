def print_formatted(number):
    for num in range(1,number+1):
        
        print(num, octal(num), hexadecimal(num), binario(num))
       
        
def binario(num)->str:
    lista = [2**n for n in range(num) if 2**n <= num ]
    
    for i in reversed(lista):
        if i <= num:
            num = num-i
            lista[lista.index(i)] = 1
        else:
            lista[lista.index(i)] = 0
    
    binario = ''.join(reversed([str(num) for num in lista]))
    return binario

    
def octal(num)->str:
    lista = []
    while num > 0:
        division = num//8
        multiplicacion = division * 8
        resta = num - multiplicacion
        lista.insert(0,str(resta))
        num =+ division
    octal = ''.join(lista)
    return octal

    
def hexadecimal(num)->str:
    lista = []
    dic = {0:0, 1:1, 2:2, 3:3, 4:4, 5:5, 6:6, 7:7, 8:8, 9:9,
           10:"A", 11:"B", 12:"C", 13:"D", 14:"E", 15:"F"}
    while num > 0:
        division = num//16
        multiplicacion = division * 16
        resta = num - multiplicacion
        lista.insert(0,resta)
        num =+ division
    lista = [str(dic[n]) for n in lista]
    hexadecimal = ''.join(lista)
    return hexadecimal

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
