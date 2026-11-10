def recursive_sum(list, l, r):
    if l == r:
        return list[l]
    mid = l+(r-l)//2
    return recursive_sum(list, l, mid) + recursive_sum(list, mid+1, r)

def main():
    lista = [1, 3, 5, 8, 9, 10]
    print(recursive_sum(lista, 0, len(lista)-1))
main()