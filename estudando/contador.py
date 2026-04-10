'''O Contador Inteligente (Fluxograma Mental)
Objetivo: Praticar lógica de incremento e limite.

Peça um número de início e um número de fim.

Use um while para imprimir todos os números desse intervalo, um por um.

Desafio: Se o número de início for maior que o de fim, mostre uma mensagem de erro em vez de tentar contar.'''

inicio = int(input("De o valor de início: "))
fim = int(input("Dê o valor de fim: "))

if inicio > fim:
    print("Valor de início maior que o de fim")
else:
    while inicio <= fim:
        print(inicio)
        inicio += 1
