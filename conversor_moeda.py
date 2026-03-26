'''1. Conversor de Moedas
Enunciado: Crie um programa que receba um valor em Reais (R$) e a cotação atual do Dólar. O programa deve exibir quanto esse valor representa em Dólares (US$).
Entrada: Valor em reais e cotação do dólar.
Processamento: dolar = reais / cotacao.
Saída: Valor convertido.'''

# Recebimento de valor por input/Atribuindo valor a variavel

valorReal = float(input('Insira o valor em Reais (R$) para conversão em Dólar ($)'))
cotacaoDolar = 5.25

#Conversao

valorDolar = valorReal * cotacaoDolar

print('-' * 30)
print('Conversão Real (R$) para Dólar ($)')
print(f'R${valorReal} --> ${valorDolar}')
print(f'Cotação do Dólar: {cotacaoDolar}')
print('-' * 30)