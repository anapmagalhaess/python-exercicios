'''Exercício 5 – Desconto em Compra (Teste Composto)
Escreva um programa em Python que solicite ao usuário o valor total de uma compra e a forma de pagamento:
1 → Dinheiro
2 → Cartão
O programa deve utilizar testes compostos (condições com operadores lógicos && e ||) com if, else if e else para aplicar as seguintes regras de desconto:
Se o valor da compra for maior ou igual a 100 e o pagamento for em dinheiro → aplicar 10% de desconto
Se o valor da compra for maior ou igual a 100 e o pagamento for em cartão → aplicar 5% de desconto
Se o valor da compra for menor que 100 → não há desconto
O programa deve exibir o valor final da compra e uma mensagem indicando se houve desconto.
Requisitos:
Utilizar apenas if, elif e else ou match-case.
Utilizar operadores lógicos (&&, ||) para formar condições compostas.
Validar a forma de pagamento (apenas 1 ou 2).
Exemplo de execução:
Digite o valor da compra: 150
Forma de pagamento (1-Dinheiro / 2-Cartão): 1
Desconto aplicado!
Valor final: 135.0'''

print("=" * 30)
valorTotal = float(input('Digite o valor total da compra: '))
formaPagamento = int(input('\n1 → Dinheiro\n2 → Cartão\n\nDigite a forma de pagamento: '))

if (formaPagamento != 1 and formaPagamento != 2):
    print('\nForma de pagamento inválida.')
else:
    if (formaPagamento == 1 and valorTotal >= 100):
        valorTotal = valorTotal - (valorTotal * 0.10)
        print(f'Valor final com desconto aplicado R${valorTotal}')
    elif (formaPagamento == 2 and valorTotal >= 100):
        valorTotal = valorTotal - (valorTotal * 0.05)
        print(f'Valor final com desconto aplicado R${valorTotal}')
    else:
        print(f'Valor final sem desconto aplicado\nValor final = R${valorTotal}')

print("=" * 30)