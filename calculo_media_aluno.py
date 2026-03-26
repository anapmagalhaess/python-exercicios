'''Exercício 3 – Cálculo de Média e Situação do Aluno
Crie um programa que receba duas notas (valores decimais) de um aluno e calcule a média.
Com base na média, o programa deve exibir:
Média maior ou igual a 7 → "Aprovado"
Média entre 5 e 6.9 → "Recuperação"
Média menor que 5 → "Reprovado"
Requisitos:
Utilizar apenas if, elif e else.
Calcular a média corretamente.
Considerar que as notas variam de 0 a 10 (não é obrigatório validar).
Exemplo:
Digite a primeira nota: 6
Digite a segunda nota: 8
Aprovado'''

nota1 = float(input('Olá, envie a primeira nota para cálculo da média: '))
nota2 = float(input('Agora envie a segunda nota: '))

mediaFinal = (nota1 + nota2)/2

if (mediaFinal < 5):
    print(f'Nota: {mediaFinal}, Reprovado.')
elif (mediaFinal < 6.9):
    print(f'Nota {mediaFinal}, Recuperação,')
elif (mediaFinal <= 10):
    print(f'Nota {mediaFinal}, Aprovado.')
