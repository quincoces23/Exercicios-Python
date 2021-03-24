# Faça um programa que peça o tamanho de um arquivo para download (em MB) e a
# velocidade de um link de Internet (em Mbps), calcule e informe o tempo
# aproximado de download do arquivo usando este link (em minutos).

tamanho_arquivo = float(input('Qual o tamanho do arquivo em MB: ').replace(' ', ''))
velocidade_internet = float(input('Qual a velocidade da internet em mbps: ').replace(' ', ''))
print(f'O tempo aproximado do download do arquivo vai ser de'
      f' {(tamanho_arquivo/(velocidade_internet/ 8 ))/60:.2f} Minutos. ')
