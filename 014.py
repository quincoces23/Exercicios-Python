# João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar
# o rendimento diário de seu trabalho. Toda vez que ele traz um peso de peixes maior
# que o estabelecido pelo regulamento de pesca do estado de São Paulo (50 quilos)
# deve pagar uma multa de R$ 4,00 por quilo excedente. João precisa que você faça
# um programa que leia a variável peso (peso de peixes) e calcule o excesso.
# Gravar na variável excesso a quantidade de quilos além do limite e na variável
# multa o valor da multa que João deverá pagar. Imprima os dados do programa
# com as mensagens adequadas.

quilos_peixe = float(input('João, Digite o peso dos peixes: ').replace(' ', ''))
if quilos_peixe > 50.0:
    print(f'Infelizmente passou dos 50 quilos.\nUma multa'
          f' de {(quilos_peixe-50)*4.00:.2f} Reais Será atribuida a essa pesca.')
else:
    print(f'O senhor não ultrapassou o valor em quilos permitido.')