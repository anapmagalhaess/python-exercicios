'''Exercício 4 – Rodízio de Veículos (São Paulo)
Escreva um programa em Python que solicite ao usuário o último dígito da placa de um veículo (um número inteiro de 0 a 9) e o dia da semana (também representado por um número de 1 a 5), considerando apenas dias úteis:
1 → Segunda-feira
2 → Terça-feira
3 → Quarta-feira
4 → Quinta-feira
5 → Sexta-feira
 
O programa deve utilizar if, elif e else para verificar se o veículo está impedido de circular naquele dia, de acordo com as regras do rodízio de veículos da cidade de São Paulo:
Segunda-feira (1): placas terminadas em 1 e 2
Terça-feira (2): placas terminadas em 3 e 4
Quarta-feira (3): placas terminadas em 5 e 6
Quinta-feira (4): placas terminadas em 7 e 8
Sexta-feira (5): placas terminadas em 9 e 0
O programa deve exibir uma das seguintes mensagens:
"Rodízio ativo: veículo não pode circular"
"Dia ou placa inválidos" (caso os valores informados estejam fora dos intervalos esperados)
Requisitos:
Utilizar  if, else if e else ou match-case.
Validar se o dia está entre 1 e 5.
Validar se o dígito da placa está entre 0 e 9.
Exemplo de execução:
Digite o último dígito da placa: 4
Digite o dia da semana (1 a 5): 2
Rodízio ativo: veículo não pode circular'''

print('=' * 30)
print('Rodízio de Veículos - São Paulo')
ultimoDigitoPlaca = int(input('Olá! Envie o último digito da placa do seu veículo: '))
diaDaSemana = int(input('Envie um número de acordo com o dia da semana de hoje.\n\n(1)Segunda\n(2)Terça\n(3)Quarta\n(4)Quinta\n(5)Sexta\n\nDigite aqui: '))

match (ultimoDigitoPlaca, diaDaSemana):
    case (1 | 2 , 1):
        print('Rodízio ativo: veículo não pode circular')
    case (3 | 4 , 2):
        print('Rodízio ativo: veículo não pode circular')
    case (5 | 6 , 3):
        print('Rodízio ativo: veículo não pode circular')
    case (7 | 8 , 4):
        print('Rodízio ativo: veículo não pode circular')
    case (9 | 0 , 5):
        print('Rodízio ativo: veículo não pode circular')
    case _:
        print('Dia ou placa inválidos')


"""if (diaDaSemana == 1):
    if (ultimoDigitoPlaca == 1 or ultimoDigitoPlaca == 2):
        print('Rodízio ativo: veículo não pode circular')
    elif(ultimoDigitoPlaca < 0 or ultimoDigitoPlaca > 9):
        print('Dia ou placa inválidos')
    else:
        print('Sem rodízio: veículo pode circular')
elif (diaDaSemana == 2):
    if (ultimoDigitoPlaca == 3 or ultimoDigitoPlaca == 4):
        print('Rodízio ativo: veículo não pode circular')
    elif(ultimoDigitoPlaca < 0 or ultimoDigitoPlaca > 9):
        print('Dia ou placa inválidos')
    else:
        print('Sem rodízio: veículo pode circular')
elif (diaDaSemana == 3):
    if (ultimoDigitoPlaca == 5 or ultimoDigitoPlaca == 6):
        print('Rodízio ativo: veículo não pode circular')
    elif(ultimoDigitoPlaca < 0 or ultimoDigitoPlaca > 9):
        print('Dia ou placa inválidos')
    else:
        print('Sem rodízio: veículo pode circular')
elif (diaDaSemana == 4):
    if (ultimoDigitoPlaca == 7 or ultimoDigitoPlaca == 8):
        print('Rodízio ativo: veículo não pode circular')
    elif(ultimoDigitoPlaca < 0 or ultimoDigitoPlaca > 9):
        print('Dia ou placa inválidos')
    else:
        print('Sem rodízio: veículo pode circular')
elif (diaDaSemana == 5):
    if (ultimoDigitoPlaca == 9 or ultimoDigitoPlaca == 0):
        print('Rodízio ativo: veículo não pode circular')
    elif(ultimoDigitoPlaca < 0 or ultimoDigitoPlaca > 9):
        print('Dia ou placa inválidos')
    else:
        print('Sem rodízio: veículo pode circular')"""