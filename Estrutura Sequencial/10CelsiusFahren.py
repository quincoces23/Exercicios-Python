# Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Fahrenheit.
temperatura_celsius = float(input('Me diga a temperatura em Celsius que deseja '
                                  'converter para Fahrenheit:').replace(' ', ''))
print(f'{temperatura_celsius}Celsius fica'
      f' {(temperatura_celsius*(9/5)) +32 :.2f} em Fahrenheit.')
