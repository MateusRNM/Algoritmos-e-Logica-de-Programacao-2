import json

clientes = recebimentos = None

try:
    with open("lista_arquivos/clientes.txt", "r") as clientes_file:
        clientes = json.load(clientes_file)
except:
    clientes = []

try:
    with open("lista_arquivos/recebimentos.txt", "r") as recebimentos_file:
        recebimentos = json.load(recebimentos_file)
except:
    recebimentos = []

cod = int(input("Digite o código do cliente a ser excluído: "))
idx = -1

for i in range(len(clientes)):
    if clientes[i]["Cod_Cli"] == cod:
        idx = i
        break

if idx == -1:
    print("Cliente não existe!")
else:
    delete_count = 0
    for i in range(len(recebimentos)):
        if recebimentos[i-delete_count]["Cod_Cli"] == cod:
            del recebimentos[i-delete_count]
            delete_count += 1
    del clientes[idx]

    with open("lista_arquivos/clientes.txt", "w") as clientes_file:
        clientes_file.write(json.dumps(clientes))

    with open("lista_arquivos/recebimentos.txt", "w") as recebimentos_file:
        recebimentos_file.write(json.dumps(recebimentos))