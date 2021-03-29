# Faça um Programa que leia três números e mostre o maior e o menor deles.

valor1 = float(input('Digite o primeiro valor: ').replace(' ', ''))
valor2 = float(input('Digite o segundo valor: ').replace(' ', ''))
valor3 = float(input('Digite o terceiro valor: ').replace(' ', ''))
lista_valores = [valor1, valor2, valor3]
print(f'O maior valor é o {max(lista_valores)}')
print(f'O menor valor é o {min(lista_valores)}')
