'''2. Cálculo de Salário com Comissão
Enunciado: Uma empresa paga um salário fixo de R$ 2.000,00 mais uma comissão de 15% sobre o total de vendas efetuadas pelo vendedor. Receba o total de vendas do mês e exiba o salário final.
Entrada: Total de vendas (double).
Processamento: total = 2000 + (vendas * 0.15).
Saída: Salário final formatado.
=========================='''


#Recebimento de valor por input
vendas = float(input('Total de vendas efetuadas pelo vendedor? '))

#Calculo do salario com Comissao
salarioFinal = 2000 + (vendas * 0.15)

#Saida
print('=' * 30)
print('Salário com Comissão')
print(f'R${salarioFinal:.2f}')
print('=' * 30)

