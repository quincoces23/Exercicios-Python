# Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
# Calcule e mostre o total do seu salário no referido mês, sabendo-se que são
# descontados 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato,
# faça um programa que nos dê:
# salário bruto.
# quanto pagou ao INSS.
# quanto pagou ao sindicato.
# o salário líquido.
# calcule os descontos e o salário líquido, conforme a tabela abaixo:
# + Salário Bruto : R$
# - IR (11%) : R$
# - INSS (8%) : R$
# - Sindicato ( 5%) : R$
# = Salário Liquido : R$
# Obs.: Salário Bruto - Descontos = Salário Líquido.

ganho_hora = float(input('Valor ganho por hora: R$').replace(' ', ''))
horas_mes_trabalho = float(input('Quantas horas de trabalho no mês: ').replace(' ', ''))
salário_mes = ganho_hora*horas_mes_trabalho
print(f'Seu salário bruto é de R${salário_mes:.2f} Reais.')
print(f'Foi descontado R${salário_mes*(8/100):.2f} Reais do seu salário para o INSS.')
print(f'Foi descontado R${salário_mes*(5/100):.2f} Reais do seu salário para o Sindicato.')
print(f'Foi descontado R${salário_mes*(11/100):.2f} Reais do seu salário para o Imposto de Renda.')
print(f'Seu salário liquido vai ser R$'
      f'{salário_mes -(salário_mes*(8/100)) - (salário_mes*(5/100)) - (salário_mes*(11/100)):.2f} Reais.')