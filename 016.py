# Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho
# em metros quadrados da área a ser pintada. Considere que a cobertura da tinta
# é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de
# 18 litros, que custam R$ 80,00. Informe ao usuário a quantidades de latas de
# tinta a serem compradas e o preço total.
from math import ceil

area_parede = float(input('Qual a área da parede que desejas pintar? ').replace(' ', ''))
litros_necessarios = area_parede/3
latas_necessarias = litros_necessarios/18
custo_latas = ceil(latas_necessarias)*80
print(f'Você vai precisar de {litros_necessarios:.2f} Litros de tinta\nO que'
      f' equivale a {latas_necessarias:.2f} latas de tinta.\nEssa quantidade'
      f'de latas de tinta, fica por R${custo_latas:.2f} Reais.')
