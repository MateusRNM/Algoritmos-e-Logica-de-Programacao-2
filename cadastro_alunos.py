alunos = []

def add_aluno():
    nome = input("Informe o nome do aluno: ")
    notas = []
    for i in range(1, 5):
        notas.append(float(input(f"Digite a {i} nota do aluno: ")))
    alunos.append({ "nome": nome, "notas": notas })
    print(f"Aluno {nome} adicionado com sucesso!")

def remove_aluno():
    if len(alunos) == 0:
        print("Sem alunos cadastrados!")
        return
    
    print("Escolha o aluno para ser removido:")
    idx = -1
    while True:
        for i in range(len(alunos)):
            print(f"{i+1} - {alunos[i]["nome"]}")
        idx = int(input("Digite a opção: ")) - 1

        if idx < 0 or idx >= len(alunos):
            print("Opção inválida!\n")
        else:
            break
    print(f"Aluno {alunos[idx]["nome"]} removido com sucesso!")
    del alunos[idx]

def calcular_media():
    if len(alunos) == 0:
            print("Sem alunos cadastrados!")
            return
    
    print("Médias:")
    for i in range(len(alunos)):
        aluno = alunos[i]
        media = sum(aluno["notas"])/len(aluno["notas"])
        print(f"{i+1} - {aluno["nome"]}: {media}")

def indentificar_maior_media():
    if len(alunos) == 0:
            print("Sem alunos cadastrados!")
            return
    
    maior_media = -1
    nome = ""
    for i in range(len(alunos)):
        aluno = alunos[i]
        media = sum(aluno["notas"])/len(aluno["notas"])
        if media > maior_media:
            maior_media = media
            nome = aluno["nome"]
    print(f"O aluno com a maior média é: {nome} - Média: {maior_media}")

def exibir_alunos():
    if len(alunos) == 0:
        print("Sem alunos cadastrados!")
        return

    for i in range(len(alunos)):
        aluno = alunos[i]
        media = 0
        print(f"{i+1} - {aluno["nome"]}")
        for j in range(len(aluno["notas"])):
            print(f"Nota {j+1}: {aluno["notas"][j]}")
            media += aluno["notas"][j]
        media /= len(aluno["notas"])
        print(f"Média: {media}\n")
        

def main():
    while True:
        print("Sistema de cadastro de alunos:")
        print("0 - Adicionar um novo aluno")
        print("1 - Remover um aluno")
        print("2 - Calcular a média de todos os alunos")
        print("3 - Identificar o aluno com a maior média")
        print("4 - Exibir todos os alunos")
        print("5 - Sair do sistema")
        op = int(input("Digite a opção: "))
        print()
        if op == 0:
            add_aluno()
        elif op == 1:
            remove_aluno()
        elif op == 2:
            calcular_media()
        elif op == 3:
            indentificar_maior_media()
        elif op == 4:
            exibir_alunos()
        elif op == 5:
            break
        else:
            print("Opção inválida!\n")
        print()
main()