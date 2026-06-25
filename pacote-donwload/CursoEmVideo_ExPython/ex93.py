dados = dict()
lista_gols = list()
dados['nome'] = str(input('Nome: '))
partidas = int(input(f'Quantas partidas {dados["nome"]} jogou? '))
for c, partidas in enumerate(range(0, partidas)):
    lista_gols.append(int(input(f'Quantos gols na partida {partidas}? ')))
dados['Gols'] = lista_gols[:]
total = sum(lista_gols)
dados['Total'] = total
print(dados)

for z,v in dados.items():
    print(f'O campo {z} tem o valor  {v}')
print(f'O jogador {dados["nome"]} jogou {len(dados["Gols"])} partidas.')
for i,v in enumerate(dados['Gols']):
    print(f'Na partida {i} ,fez {v} gols.')