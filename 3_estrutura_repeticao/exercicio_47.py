# # Exercicio 47 - Em uma competição de ginástica, cada atleta recebe votos de sete jurados. A melhor e a pior nota são eliminadas. A sua nota fica sendo a média
# dos votos restantes. Você deve fazer um programa que receba o nome do ginasta e as notas dos sete jurados alcançadas pelo atleta em sua apresentação e depois
# informe a sua média, conforme a descrição acima informada (retirar o melhor e o pior salto e depois calcular a média com as notas restantes). As notas não são
# informados ordenadas. Um exemplo de saída do programa deve ser conforme o exemplo abaixo:

melhor = 0
pior = 999999
medias = []
melhor_nota = []
pior_nota = []
atletas = []

while True:
    notas = 0
    nome = input('Nome: ')
    if nome == '':
        break
    atletas.append(nome)
    print()
    for i in range(7):
        nota = float(input('Nota: '))
        notas += nota
        if nota > melhor:
            melhor = nota
        if nota < pior:
            pior = nota
    melhor_nota.append(melhor)
    pior_nota.append(pior)
    notas = notas - (melhor + pior)
    media = notas / 5
    medias.append(media)
    print()

print('RESULTADO FINAL:')
for i in range(len(atletas)):
    print(f'''
Atleta: {atletas[i]}
Melhor nota: {melhor_nota[i]:.2f}
Pior nota: {pior_nota[i]:.2f}
Média: {medias[i]:.2f}
''')
