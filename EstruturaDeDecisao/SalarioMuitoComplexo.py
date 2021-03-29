# Faça um programa para o cálculo de uma folha de pagamento, sabendo que os
# descontos são do Imposto de Renda, que depende do salário bruto
# (conforme tabela abaixo) e 3% para o Sindicato e que o FGTS corresponde a 11%
# do Salário Bruto, mas não é descontado (é a empresa que deposita). O Salário
# Líquido corresponde ao Salário Bruto menos os descontos. O programa deverá
# pedir ao usuário o valor da sua hora e a quantidade de horas trabalhadas no mês.
# Desconto do IR:
# Salário Bruto até 900 (inclusive) - isento
# Salário Bruto até 1500 (inclusive) - desconto de 5%
# Salário Bruto até 2500 (inclusive) - desconto de 10%
# Salário Bruto acima de 2500 -
# desconto de 20% Imprima na tela as informações, dispostas conforme o exemplo abaixo:
# No exemplo o valor da hora é 5 e a quantidade de hora é 220.
# Salário Bruto: (5 * 220)        : R$ 1100,00
# (-) IR (5%)                     : R$   55,00
# (-) INSS ( 10%)                 : R$  110,00
# FGTS (11%)                      : R$  121,00
# Total de descontos              : R$  165,00
# Salário Liquido                 : R$  935,00

salario_hora = float(input('Diga quanto você ganha por hora: R$ ').replace(' ', ''))
horas_trabalho = float(input('Quantas horas você trabalha por mês: ').replace(' ', ''))
salario_bruto = salario_hora * horas_trabalho
desconto_ir_5 = 5/100*salario_bruto
desconto_ir_10 = 10/100*salario_bruto
desconto_ir_20 = 20/100*salario_bruto
desconto_inss = 10/100*salario_bruto
desconto_fgts = 11/100*salario_bruto
desconto_sindicato = 3/100*salario_bruto

if salario_bruto <= 900:
    print(f'Salário Bruto: R${horas_trabalho*salario_hora:.2f}\n'
          f'(-) IR: Isento\n'
          f'(-) INSS (10%): R${desconto_inss:.2f}\n'
          f'FGTS -Empresa- (11%): R${desconto_fgts:.2f}\n'
          f'Sindicato (3%): R${desconto_sindicato:.2f}\n'
          f'Total de descontos: R${desconto_inss + desconto_sindicato:.2f}\n'
          f'Seu Salário liquido:'
          f' R${salario_bruto - desconto_inss - desconto_sindicato:.2f}.')
if 900 < salario_bruto <= 1500:
    print(f'Salário Bruto: R${horas_trabalho * salario_hora:.2f}\n'
          f'(-) IR (5%): R${desconto_ir_5:.2f}\n'
          f'(-) INSS (10%): R${desconto_inss:.2f}\n'
          f'FGTS -Empresa- (11%): R${desconto_fgts:.2f}\n'
          f'Sindicato (3%): R${desconto_sindicato:.2f}\n'
          f'Seu Salário liquido fica em'
          f' R${salario_bruto - desconto_ir_5 - desconto_inss - desconto_sindicato:.2f}.')
if 1500 < salario_bruto <= 2500:
    print(f'Salário Bruto: R${horas_trabalho * salario_hora:.2f}\n'
          f'(-) IR (10%): R${desconto_ir_10:.2f}\n'
          f'(-) INSS (10%): R${desconto_inss:.2f}\n'
          f'FGTS -Empresa- (11%): R${desconto_fgts:.2f}\n'
          f'Sindicato (3%): R${desconto_sindicato:.2f}\n'
          f'Seu Salário liquido fica em'
          f' R${salario_bruto - desconto_ir_10 - desconto_inss - desconto_sindicato:.2f}.')
if 2500 < salario_bruto:
    print(f'Salário Bruto: R${horas_trabalho * salario_hora:.2f}\n'
          f'(-) IR (20%): R${desconto_ir_20:.2f}\n'
          f'(-) INSS (10%): R${desconto_inss:.2f}\n'
          f'FGTS -Empresa- (11%): R${desconto_fgts:.2f}\n'
          f'Sindicato (3%): R${desconto_sindicato:.2f}\n'
          f'Seu Salário liquido fica em'
          f' R${salario_bruto - desconto_ir_20 - desconto_inss - desconto_sindicato:.2f}.')
