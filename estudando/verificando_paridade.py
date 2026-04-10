'''Exercício: Verificador de Par ou Ímpar
Objetivo: Usar o operador % para identificar a paridade de um número.

Peça ao usuário para digitar um número inteiro.

Calcule o resto da divisão desse número por 2.

Regra: * Se o resto for igual a 0, imprima: "O número é PAR".

Se o resto for igual a 1, imprima: "O número é ÍMPAR".'''

n1 = int(input("Digite um número inteiro: "))

match n1 % 2:
    case 0:
        print("O número é par")
    case 1:
        print("O número é impar")
