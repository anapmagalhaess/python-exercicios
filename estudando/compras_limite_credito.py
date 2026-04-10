'''Exercício 1 - estrutura de repetição
Simulação de Compras com Limite de Crédito
 
Desenvolva um programa que gerencie o limite de crédito de um cliente durante uma sessão de compras. O programa deve simular o funcionamento de uma carteira digital ou cartão pré-pago.
 
Requisitos:
Entrada de Crédito: O programa deve iniciar solicitando ao usuário o valor do Crédito Disponível (valor real).
Processamento de Itens: Utilize uma estrutura de repetição para receber o preço de cada item sucessivamente.
Lógica de Abatimento: A cada item inserido, o programa deve verificar se o saldo atual é suficiente para cobri-lo:
Se o saldo for suficiente, o valor do item é subtraído do crédito e a compra continua.
Se o saldo for insuficiente, o programa deve informar que não há crédito para aquele item e encerrar a entrada de dados imediatamente.
Saída de Dados: Ao final, exiba:
O Valor Total acumulado da compra.
O Saldo Restante (crédito que sobrou).
 '''

credito_disponivel = float(input("Digite o valor do Crédito Disponível: "))
carrinho = 0

while True:
    valor_item = float(input("Digite o preço do item: "))
    if valor_item > credito_disponivel:
        print('Saldo insuficiente.')
        break
    else:
        credito_disponivel -= valor_item
        carrinho += valor_item

print('=' * 10)
print(f'Valor total da compra: {carrinho}')
print(f'Saldo restante: {credito_disponivel}')
print('=' * 10)