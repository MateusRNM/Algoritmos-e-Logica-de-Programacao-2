def recursive_sum(list, i):
    if i == len(list):
        return 0
    return list[i] + recursive_sum(list, i+1)

def main():
    lista = [1, 3, 5, 8, 9, 10]
    print(recursive_sum(lista, 0))
main()