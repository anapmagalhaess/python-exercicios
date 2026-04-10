'''Exercício - Sistema de Caixa de Supermercado
Exercício: Sistema de Caixa de Supermercado
 
Desenvolva um programa em Python que simule o fechamento de um caixa. O sistema deve ler o preço de cada item (valor real) de forma contínua.
Para encerrar a entrada de dados, o usuário deve digitar o valor sentinela -1.
Ao final, o programa deve exibir o valor total acumulado da compra, formatado como moeda (duas casas decimais).
Atenção: O valor sentinela não deve ser somado ao total.
 '''

valor_acumulado = 0

while True:
    item = float(input("Digite o preço do item (ou digite -1 para encerrar): "))
    if item == -1:
        break
    else:
        valor_acumulado += item

print(f"Valor acumulado da compra: {valor_acumulado:.2f}")

    
