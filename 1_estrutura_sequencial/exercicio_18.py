# Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um link de
# internet (em Mbps), calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos).

tamanho = float(input('Informe o tamanho do arquivo em MB que você deseja baixar: '))
velocidade = float(input('Informe a velocidade do link em Mbps: '))
tempo = tamanho / (velocidade / 8)
minutos = int(tempo / 60)
segundos = int(tempo % 60)
print(f'\nTempo estimado de download é de {tempo:.0f} segundos \nAproximadamente {minutos} min e {segundos} seg.')
