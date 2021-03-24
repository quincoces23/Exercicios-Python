# Faça um Programa que verifique se uma letra digitada é vogal ou consoante.

letra = str(input('Digite uma letra: ').replace(' ', '').upper())
if letra == 'A' or letra == 'E' or letra == 'I' or letra == 'O' or letra == 'U':
    print('Se trata de uma vogal.')
else:
    print('Se trata de uma consoante.')
