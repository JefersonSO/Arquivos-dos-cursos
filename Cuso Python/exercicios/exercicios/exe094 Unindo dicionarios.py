todos = list()
pessoa = dict()
mulheres = list()
soma = acimedia = 0
while True:
    pessoa['nome'] = str(input('Nome: '))
    pessoa['sexo'] = str(input('Sexo: [M/F] '))
    while pessoa['sexo'] != 'm' and pessoa['sexo'] != 'f':
        print('ERRO! Por favor digite apenas M ou F.')
        pessoa['sexo'] = str(input('Sexo: [M/F] '))
    pessoa['idade'] = int(input('Idade: '))
    if pessoa['sexo'] in 'Ff':
        mulheres.append(pessoa['nome'])
    todos.append(pessoa.copy())
    resp = str(input('Quer continuar? '))
    while resp != 'N' and resp != 'n' and resp != 'S' and resp != 's':
        print('ERRO! Por favor digite apenas S ou N.')
        resp = str(input('Quer continuar? '))
    if resp == 'S' or resp == 's':
        continue
    elif resp == 'N' or resp == 'n':
        break
print(todos)
print('-='*30)
print(f'A) Ao todo temos {len(todos)} cadastrados.')
for c in range(0, len(todos)):
    soma += todos[c]["idade"]
media = soma / len(todos)
print(f'B) A media de idade é de {media:.2f}')
print(f'C)As mulheres cadastradas foram {mulheres}')
for c in range(0, len(todos)):
   if todos[c]['idade'] > media:
        print(f'D) Lista de pessoas que estão acima da media:')
        print(f'nome = {todos[c]["nome"]} sexo = {todos[c]["sexo"]} idade = {todos[c]["idade"]}')