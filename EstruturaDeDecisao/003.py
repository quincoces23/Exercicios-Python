# Faça um Programa que verifique se uma letra digitada é "F" ou "M". Conforme
# a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.

sexo = str(input('Digite o seu sexo F - Feminino, M - Masculino: ').upper().replace(' ', ''))
if sexo == 'F':
    print('Feminino')
elif sexo == 'M':
    print('Masculino')
else:
    print('Digite M/F para escolher o sexo.')