# Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em
# metros quadrados da área a ser pintada. Considere que a cobertura da tinta é
# de 1 litro para cada 6 metros quadrados e que a tinta é vendida em latas de 18
# litros, que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.
# Informe ao usuário as quantidades de tinta a serem compradas e os respectivos
# preços em 3 situações:
# comprar apenas latas de 18 litros;
# comprar apenas galões de 3,6 litros;
# misturar latas e galões, de forma que o desperdício de tinta seja menor.
# Acrescente 10% de folga e sempre arredonde os valores para cima, isto é,
# considere latas cheias.
from math import ceil


area = float(input('Qual o tamanho da área que desejas pintas em '
                   'metros ao quadrado: ').replace(' ', ''))

litros_necessarios = area/6
latas_necessarias = litros_necessarios/18 + ((10/100) * litros_necessarios)
custo_latas = ceil(latas_necessarias) * 80.0
galoes_necessarios = litros_necessarios/3.6 + ((10/100) * litros_necessarios)
custo_galoes = ceil(galoes_necessarios) * 25.0

quantidade_galoes_misto = litros_necessarios // 3.6
quantidade_latas_misto = ceil((litros_necessarios - quantidade_galoes_misto * 3.6) / 18.0)
valor_galao_misto = quantidade_galoes_misto * 25.0
valor_lata_misto = quantidade_latas_misto * 80.0

print('-=-'*29)

print(f'Compando apenas latas, você vai precisar de {ceil(latas_necessarias)}'
      f' lata(s) isso vai custar R${custo_latas:.2f} Reais. ')

print('-=-'*29)

print(f'Compando apenas galões, você vai precisar de {ceil(galoes_necessarios)}'
      f' galões isso vai custar R${custo_galoes:.2f} Reais. ')

print('-=-'*29)

print(f'Misturando latas e galões para maior eficiencia, precisamos de'
      f' {quantidade_galoes_misto:.0f} Galões, e de'
      f' {quantidade_latas_misto} Lata(s)\nNo total o valor vai ficar por'
      f' R${valor_lata_misto + valor_galao_misto:.2f} Reais.')
