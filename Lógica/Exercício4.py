#Questão 4 - Barbara Bianca Campos Coelho - RU 4821162

# Mensagem de boas vindas e nome completo
print("Bem vindos a empresa da Barbara Bianca!")

lista_funcionarios = [] # Lista vazia para armazenar os funcionários
id_global = 4821162 # ID global para os funcionários

def cadastrarFuncionario(id, nome, salario, setor): # Função para cadastrar funcionário
    nome = input("Digite o nome do funcionário: ").strip().title() # Nome do funcionário
    salario = float(input("Digite o salário do funcionário: ")) # Salário do funcionário
    setor = input("Digite o setor do funcionário: ").strip().title() # Setor do funcionário

    funcionario = {
        "ID": id, 
        "Nome": nome, 
        "Salário": salario, 
        "Setor": setor} # Dicionário com os dados do funcionário
    
    lista_funcionarios.append(funcionario.copy()) # Adiciona o dicionário à lista de funcionários
    print("Funcionário cadastrado com sucesso!") 

def consultar_funcionarios(): # Função para consultar os funcionários cadastrados
    while True:
        print("1- Consultar todos os funcionários")
        print("2- Consultar por id")
        print("3- Consultar por setor")
        print("4- Retornar ao menu principal")
        
        try: # Tratamento de exceção para entrada inválida
            opcoes = int(input("Digite qual opção deseja: "))
        except ValueError:
            print("Opção inválida! Digite um número de 1 a 4.")
            continue

        if opcoes == 1: # Consulta todos os funcionários
            for funcionario in lista_funcionarios:
                print(f"ID: {funcionario['ID']} - Nome: {funcionario['Nome']} - Salário: R$ {funcionario['Salário']} - Setor: {funcionario['Setor']}")
        
        elif opcoes == 2: # Consulta por ID
            id = int(input("Digite o ID do funcionário: "))
            for funcionario in lista_funcionarios:
                if id == funcionario["ID"]:
                    print(f"ID: {funcionario['ID']} - Nome: {funcionario['Nome']} - Salário: R$ {funcionario['Salário']} - Setor: {funcionario['Setor']}")
        
        elif opcoes == 3: # Consulta por setor
            setor = input("Digite o setor do funcionário: ").strip().title()
            for funcionario in lista_funcionarios:
                if setor == funcionario["Setor"]:
                    print(f"ID: {funcionario['ID']} - Nome: {funcionario['Nome']} - Salário: R$ {funcionario['Salário']} - Setor: {funcionario['Setor']}")
        
        elif opcoes == 4:
            break  # Sai do loop e retorna ao menu principal
        
        else: 
            print("Opção inválida! Digite um número de 1 a 4.")
    
def remover_funcionario(): # Função para remover funcionário
    id = int(input("Digite o ID do funcionário que deseja remover: "))
    for funcionario in lista_funcionarios:

        if id == funcionario["ID"]: # Remove o funcionário da lista
            lista_funcionarios.remove(funcionario)
            print("Funcionário removido com sucesso!")

        elif id != funcionario["ID"]: # Mensagem de erro caso o ID não seja encontrado
            print("ID não foi encontrado! Tente novamente.")
                  
# Código principal

print("MENU PRINCIPAL------------")
print("1 - Cadastrar funcionário")
print("2 - Consultar funcionários")
print("3 - Remover funcionário")
print("4 - Encerrar programa")

opcao_menu = int(input("Digite a opção desejada: ")) # Menu principal

if opcao_menu == 1: # Cadastrar funcionário
    id_global += 1
    cadastrarFuncionario(id_global, "", 0, "")
elif opcao_menu == 2:
    consultar_funcionarios() # Consultar funcionários
elif opcao_menu == 3:
    remover_funcionario() # Remover funcionário
elif opcao_menu == 4:
    print("Programa encerrado!") # Encerrar programa
else:
    print("Opção inválida! Tente novamente.")


                 
