def potencia(a, b):
    if b == 1:
        return a
    elif b == 0:
        return 1
    return a * potencia(a, b-1)

def main():
    a = 3
    b = 4
    print(potencia(a, b))
main()