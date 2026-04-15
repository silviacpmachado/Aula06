# Valor de venda - 10% para vendas acima de R$ 1.000,00


resposta = 'S'
soma = 0

while resposta != "N":
    valor = float(input('Digite o valor da compra: '))

    if valor > 1000:
      desconto = valor * 0.10
      valor_final = valor - desconto
    else:
      valor_final = valor

soma += valor_final
resposta = input('Quer continuar? [S/N] ').upper().strip()

print(f'O total da soma é: {soma}')