# Exercício 12 - Classe Conta de Investimento: Faça uma classe contaInvestimento que seja semelhante a classe contaBancaria, com a diferença de que se adicione
# um atributo taxaJuros. Forneça um construtor que configure tanto o saldo inicial como a taxa de juros. Forneça um método adicioneJuros (sem parâmetro explícito) 
# que adicione juros à conta. Escreva um programa que construa uma poupança com um saldo inicial de R$1000,00 e uma taxa de juros de 10%. Depois aplique o método
# adicioneJuros() cinco vezes e imprime o saldo resultante.

class ContaInvestimento():
  def __init__(self, taxa_juros, saldo):
    self.taxa_juros = taxa_juros
    self.saldo = saldo
        
  def verificarSaldo(self):
    return f'Valor em conta: R$ {self.saldo:.2f}'
    

  def addJuros(self
               ):
    self.saldo += (self.taxa_juros/100)*self.saldo
    return f'O novo saldo é de {self.saldo:.2f}'


nome = input('Nome: ').upper()
num = input('Conta: ')
valor_em_conta = float(input('Digite seu valor em R$: '))
tax = float(input('Digite a taxa de Juros: '))

xp = ContaInvestimento(tax, valor_em_conta)

print(xp.addJuros())
print(xp.addJuros())
print(xp.addJuros())
print(xp.addJuros())
print(xp.addJuros())
