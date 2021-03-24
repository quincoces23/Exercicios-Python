# Faça um Programa que calcule a área de um quadrado.
# Em seguida mostre o dobro desta área para o usuário.
lado = float(input('Diga um lado do quadrado: ').replace(' ', ''))
print(f'A área do quadrado corresponde ao lado vezes ele mesmo, ou seja,'
      f' {lado*lado} e o dobro desse valor corresponde a {(lado*lado)*2}')
