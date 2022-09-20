# Exercício 46 - Em uma competição de salto em distância cada atleta tem direito a cinco saltos. No final da série de saltos de cada atleta, o melhor e o pior 
# resultados são eliminados. O seu resultado fica sendo a média dos três valores restantes. Você deve fazer um programa que receba o nome e as cinco distâncias
# alcançadas pelo atleta em seus saltos e depois informe a média dos saltos conforme a descrição acima informada (retirar o melhor e o pior salto e depois calcular 
# a média). Faça uso de uma lista para armazenar os saltos. Os saltos são informados na ordem da execução, portanto não são ordenados. O programa deve ser encerrado 
# quando não for informado o nome do atleta. A saída do programa deve ser conforme o exemplo abaixo:

atletas = []
media_salto = []
nome = 'Start'
contagem = ['Primeiro', 'Segundo', 'Terceiro', 'Quarto', 'Quinto']
salto: list[float] = []
saltos_dos_atletas = []

while True:
    menor = 999999
    maior = 0
    nome = input('Atleta: ')
    print()
    if nome == '' or nome == ' ':
        break
    else:
        salto.clear()                                       # Zera os valores dos saltos
        atletas.append(nome)                                # Adiciona o nome do atleta a lista de nomes
        media = 0                                           # zera a media dos saltos

        for contagem_de_saltos in range(5):
            distancia_salto = float(input(f'{contagem[contagem_de_saltos]} salto: '))
            salto.append(distancia_salto)                   # Adiciona à lista de saltos a distancia do salto
        for numero_salto in range(5):
            if salto[numero_salto] > maior:
                maior = salto[numero_salto]
            if salto[numero_salto] < menor:
                menor = salto[numero_salto]
        salto.remove(maior)                                 # remove o maior salto da lista
        salto.remove(menor)                                 # remove o menor salto da lista
        print()
        print(f'Melhor salto: {maior:.1f} m')               # imprime o maior salto
        print(f'Pior salto: {menor:.1f} m')                 # imprime o menor salto
        media = (sum(salto)) / 3                            # Calcula a média dos saltos sem o maior e o menor
        media_salto.append(media)                           # adiciona a lista de media de saltos
        print(f'Média dos demais saltos: {media:.2f} m')    # Imprime qual foi a média dos saltos do atleta

        for valor in range(3):
            saltos_dos_atletas.append(salto[valor])

    print()

inicio = 0
fim = 3

for atleta in range(len(atletas)):                          # para cada atleta da lista de atletas
    print('Resultado final:')
    print(f'Atleta: {atletas[atleta]}')                     # Imprime o nome do atleta
    print()
    print(f'Saltos: ', end=' ')
    for i in range(3):
        if i == 2:
            print(saltos_dos_atletas[i + (atleta * 3)], end='')
        else:
            print(saltos_dos_atletas[i + (atleta * 3)], end=' - ')
    print(f'\nMédia dos saltos: {media_salto[atleta]:.2f} m')
    print()
