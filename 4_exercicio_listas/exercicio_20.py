# Exercício 20 - As Organizações Tabajara resolveram dar um abono aos seus colaboradores em reconhecimento ao bom resultado alcançado durante o ano que 
# passou. Para isto contratou você para desenvolver a aplicação que servirá como uma projeção de quanto será gasto com o pagamento deste abono. Após reuniões envolvendo a diretoria executiva, a diretoria financeira e os representantes do sindicato laboral, chegou-se a seguinte forma de cálculo:

# a. Cada funcionário receberá o equivalente a 20% do seu salário bruto de dezembro;
# b. O piso do abono será de 100 reais, isto é, aqueles funcionários cujo salário for muito baixo, recebem este valor mínimo; Neste momento, não se deve ter nenhuma preocupação com colaboradores com tempo menor de casa, descontos, impostos ou outras particularidades. Seu programa deverá permitir a digitação do salário de um número indefinido (desconhecido) de salários. Um valor de salário igual a 0 (zero) encerra a digitação. Após a entrada de todos os dados o programa deverá calcular o valor do abono concedido a cada colaborador, de acordo com a regra definida acima. Ao final, o programa deverá apresentar:

# O salário de cada funcionário, juntamente com o valor do abono;
# O número total de funcionário processados;
# O valor total a ser gasto com o pagamento do abono;
# O número de funcionário que receberá o valor mínimo de 100 reais;
# O maior valor pago como abono;
# A tela abaixo é um exemplo de execução do programa, apenas para fins ilustrativos. Os valores podem mudar a cada execução do programa.

salario = []
abono = []
minimo = 0
maior = 0

while True:
  valor = float(input('Salário: '))
  if valor == 0:
    break
  else:
    salario.append(valor)
    beneficio = valor * 0.2
    if beneficio <= 100:
      minimo += 1
      beneficio = 100
      abono.append(beneficio)
    else:
      abono.append(beneficio)
    if beneficio > maior:
      maior = beneficio

print()
print('    Salário      -      Abono')
for i in range(len(salario)):
  print(f'R$ {salario[i]:10.2f}    - R$ {abono[i]:10.2f}')

print()

print(f'Número de funcionários processados: {len(salario)}')
print(f'Valor total gasto com o pagamento do abono: R$ {sum(abono):.2f}')
print(f'A quantidade de funcionários que receberá o valor mínimo é: {minimo}')
print(f'O maior valor pago como abono foi: R$ {maior:.2f}')
