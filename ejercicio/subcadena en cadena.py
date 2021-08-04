def count_substring(string, sub_string):
    len_subcadena = len(sub_string)
    len_cadena = len(string)
    cont = 0
    for i in range(0,len_cadena+1):
        
        if string.find(sub_string,i,i+len_subcadena) != -1:
            cont += 1
        
    return cont
