# Faça um Programa que peça as 4 notas bimestrais e mostre a média.
nota1 = float(input('Quanto você tirou na primeira prova?').replace(' ', ''))
nota2 = float(input('Quanto você tirou na segunda prova?').replace(' ', ''))
nota3 = float(input('Quanto você tirou na terceira prova?').replace(' ', ''))
nota4 = float(input('Quanto você tirou na quarta prova?').replace(' ', ''))
print(f'Sua média nesse bimestre foi {(nota1+nota2+nota3+nota4)/4:.2f}')
