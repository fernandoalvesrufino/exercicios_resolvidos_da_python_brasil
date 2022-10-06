# Exercício 1 - Faça um programa que leia um arquivo texto contendo uma lista de endereços IP e gere um outro arquivo, contendo um relatório dos endereços IP válidos e inválidos.

# O arquivo de entrada possui o seguinte formato:

# 200.135.80.9
# 192.168.1.1
# 8.35.67.74
# 257.32.4.5
# 85.345.1.2
# 1.2.3.4
# 9.8.234.5
# 192.168.0.256

validos = []
invalidos = []
result_validos = []
result_invalidos = []

def validar_ip (numeros):
  sim = 0
  nao = 0
  teste = numeros.split('.')
  for i in teste:
    valor = int(i)
    if 0 <= valor <= 255:
      #validos.append(numeros)
      sim += 1
    else:
      #invalidos.append(numeros)
      nao += 1 
  if sim == 4:
    result_validos.append(numeros)
  else:
    result_invalidos.append(numeros)


with open("sample_data/ips_entrada.txt","r") as arquivo_entrada:
  linhas = arquivo_entrada.readlines()  
  
  for linha in linhas:
    validar_ip(linha)

with open("sample_data/ips_saida.txt","w") as arquivo_saida:
  arquivo_saida.write('[Endereços Válidos:]\n')
  for i in range(len(result_validos)):
    arquivo_saida.write(result_validos[i])
  
  arquivo_saida.write('\n')
  arquivo_saida.write('[Endereços Inválidos:]\n')
  for i in range(len(result_invalidos)):
    arquivo_saida.write(result_invalidos[i])
