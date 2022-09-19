# Exercício 37 - Uma academia deseja fazer um senso entre seus clientes para descobrir o mais alto, o mais baixo, a mais gordo e o mais magro, para isto você deve
# fazer um programa que pergunte a cada um dos clientes da academia seu código, sua altura e seu peso. O final da digitação de dados deve ser dada quando o usuário
# digitar 0 (zero) no campo código. Ao encerrar o programa também deve ser informados os códigos e valores do clente mais alto, do mais baixo, do mais gordo e do 
# mais magro, além da média das alturas e dos pesos dos clientes

maior = 0
menor = 9999
pesado = 0
leve = 9999

while True:
  codigo = int(input('Informe o código do cliente: '))
  if codigo == 0:
    break
  
  altura = float(input('Informe a altura do cliente: '))
  peso = float(input('Informe o peso do cliente: '))

  if altura > maior:
    maior = altura
    codigo_maior = codigo
    peso_maior = peso
  if altura < menor:
    menor = altura
    codigo_menor = codigo
    peso_menor = peso

  if peso > pesado:
    pesado = peso
    codigo_pesado = codigo
    altura_pesado = altura
  if peso < leve:
    leve = peso
    codigo_leve = codigo
    altura_leve = altura
  print()

print(f'''

Cliente mais alto: Código {codigo_maior} - ALTURA {maior} m - Peso {peso_maior} Kg
Cliente mais baixo: Código {codigo_menor} - ALTURA {menor} m - Peso {peso_menor} Kg
Cliente mais gordo: Código {codigo_pesado} - Altura {altura_pesado} m - PESO {pesado} Kg
Cliente mais magro: Código {codigo_leve} - Altura {altura_leve} m - PESO {leve} Kg
''')
