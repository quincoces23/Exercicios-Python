# Faça um Programa que peça o raio de um círculo, calcule e mostre sua área.
raio_circulo = float(input('Qual é o raio do circulo? ').replace(' ', ''))
print(f'A área desse circulo é ele vezes ele mesmo, vezes pi(3,14)'
      f' ou seja {(raio_circulo*raio_circulo) * 3.14:.2f} Cm ao quadrado.')
