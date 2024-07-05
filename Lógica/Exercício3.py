#Questão 3 - Barbara Bianca Campos Coelho - RU 4821162

print('Bem-vindo(a) a fábrica de camisetas de Barbara Bianca!\n') #Mensagem de boas vindas com nome completo
print('--------------PREÇOS DAS CAMISETAS--------------') 

def precos_camisetas(): #dados das camisetas
    camisetas = [
        ("Camiseta Manga Curta Simples     (MCS)", 1.80),
        ("Camiseta Manga Longa Simples     (MLS)", 2.10),
        ("Camiseta Manga Curta Com Estampa (MCE)", 2.90),
        ("Camiseta Manga Longa Com Estampa (MLE)", 3.20)
    ]

    for descricao, valor in camisetas: # Apresenta os valores de cada opção de camiseta
        print(f"{descricao} - R$ {valor:.2f}")

precos_camisetas() # Chama a função para apresentar os valores das camisetas

# Função para escolher o modelo de camiseta
def escolha_modelo():
    while True:
        global modelo # Variável global para ser usada no codigo principal
        modelo = input("\nDigite o modelo desejado: ").strip().upper()
        if modelo == "MCS":
            return 1.80
        elif modelo == "MLS":
            return 2.10
        elif modelo == "MCE":
            return 2.90
        elif modelo == "MLE":
            return 3.20
        else:
            print("Modelo inválido! Tente novamente.")

# Função para escolher o número de camisetas
def num_camisetas():
    while True:
        try: # Tratamento de exceção para entrada inválida
            num = int(input("Digite o número de camisetas desejado: "))
            if num <= 0:
                print("Número de camisetas deve ser maior que zero! Tente novamente.")
            elif num > 20000:
                print("Não aceitamos tantas camisetas de uma só vez. Tente novamente.")

            else:
                if num >= 20 and num < 200: # Desconto de 5%
                    return num * 0.95
                elif num >= 200 and num < 2000: # Desconto de 7%
                    return num * 0.93
                elif num >= 2000 and num <= 20000: # Desconto de 12%
                    return num * 0.88
                else:
                    return num # Retorna o número de camisetas sem desconto
                    
        except ValueError: # Exceção para valor inválido
            print("Entrada inválida! Digite um número inteiro.\n")

def precos_fretes(): # dados dos modelos de frete
    tipos_frete = [
        ("1- Transportadora......................", 100.00),
        ("2- Sedex...............................", 200.00),
        ("0- Retirar na Fábrica..................", 0.00)
    ]

    print("\n------------SERVIÇO ADICIONAL DE FRETE------------")

    for descricao, valor in tipos_frete: # Apresenta os valores de cada opção de frete  
        print(f"{descricao} - R$ {valor:.2f}")

# Função para escolher o frete
def frete():
    while True:
        precos_fretes() # Chama a função para apresentar os valores dos fretes
        opcao_frete = input("\nDigite o serviço adicional de frete (1/2/0)): ").strip()
        if opcao_frete == "1":
            return 100
        elif opcao_frete == "2":
            return 200
        elif opcao_frete == "0":
            return 0
        else:
            print("Opção de frete inválida! Tente novamente.")

# Código principal

valor_modelo = escolha_modelo()  
numero_camisetas = num_camisetas()  
valor_frete = frete() 

# Cálculo do total a pagar
total = (valor_modelo * numero_camisetas) + valor_frete  

print(f"O valor total a pagar é: R$ {total:.2f}")  # Saída do resultado final