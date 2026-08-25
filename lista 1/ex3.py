def concatenar(a, b):
    res = []
    if len(a) > len(b):
        a, b = [b, a]
    for i in range(len(a)):
        res.append(a[i])
        res.append(b[i])
    for i in range(len(a), len(b)):
        res.append(b[i])
    return res

print(concatenar([2, 5, 6, 7, 1], [4, 3, 2]))