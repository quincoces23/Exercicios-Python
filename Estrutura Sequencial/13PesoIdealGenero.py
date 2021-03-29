# Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo
# que calcule seu peso ideal, utilizando as seguintes fórmulas:
# Para homens: (72.7*h) - 58
# Para mulheres: (62.1*h) - 44.7

sexo = str(input('Qual é o seu sexo? M para Mulher e H para Homem: ').replace(' ', '').upper())
altura = float(input('Qual é a sua altura em metros? ').replace(' ', ''))
if sexo == 'M':
    print(f'Seu peso ideal é {(62.1*altura) - 44.7:.2f}.')
elif sexo == 'H':
    print(f'Seu peso ideal é {(72.7*altura) - 58:.2f}.')
else:
    print('Digite um valor valido: M/H')
