# Exercício 22 - Sua organização acaba de contratar um estagiário para trabalhar no Suporte de Informática, com a intenção de fazer um levantamento nas sucatas 
# encontradas nesta área. A primeira tarefa dele é testar todos os cerca de 200 mouses que se encontram lá, testando e anotando o estado de cada um deles, para 
# verificar o que se pode aproveitar deles.

# Foi requisitado que você desenvolva um programa para registrar este levantamento. O programa deverá receber um número indeterminado de entradas, cada uma contendo:
# um número de identificação do mouse o tipo de defeito:

# - necessita da esfera;
# - necessita de limpeza;
# - necessita troca do cabo ou conector;
# - quebrado ou inutilizado
# - Uma identificação igual a zero encerra o programa.

# Ao final o programa deverá emitir o seguinte relatório:

identificacao = []
a = 0
b = 0
c = 0
d = 0

print(f'''
Defeitos:
[A] Necessita da esfera;
[B] Necessita de limpeza; 
[C] Necessita troca do cabo ou conector; 
[D] Quebrado ou inutilizado 

''')

while True:
  codigo = int(input('Identificação do mouse: '))
  if codigo == 0:
    break
  elif codigo < 0:
    print('Informe um código positivo válido ou digite 0 para encerrar.')
  elif codigo > 0:
    identificacao.append(codigo)
    while True:
      classificacao = input('Selecione o tipo de defeito: [A], [B], [C] ou [D] ').upper()
      if classificacao == 'A':
        a += 1
        break
      elif classificacao == 'B':
        b += 1
        break
      elif classificacao == 'C':
        c += 1
        break
      elif classificacao == 'D':
        d += 1
        break
      else:
        print('Informe um tipo de defeito entre A, B, C ou D!')  
  else:
    print('Informe um código positivo válido ou digite 0 para encerrar.')

total = a + b + c + d
pa = (a / total) * 100
pb = (b / total) * 100
pc = (c / total) * 100
pd = (d / total) * 100

print()
print(f'Quantidade de mouses: {len(identificacao)}')
print(f'''

         Situação                                   Qtd                     %
[A] Necessita da esfera:                              {a}                   {pa:.1f}
[B] Necessita de limpeza:                             {b}                   {pb:.1f}
[C] Necessita troca do cabo ou conector:              {c}                   {pc:.1f}
[D] Quebrado ou inutilizado:                          {d}                   {pd:.1f}
''')

