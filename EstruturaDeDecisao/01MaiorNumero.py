# Faça um Programa que peça dois números e imprima o maior deles.
numero1 = float(input('Me diga um número:').replace(' ', ''))
numero2 = float(input('Me diga outro número:').replace(' ', ''))
if numero1>numero2:
    print(f'O número {numero1} é maior que o {numero2}')
elif numero1<numero2:
    print(f'O número {numero2} é maior que o {numero1}')
else:
    print('Os números tem o mesmo valor.')