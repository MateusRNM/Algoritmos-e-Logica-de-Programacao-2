
def fatorial(n):
    res = 1
    for i in range(n, 1, -1):
        res *= i
    return res

def fatorial_recursivo(n):
    if n <= 1:
        return 1
    return n * fatorial_recursivo(n-1)

n = int(input("Digite o número para calcular o fatorial: "))
print(fatorial(n))