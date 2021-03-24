# Faça um programa para a leitura de duas notas parciais de um aluno. O programa
# deve calcular a média alcançada por aluno e apresentar:
# A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
# A mensagem "Reprovado", se a média for menor do que sete;
# A mensagem "Aprovado com Distinção", se a média for igual a dez.

nota1 = float(input('Qual foi a sua primeira nota? ').replace(' ', ''))
nota2 = float(input('Qual foi a sua segunda nota? ').replace(' ', ''))
média = (nota1+nota2)/2
if 7 <= média < 10:
    print('Aprovado.')
elif média < 7:
    print('Reprovado.')
if média == 10.0:
    print('Aprovado com Distinção.')
