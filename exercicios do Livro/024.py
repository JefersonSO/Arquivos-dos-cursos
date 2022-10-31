'''O IPVA de um veiculo é calculado tomando como base o valor do veiculo,
 o combustivel utilizado e o tipo do veiculo que seram fornecidos pelo usuario.
Em seguida, o IPVA será calculado como 4% do valor do veiculo, no caso de automoveis
movidos a gasolina ou flex. Já para carros movidos somente a etanol,
eletricidade ou gás ou qualquer um desses três combinados, a alíquota é de 3 %. Para motos,
camionetes cabine simples e ônibus ou micro-ônibus a alíquota é de 2% e para caminhões,
 de 1,5%. Elaborar uma rotina que, a partir destas informações, calcule e mostre p valor do IPVA.'''

valor_veiculo = float(input('Valor do veiculo:'))
tipo_combustivel = str(input('Qual o tipo de combustivel ?:\n[1] Gasolina \n[2] Flex \n[3] Etanol \n[4] Eletricidade \n[5] Gás\n '))
tipo_veiculo = int(input('Qual é o tipo do veiculo ?: \n[1] Carro \n[2] Caminhões \n[3] Outro\n '))
IPVA = 0
if tipo_veiculo == 1:
    if tipo_combustivel == 1 and 2:
        IPVA = (4 * valor_veiculo) / 100
        print(f'O IPVA desse veiculo é R$ {IPVA:.2f}')
    elif tipo_combustivel != 1 and 2:
         IPVA = (3 * valor_veiculo) / 100
         print(f'O IPVA desse veiculo é $ {IPVA:.2f}')
elif tipo_veiculo == 2:
        IPVA = (1.5 * valor_veiculo) / 100
        print(f'O IPVA desse veiculo é $ {IPVA:.2f}')
elif tipo_veiculo == 3:
        IPVA = (2 * valor_veiculo) / 100
        print(f'O IPVA desse veiculo é $ {IPVA:.2f}')
else:
    print('Digite uma opção valida.')
print('foi')

