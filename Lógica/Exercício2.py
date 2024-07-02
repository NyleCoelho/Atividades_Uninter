print('Bem-vindos à loja de marmitas da Barbara Bianca!')  # Mensagem de boas-vindas com nome completo




total_pedido = 0 # Acumulador do valor total do pedido

while True:
    # Coletando do usuário o sabor escolhido
    while True: # Loop para garantir que o usuário entre com um sabor válido
        sabor = input('Entre com o sabor desejado (BA ou FF): ')
        if sabor not in ['BA', 'FF']: 
            print("Sabor inválido. Tente novamente!")
            continue
        break
    
    while True: # Loop para garantir que o usuário entre com um tamanho válido
        tamanho = input('Entre com o tamanho desejado (P, M ou G): ')
        if tamanho not in ['P', 'M', 'G']: 
            print("Tamanho inválido. Tente novamente!")
            continue
        break
    
    valor_pedido = 0 # Variável para armazenar o valor do pedido atual

    # Utilizando modelo aninhado para cada uma das combinações de sabor e tamanho
    if sabor == 'BA': 
        if tamanho == 'P': 
            valor_pedido = 16.00
        elif tamanho == 'M': 
            valor_pedido = 18.00 
        elif tamanho == 'G': 
            valor_pedido = 22.00
        print(f"Você escolheu um Bife Acebolado tamanho {tamanho} no valor de R$ {valor_pedido:.2f}") 

    elif sabor == 'FF': 
        if tamanho == 'P': 
            valor_pedido = 15.00
        elif tamanho == 'M': 
            valor_pedido = 17.00
        elif tamanho == 'G': 
            valor_pedido = 21.00
        print(f"Você escolheu um Filé de Frango tamanho {tamanho} no valor de R$ {valor_pedido:.2f}") 

    total_pedido += valor_pedido # Acumula o valor do pedido ao total pedido 

    # Pergunta ao usuário se deseja adicionar mais alguma coisa ao pedido
    resposta = input('Deseja adicionar mais alguma coisa ao pedido? (S/N): ')
    if resposta.upper() != 'S':
        break

print(f"O valor total do seu pedido é: R$ {total_pedido:.2f}") # Exibe o valor total do pedido