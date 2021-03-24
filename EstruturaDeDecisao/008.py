# Faça um programa que pergunte o preço de três produtos e informe qual produto
# você deve comprar, sabendo que a decisão é sempre pelo mais barato.

produto1 = float(input('Qual o valor do produto?').replace(' ', ''))
produto2 = float(input('Qual o valor do produto?').replace(' ', ''))
produto3 = float(input('Qual o valor do produto?').replace(' ', ''))
if produto1 < produto2 and produto1 < produto3:
    print('Você deve comprar o primeiro produto.')
if produto2 < produto1 and produto2 < produto3:
    print('Você deve comprar o segundo produto.')
else:
    print('Você deve comprar o terceiro produto.')
