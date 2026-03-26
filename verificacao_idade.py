'''Exercício 2 – Classificação de Idade
 
Escreva um programa em Python que solicite ao usuário a entrada de uma idade (número inteiro).
O programa deve classificar a idade informada de acordo com as regras abaixo:
0 a 12 → "Criança"
13 a 17 → "Adolescente"
18 a 59 → "Adulto"
60 ou mais → "Idoso"
Idade negativa → "Idade inválida"
Requisitos:
Utilizar apenas if, elif e else.
Validar valores negativos.
Exemplo:
Digite a idade: 25
Adulto'''

idadeUsuario = int(input('Envie a sua idade para verificação: '))

if (idadeUsuario < 0):
    print('Idade inválida.')
elif (idadeUsuario < 12):
    print('Criança.')
elif (idadeUsuario < 17):
    print('Adolescente.')
elif (idadeUsuario < 59):
    print('Adulto.')
elif (idadeUsuario >= 60):
    print('Idoso.')