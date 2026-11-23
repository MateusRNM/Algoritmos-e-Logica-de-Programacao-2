import json

with open("lista_arquivos/clientes.txt", "w+") as clientes_file:
    clientes = json.loads(clientes_file.read() or "[]")
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
    clientes_file.write(json.dumps(clientes))
    print("Cliente cadastrado!")