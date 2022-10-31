'''Desenvolver um programa para uma loja que precisa determinar o preço
 final de compra, a partir dos seguintes dados fornecidos pelo usuario:
 codigo, descrição, peso, quantidade, preço. Em seguida, para determinar o
 preço final, devem-se utilizar os seguintes criterios para calculo:
  a) O preço total (bruto) é obtido multiplicando o preço unitario com a quantidade;

  b) O valor do imposto sera obtido por meio das seguintes faixas:

        -Preço total(bruto)-           -Valor do imposto-
        ----------------------------------------------------
        <R$ 500,00              5,0% do preço total (bruto)
        ----------------------------------------------------
        >=R$ 500,00             7,5% do preço total (bruto)
        e <R$ 1.500,00
        ----------------------------------------------------
        >= R$ 1.500,00          10,0% do preço total (bruto)
        ----------------------------------------------------

  c) Quando o preso total do produto (peso x quantidade) for maior que 10 kg
   acrescentar R$ 50,00 de frete, caso contrario, o frete será gratuito;

  d) O preço final sera obtido somando o preço total (bruto) com o valor do imposto
   e o custo do frete.        '''


codigo = str(input('Código do produto: '))
descricao = str(input('Nome do profuto: '))
peso = float(input('Peso: '))
quantidade = int(input('Quantidade: '))
preco = float(input('Preço R$: '))
valorT = preco*quantidade
pesoT = peso*quantidade
print('-'*30)
print(f'Preço total R$: {valorT:.3f}')
print('-'*30)
if preco < 500:
    valorT = preco + (preco * 5 / 100)
elif preco >= 500 and preco <= 1.500:
    valorT = preco + (preco * 7.5 / 100)
elif preco >= 1.500:
    valorT = preco + (preco * 10.0 / 100)

else:
    print('Digite uma opção valida')

if pesoT > 10:
    valorT += 50
print(f'O total a pagar R$ {valorT:.2f} com imposto e + R$ 50 de frete  ' )



