tabela = (
    'Palmeiras',
    'Flamengo',
    'Fluminense',
    'São Paulo',
    'Athletico Paranaense',
    'Bragantino',
    'Coritiba',
    'Bahia',
    'Botafogo',
    'Atlético Mineiro',
    'Internacional',
    'Vasco da Gama',
    'Cruzeiro',
    'Vitória',
    'Grêmio',
    'Santos',
    'Corinthians',
    'Mirassol',
    'Remo',
    'Chapecoense'
)

print('Primeiros 5 times:')
print(tabela[0:5])

print('\nÚltimos 4 times:')
print(tabela[-4:])

print('\nTabela em ordem alfabética:')
print(sorted(tabela))

indice = tabela.index('Chapecoense') + 1
print(f'\nChapecoense está na posição {indice}')