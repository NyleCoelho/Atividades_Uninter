# Mensagem de boas vindas e nome completo
print("\nBem vindos a empresa da Barbara Bianca!")

lista_funcionarios = [] # Lista vazia para armazenar os funcionários
id_global = 4821162 # ID global para os funcionários

def cadastrarFuncionario(id, nome, salario, setor): # Função para cadastrar funcionário
    print(f"\nO ID do funcionário é: {id}")
    nome = input("Digite o nome do funcionário: ").strip().title() # Nome do funcionário
    salario = float(input("Digite o salário do funcionário: R$ ")) # Salário do funcionário
    setor = input("Digite o setor do funcionário: ").strip().title() # Setor do funcionário

    funcionario = {
        "ID": id, 
        "Nome": nome, 
        "Salário": salario, 
        "Setor": setor} # Dicionário com os dados do funcionário
    
    lista_funcionarios.append(funcionario.copy()) # Adiciona o dicionário à lista de funcionários
    print("\nFuncionário cadastrado com sucesso!\n")

def consultar_funcionarios(): # Função para consultar os funcionários cadastrados
    while True:
        print("\nMENU DE CONSULTAS-------------------")
        print("1- Consultar todos os funcionários")
        print("2- Consultar por id")
        print("3- Consultar por setor")
        print("4- Retornar ao menu principal\n")
        
        try: # Tratamento de exceção para entrada inválida
            opcoes = int(input("Digite qual opção deseja: "))
        except ValueError:
            print("\nOpção inválida! Digite um número de 1 a 4.\n")
            continue

        if opcoes == 1: # Consulta todos os funcionários
            if not lista_funcionarios:
                print("\nNão há funcionários cadastrados.\n")
            else:
                for funcionario in lista_funcionarios:
                    print(f"\nID: {funcionario['ID']} \n Nome: {funcionario['Nome']} \n Salário: R$ {funcionario['Salário']} \n Setor: {funcionario['Setor']}\n")

        elif opcoes == 2: # Consulta por ID
            id = int(input("Digite o ID do funcionário: "))
            encontrado = False

            for funcionario in lista_funcionarios:
                if id == funcionario["ID"]:
                    print(f"\nID: {funcionario['ID']} \n Nome: {funcionario['Nome']} \n Salário: R$ {funcionario['Salário']} \n Setor: {funcionario['Setor']}\n")
                    encontrado = True
                    break
            if not encontrado:

                print("\nID não foi encontrado! Tente novamente.\n")
        
        elif opcoes == 3: # Consulta por setor
            setor = input("Digite o setor do funcionário: ").strip().title()
            encontrado = False

            for funcionario in lista_funcionarios:
                if setor == funcionario["Setor"]:
                    print(f"\nID: {funcionario['ID']} \n Nome: {funcionario['Nome']} \n Salário: R$ {funcionario['Salário']} \n Setor: {funcionario['Setor']}\n")
                    encontrado = True

            if not encontrado:
                print("\nSetor não foi encontrado! Tente novamente.\n")

        elif opcoes == 4:
            break  # Sai do loop e retorna ao menu principal
        
        else: 
            print("\nOpção inválida! Digite um número de 1 a 4.\n")

def remover_funcionario(): # Função para remover funcionário
    id = int(input("Digite o ID do funcionário que deseja remover: "))
    encontrado = False

    for funcionario in lista_funcionarios:
        if id == funcionario["ID"]: # Remove o funcionário da lista
            lista_funcionarios.remove(funcionario)
            print("\nFuncionário removido com sucesso!\n")
            encontrado = True
            break

    if not encontrado: # Mensagem de erro caso o ID não seja encontrado
        print("\nID não foi encontrado! Tente novamente.\n")

# Código principal
while True:
    print("\nMENU PRINCIPAL------------")
    print("1 - Cadastrar funcionário")
    print("2 - Consultar funcionário(s)")
    print("3 - Remover funcionário")
    print("4 - Encerrar programa\n")

    try:
        opcao_menu = int(input("Digite a opção desejada: "))
    except ValueError:
        print("\nOpção inválida! Digite um número de 1 a 4.\n")
        continue

    if opcao_menu == 1:
        id_global += 1
        cadastrarFuncionario(id_global, "", 0, "")
    elif opcao_menu == 2:
        consultar_funcionarios()
    elif opcao_menu == 3:
        remover_funcionario()
    elif opcao_menu == 4:
        print("\nPrograma encerrado!\n")
        break
    else:
        print("\nOpção inválida! Digite um número de 1 a 4.\n")