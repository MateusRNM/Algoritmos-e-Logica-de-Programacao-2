import json

clientes = None

try:
    with open("lista_arquivos/clientes.txt", "r") as clientes_file:
        clientes = json.load(clientes_file)
except:
    clientes = []

print("Cadastrar cliente:")
nome = input("Digite o nome: ")
endereco = input("Digite o endereço: ")
telefone = input("Digite o telefone: ")
clientes.append({
    "Cod_Cli": len(clientes),
    "Nome": nome,
    "Endereco": endereco,
    "Fone": telefone
})
print("Cliente cadastrado!")

with open("lista_arquivos/clientes.txt", "w") as clientes_file:
    clientes_file.write(json.dumps(clientes))