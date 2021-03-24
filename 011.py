# Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
# o produto do dobro do primeiro com metade do segundo .
# a soma do triplo do primeiro com o terceiro.
# o terceiro elevado ao cubo.

inteiro1 = int(input('Me diga um valor inteiro: ').replace(' ', ''))
inteiro2 = int(input('Me dida um segundo valor inteiro: ').replace(' ', ''))
real1 = float(input('Me diga um valor real: ').replace(' ', ''))
print(f'o dobro do primeiro número é {inteiro1*2}'
      f' e metade do segundo resulta em {inteiro2/2},'
      f' a multiplicação desses dois resultados é {inteiro1*inteiro1*(inteiro2/2)}.')
print(f'O triplo do primeiro número é {inteiro1*3},'
      f' mais o terceiro número, fica {(inteiro1*3) + real1}.')
print(f'O terceiro número elevado ao cubo resulta em {real1**3}.')
