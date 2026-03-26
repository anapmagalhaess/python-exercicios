''' 4. Média Ponderada
Enunciado: Receba três notas de um aluno. Calcule a média ponderada considerando que a primeira nota tem peso 2, a segunda peso 3 e a terceira peso 5.
Processamento: media = (n1*2 + n2*3 + n3*5) / 10. '''

#Recebimento de valores por input.
n1 = float(input('Envie a primeira nota: '))
n2 = float(input('Envie a segunda nota: '))
n3 = float(input('Envie a terceira nota: '))

#Calculo da media.
media = (n1*2 + n2*3 + n3*5 )/10

#Saida.
print('=' * 30)
print(f'Media final: {media:.2f}')
print('=' * 30)

