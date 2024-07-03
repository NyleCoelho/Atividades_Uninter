#Questão 3 - Barbara Bianca Campos Coelho - RU 4821162

print('Bem-vindo(a) a fábrica de camisetas de Barbara Bianca!') #Mensagem de boas vindas com nome completo
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
        modelo = input("Digite o modelo desejado: ").strip().upper()
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
        try:
            num = int(input("Digite o número de camisetas desejado: "))
            if num <= 0:
                print("Número de camisetas deve ser maior que zero. Tente novamente.")
            elif num > 20000:
                print("Não aceitamos tantas camisetas de uma só vez. Tente novamente.")
            else:
                if num < 20:
                    return num
                elif num < 200:
                    return num * 0.95
                elif num < 2000:
                    return num * 0.93
                else:
                    return num * 0.88
        except ValueError:
            print("Entrada inválida! Digite um número inteiro.")

# Função para escolher o frete
def frete():
    while True:
        opcao_frete = input("Digite o serviço adicional de frete (1 para Transportadora, 2 para Sedex, 0 para Retirar na Fábrica): ").strip()
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