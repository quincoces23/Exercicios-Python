# As Organizações Tabajara resolveram dar um aumento de salário aos seus
# colaboradores e lhe contraram para desenvolver o programa que calculará os reajustes.
# Faça um programa que recebe o salário de um colaborador e o reajuste segundo
# o seguinte critério, baseado no salário atual:
# salários até R$ 280,00 (incluindo) : aumento de 20%
# salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
# salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
# salários de R$ 1500,00 em diante : aumento de 5% Após o aumento ser realizado,
# informe na tela:
# o salário antes do reajuste;
# o percentual de aumento aplicado;
# o valor do aumento;
# o novo salário, após o aumento.

salario = float(input('Qual é o seu salário: R$ ').replace(' ', ''))
print(f'Seu salário atualmente é R${salario:.2f} Reais.')

if salario <= 280:
    print(f'Você vai receber um aumento de 20%.\n'
          f'Esse valor corresponde a {20/100*salario:.2f}\n'
          f'Seu salário novo é R${salario+(20/100*salario):.2f} Reais.')
if 280 < salario <= 700:
    print(f'Você vai receber um aumento de 15%.\n'
          f'Esse valor corresponde a {15/100*salario:.2f}\n'
          f'Seu salário novo é R${salario+(15/100*salario):.2f} Reais.')
if 700 < salario <= 1500:
    print(f'Você vai receber um aumento de 10%.\n'
          f'Esse valor corresponde a {10/100*salario:.2f}\n'
          f'Seu salário novo é R${salario+(10/100*salario):.2f} Reais.')
if 1500 < salario:
    print(f'Você vai receber um aumento de 5%.\n'
          f'Esse valor corresponde a {5/100*salario:.2f}\n'
          f'Seu salário novo é R${salario+(5/100*salario):.2f} Reais.')
