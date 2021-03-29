# Faça um Programa que pergunte em que turno você estuda. Peça para digitar
# M-matutino ou V-Vespertino ou N- Noturno. Imprima a mensagem "Bom Dia!",
# "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso.

turno = str(input('Digite em que turno você estuda!'
                  '\nM-matutino\nV-Vespertino\nN- Noturno ').upper().replace(' ', ''))
if turno == 'M':
    print('Bom dia.')
if turno == 'V':
    print('Boa tarde.')
if turno == 'N':
    print('Boa noite.')
else:
    print('Valor inválido.')
