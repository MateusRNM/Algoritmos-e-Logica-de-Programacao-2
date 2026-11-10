def contagem(n):
    print(n)
    if n > 1:
        contagem(n-1)

def main():
    n = 10
    contagem(n)
main()