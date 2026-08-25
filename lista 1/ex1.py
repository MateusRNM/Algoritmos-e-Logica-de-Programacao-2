def media_movel(a, k):
    soma = 0
    res = []
    for i in range(k):
        soma += a[i]
    res.append(soma/k)
    for i in range(k, len(a)):
        soma += a[i]
        soma -= a[i - k]
        res.append(soma/k)
    return res


lista = [20, 4, 5, 6 , 7 , 8, 9]
k = int(input())
print(media_movel(lista, k))