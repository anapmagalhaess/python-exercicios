'''3. Cálculo de Área e Perímetro
Enunciado: Escreva um programa que leia a base e a altura de um retângulo e exiba sua área e seu perímetro.
Fórmulas: Area = base * altura | Perimetro = 2 * (base + altura).'''

# recebimento do valor por input

base = float(input('Insira a base do retângulo: '))
altura = float(input('Insira a altura do retângulo: '))

#calculo dos valores
area = base * altura
perimetro = 2 * (base + altura)

#saida

print('=' * 30)
print(f'Área do Retângulo: {area:.2f}')
print(f'Perimetro do Retângulo: {perimetro:.2f}')
print('=' * 30)

