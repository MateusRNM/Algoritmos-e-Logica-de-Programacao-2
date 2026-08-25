def controlar_qualidade(pesos, peso_min, peso_max):
    aprovados = []
    descartados = []
    for peso in pesos:
        if peso >= peso_min and peso <= peso_max:
            aprovados.append(peso)
        else:
            descartados.append(peso)
    return (aprovados, descartados, len(descartados)/len(pesos))

pesos = [100, 50, 60, 200, 80]
peso_min = float(input("Digite o peso mínimo: "))
peso_max = float(input("Digite o peso máximo: "))
print(controlar_qualidade(pesos, peso_min, peso_max))