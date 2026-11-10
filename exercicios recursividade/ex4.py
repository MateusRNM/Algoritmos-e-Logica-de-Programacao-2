def euclides(a, b):
    if b == 0:
        return a
    return euclides(b, a%b)

def main():
    a = 1345
    b = 125
    print(euclides(a, b))
main()