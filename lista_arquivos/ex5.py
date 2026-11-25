import json

clientes = None

try:
    with open("lista_arquivos/clientes.txt", "r") as clientes_file:
        clientes = json.load(clientes_file)
except:
    clientes = []

cod = int(input("Digite o código do cliente a ser alterado: "))
idx = -1

for i in range(len(clientes)):
    if clientes[i]["Cod_Cli"] == cod:
        idx = i
        break

if idx == -1:
    print("Cliente não existe!")
else:
    clientes[idx]["Nome"] = input(f"Digite o nome (Valor atual: {clientes[idx]["Nome"]}): ")
    clientes[idx]["Endereco"] = input(f"Digite o endereço (Valor atual: {clientes[idx]["Endereco"]}): ")
    clientes[idx]["Fone"] = input(f"Digite o telefone (Valor atual: {clientes[idx]["Fone"]}): ")

    with open("lista_arquivos/clientes.txt", "w") as clientes_file:
        clientes_file.write(json.dumps(clientes))