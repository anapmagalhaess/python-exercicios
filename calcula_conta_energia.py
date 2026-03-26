'''
Cálculo de Conta de Energia 2026
 
Escreva um programa para calcular o valor de uma conta de energia elétrica de
um consumidor com base no consumo de kWh. O programa deve receber o consumo de energia e
calcular o valor a pagar. Ao final, deve imprimir a conta detalhada (consumo, tarifa
aplicada, valor total a pagar...)
 
 
Regras de Negócio:
 
Consumo < 150 kWh: R$ 0,75 por kWh.
 
Consumo entre 150 e 500 kWh: R$ 0,95 por kWh.
 
Consumo acima de 500 kWh: R$ 1,20 por kWh.
 
Taxa Mínima (Disponibilidade): R$ 45,00 (se o cálculo do consumo for inferior a
este valor, o consumidor paga o mínimo).
'''

 # receber valor pelo input
consumo = int(input('Qual foi o consumo de energia elétrica em kWh?'))

# condicionais para definir tarifa conforme consumo de kWh
if consumo < 150:
    tarifa = 0.75
elif consumo <=500:
    tarifa = 0.95
else:
    tarifa = 1.20

#calculo da tarifa por consumo, com a tarifa aplicada
valorFinal = consumo * tarifa

#exibicao da conta
print(' -- Conta de Energia Elétrica --')
print(f'Consumo em kWh: {consumo}')
print(f'Tarifa: {tarifa}')

#Verificando se o valor final é menor que a Taxa Mínima
if valorFinal <= 45:
    print(f'Consumo inferior ao valor mínimo, será cobrada a taxa mínima de R$45')
else:
    print(f'Valor total a pagar: {valorFinal}')