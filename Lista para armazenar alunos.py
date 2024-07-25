# Lista para armazenar alunos
alunos = []

# Função para adicionar um aluno
def adicionar_aluno(nome, idade, nota):
    aluno = (nome, idade, nota)  # Criando uma tupla para o aluno
    alunos.append(aluno)  # Adicionando a tupla à lista de alunos
    print(f"Aluno {nome} adicionado com sucesso!")

# Função para remover um aluno pelo nome
def remover_aluno(nome):
    for aluno in alunos[:]:  # Faz uma cópia da lista para evitar erro de modificação durante iteração
        if aluno[0] == nome:
            alunos.remove(aluno)
            print(f"Aluno {nome} removido com sucesso!")
            return
    print(f"Aluno {nome} não encontrado!")

# Função para exibir a lista de alunos
def exibir_alunos():
    if not alunos:
        print("Nenhum aluno cadastrado.")
    else:
        print("Lista de Alunos:")
        for aluno in alunos:
            print(f"Nome: {aluno[0]}, Idade: {aluno[1]}, Nota: {aluno[2]}")

# Menu de opções
def menu():
    while True:
        print("\nMenu de Opções:")
        print("1. Adicionar Aluno")
        print("2. Remover Aluno")
        print("3. Exibir Alunos")
        print("4. Sair")
        opcao = input("Escolha uma opção: ")
        if opcao == "1":
            nome = input("Digite o nome do aluno: ")
            idade = int(input("Digite a idade do aluno: "))
            nota = float(input("Digite a nota do aluno: "))
            adicionar_aluno(nome, idade, nota)
        elif opcao == "2":
            nome = input("Digite o nome do aluno a ser removido: ")
            remover_aluno(nome)
        elif opcao == "3":
            exibir_alunos()
        elif opcao == "4":
            print("Saindo do programa...")
            break
        else:
            print("Opção inválida. Tente novamente!")

menu()