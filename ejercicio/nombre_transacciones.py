#lista de nombre de transacciones con la cantidad
def groupTransactions(transactions):
    new_dic = {}
    lista = []
    for t in transactions:
        
        if t in new_dic:
            new_dic[t] = new_dic[t] +1
        else:
            new_dic[t] = 1
    for l in new_dic:
        cadena = l +" "+str(new_dic[l])
        lista.append(cadena)

    return sorted(lista)
