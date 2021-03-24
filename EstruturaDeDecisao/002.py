# Faça um Programa que peça um valor e mostre na tela se o valor é positivo ou negativo.
valor = float(input('Me diga um número real: ').replace(' ', ''))
if valor > 0:
    print(f'O {valor} é positivo')
elif valor < 0:
    print(f'O {valor} é negativo.')
else:
    print(f'O {valor} é neutro.')