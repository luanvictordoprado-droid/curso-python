lista = []
lista_feminino = []
lista_maiormedia = []
total_idade = 0

while True:
    dicionario = {}

    dicionario['nome'] = input('Nome: ').strip()

    while True:
        sexo = input('Sexo (M/F): ').strip().upper()
        if sexo in ['M', 'F']:
            dicionario['sexo'] = sexo
            break
        print('ERRO! Digite apenas M ou F.')

    dicionario['idade'] = int(input('Idade: '))
    total_idade += dicionario['idade']

    if dicionario['sexo'] == 'F':
        lista_feminino.append(dicionario['nome'])

    lista.append(dicionario.copy())

    while True:
        pergunta = input('Quer continuar? [S/N]: ').strip().upper()
        if pergunta in ['S', 'N']:
            break
        print('ERRO! Digite apenas S ou N.')

    if pergunta == 'N':
        break

quantidade = len(lista)
media = total_idade / quantidade

for pessoa in lista:
    if pessoa['idade'] > media:
        lista_maiormedia.append(pessoa.copy())

print('-=' * 30)
print(lista)
print(f'A) Ao todo temos {quantidade} pessoas cadastradas.')
print(f'B) A média de idade é de {media:.2f} anos.')
print(f'C) As mulheres cadastradas foram: {lista_feminino}')
print('D) Lista das pessoas que estão acima da média:')

for pessoa in lista_maiormedia:
    for k, v in pessoa.items():
        print(f'   {k} = {v}')
    print()