'''4. Somador de Números (While)
Objetivo: Entender como acumular valores e parar um loop.

Crie uma variável soma = 0.

Peça para o usuário digitar um número.

Enquanto o número digitado for diferente de 0:

Some esse número à variável soma.

Peça o próximo número dentro do loop.

Ao final (quando ele digitar 0), imprima o total da soma.'''

soma = 0

while True:
    n1 = int(input("Digite um valor: "))
    soma += n1
    if n1 == 0:
        print(f"O resultado da soma é {soma}")
        break