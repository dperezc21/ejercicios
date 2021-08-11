from collections import Counter
x = int(input())
lista_tallas = input().split(" ")
n_clientes = int(input())

d = Counter(lista_tallas)
total = 0

for i in range(n_clientes):
    n = input().split(" ")
    talla = n[0]
    precio = int(n[1])
    if talla in d and d[talla] > 0:
        total += precio
        d[talla] -= 1
        
print(total)  
