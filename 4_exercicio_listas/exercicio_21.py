# Exercício 21 - Faça um programa que carregue uma lista com os modelos de cinco carros (exemplo de modelos: FUSCA, GOL, VECTRA etc). 
# Carregue uma outra lista com o consumo desses carros, isto é, quantos quilômetros cada um desses carros faz com um litro de combustível. Calcule e mostre:

# - O modelo do carro mais econômico;
# - Quantos litros de combustível cada um dos carros cadastrados consome para percorrer uma distância de 1000 quilômetros e quanto isto custará, considerando 
# um que a gasolina custe R$ 2,25 o litro. Abaixo segue uma tela de exemplo. O disposição das informações deve ser o mais próxima possível ao exemplo. Os dados
# são fictícios e podem mudar a cada execução do programa.

modelo = []
km = []
litros = []
preco = []
menor = 0
melhor_autonomia = 0

for i in range(5):
  print(f'Veículo {i+ 1}')
  marca = input('Nome: ')
  modelo.append(marca)
  autonomia = float(input('Km por litro: '))
  km.append(autonomia)
  print()
  calculo = 1000 / autonomia
  litros.append(calculo)
  valor = calculo * 2.25
  preco.append(valor)
  if km[i] > melhor_autonomia:
    melhor_autonomia = km[i]
    menor = i

print('Relatório final: ')
for i in range(5):
  print(f'{i + 1} - {modelo[i]:15} - {km[i]:10.3f} - {litros[i]:10.2f} litros - R$ {preco[i]:10.2f}')


print(f'O menor consumo é o da {modelo[menor]}')
