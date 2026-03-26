print('--- Calculo da Média ---')

#Entrada de dados
n1 = float(input('Nota 1: '))
n2 = float (input('Nota 2 : '))
n3 = float (input('Nota 3: '))

#Processamento
media = (n1+n2+n3)/3

#Saida de dados
print('Media: ', media)

#Condicionais

if media >= 6:
    print('Aprovado')
else:
    print('Reprovado')

