#Mensgaem de boas vindas apresentando nome completo
print('Bem-vindo(a) a loja da Barbara Bianca!')

#Coletando do usuário o valor do pedido e a quantidade de parcelas 
valorDoPedido = float(input('Entre com o valor do pedido: '))
quantidadeParcelas = int(input('Entre com a quantidade de parcelas: '))

#Implementando a lógica da taxa de juros de acordo com os dados fornecidos
if quantidadeParcelas >= 4 and quantidadeParcelas < 6:
    juros = 0.04 #4%
elif quantidadeParcelas >= 6 and quantidadeParcelas < 9:
    juros = 0.08 #8%
elif quantidadeParcelas >= 9 and quantidadeParcelas < 13:
    juros = 0.16 #16%
elif quantidadeParcelas >= 13:
    juros = 0.32 #32%
else:
    juros = 0.0

#Implementado o cálculo do valor das parcelas e o valor total parcelado 
valorDaParcela = valorDoPedido * (1 + juros) / quantidadeParcelas
valorTotalParcelado = valorDaParcela * quantidadeParcelas

#Apresentando o valor das parcelas e o total parcelado de acordo com a taxa de juros
print(f'Valor dos juros aplicados é de: {juros * 100:.0f}%')
print(f'O valor das parcelas é de R$ {valorDaParcela:.2f}')
print(f'O valor total parcelado é de R$ {valorTotalParcelado:.2f}')
print('Código por Barbara Bianca Campos Coelho')