# Exercício 2 - A ACME Inc., uma empresa de 500 funcionários, está tendo problemas de espaço em disco no seu servidor de arquivos. Para tentar resolver este 
# problema, o Administrador de Rede precisa saber qual o espaço ocupado pelos usuários, e identificar os usuários com maior espaço ocupado. Através de um 
# programa, baixado da Internet, ele conseguiu gerar o seguinte arquivo, chamado "usuarios.txt":

# alexandre 456123789
# anderson 1245698456
# antonio 123456456
# carlos 91257581
# cesar 987458
# rosemary 789456125
# Neste arquivo, o nome do usuário possui 15 caracteres. A partir deste arquivo, você deve criar um programa que gere um relatório, chamado "relatório.txt", 
# no seguinte formato:
  
nomes = []
memoria = []
branco = ''

def converter(valor):
  bite = float(valor)
  mb = bite / 1024 **2
  memoria.append(mb)    


with open("sample_data/usuarios.txt","r") as arquivo_entrada:
  linhas = arquivo_entrada.readlines()

  for linha in linhas:
    dados = linha.split(' ')
    dados = [value for value in dados if value != branco]
    nomes.append(dados[0]) 
    megabytes = converter(dados[1])

total = sum(memoria)
    
with open("sample_data/relatorio.txt","w") as arquivo_saida:
  arquivo_saida.write(f'''
ACME Inc.               Uso do espaço em disco pelos usuários
------------------------------------------------------------------------
Nr.  Usuário        Espaço utilizado     % do uso

''')
  
  for i in range(len(nomes)):
    porc = (memoria[i] / total) * 100
    nome = nomes[i]
    armaz = memoria[i]
    arquivo_saida.write(f'{i + 1:2}   {nome:15} {armaz:10.2f} MB {porc:12.2f} %\n')
  arquivo_saida.write(f'\nEspaço total ocupado: {total:.2f} MB\n')
  arquivo_saida.write(f'Espaço médio ocupado: {total / len(memoria):.2f} MB')    

#Espaço total ocupado: 2581,57 MB
#Espaço médio ocupado: 430,26 MB
