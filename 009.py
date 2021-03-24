# Faça um Programa que peça a temperatura em graus Fahrenheit,
# transforme e mostre a temperatura em graus Celsius.
temperatura_fahrenheit = float(input('Qual a temperatura em'
                                     ' Fahrenheit que deseja converter para '
                                     'graus Celsius? ').replace(' ', ''))
print(f'{temperatura_fahrenheit} Fahrenheit em graus Celsius fica'
      f' {(temperatura_fahrenheit - 32)*(5/9):.2f}')
