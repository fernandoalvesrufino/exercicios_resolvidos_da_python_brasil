# Bônus: Imprima todos os números primos de 2 à 100

for n in range(2, 100):
  cont = 0
  for i in range(1, n + 1):
    if n % i == 0:
      cont += 1
    else:
      cont = cont

  if cont == 2:
    print(n, end = ' ')

# números primos de 2 à 100:
# 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97
