# Tendo como dados de entrada a altura de uma pessoa, construa um algoritmo
# que calcule seu peso ideal, usando a seguinte fórmula: (72.7*altura) - 58

altura = float(input('Qual é a sua altura em metros? ').replace(' ', ''))
print(f'Seu peso ideal é {(72.7*altura) - 58:.2f}')
