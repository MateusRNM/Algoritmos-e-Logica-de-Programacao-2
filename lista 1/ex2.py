def deslocar(a, n):
    res = a[:]
    for i in range(len(a)):
        res[(i+n)%len(a)] = a[i]
    return res

lista = [20, 5, 6, 7, 8, 9, 1]
print(deslocar(lista, 50))