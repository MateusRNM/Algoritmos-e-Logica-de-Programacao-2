def merge_listas(a, b):
    res = []
    i = 0
    j = 0
    while i < len(a) or j < len(b):
        if i < len(a) and j < len(b):
            if a[i] < b[j]:
                res.append(a[i])
                i += 1
            else:
                res.append(b[j])
                j += 1
        elif i < len(a):
            res.append(a[i])
            i += 1
        else:
            res.append(b[j])
            j += 1
    return res

print(merge_listas([1, 2, 3, 4, 5], [3, 6, 7]))