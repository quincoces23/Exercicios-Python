# Faça um Programa que leia três números e mostre-os em ordem decrescente.
valor1 = float(input('Digite o primeiro valor: ').replace(' ', ''))
valor2 = float(input('Digite o primeiro valor: ').replace(' ', ''))
valor3 = float(input('Digite o primeiro valor: ').replace(' ', ''))
lista_valores = [valor3, valor2, valor1]
print(f'Na ordem decrescente:{sorted(lista_valores, key=int, reverse=True )}')
