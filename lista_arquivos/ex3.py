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

print("Cadastrar recebimento:")
valor = float(input("Digite o valor do recebimento: "))
data_emissao = input("Digite a data da emissão do documento: ")
data_vencimento = input("Digite a data do vencimento do documento: ")
cod_cli = int(input("Digite o código do cliente: "))
cliente_existe = False

for cliente in clientes:
    if cliente["Cod_Cli"] == cod_cli:
        cliente_existe = True
        break

if cliente_existe:
    recebimentos.append({
        "Num_doc": len(recebimentos),
        "Valor_doc": valor,
        "Data_Emissao": data_emissao,
        "Data_Vencimento": data_vencimento,
        "Cod_Cli": cod_cli
    })
    print("Recebimento cadastrado!")
    with open("lista_arquivos/recebimentos.txt", "w") as recebimentos_file:
        recebimentos_file.write(json.dumps(recebimentos))
else:
    print("O cliente não está cadastrado!")