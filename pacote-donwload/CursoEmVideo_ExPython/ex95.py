lista_jogadores = list()
continuar = True

while continuar:
    dados = dict()
    lista_gols = list()

    dados['nome'] = str(input('Nome: '))
    partidas = int(input(f'Quantas partidas {dados["nome"]} jogou? '))

    for c, partida in enumerate(range(0, partidas), 1):
        gols = int(input(f'Gols na partida {partida}: '))
        lista_gols.append(gols)

    dados['gols'] = lista_gols[:]
    dados['total'] = sum(lista_gols)
    lista_jogadores.append(dados)

    while True:
        pergunta = str(input('Quer continuar? [S/N] ')).strip().upper()
        if pergunta == 'S':
            break
        elif pergunta == 'N':
            continuar = False   
            break
        else:
            print('Por favor, digite apenas S ou N.')


for i, jogador in enumerate(lista_jogadores, 1):
    print(f'----- Jogador {i} -----')
    print(f'Nome:  {jogador["nome"]}')
    print(f'Gols:  {jogador["gols"]}')
    print(f'Total: {jogador["total"]}')

while True:
    num = int(input(f'Dados de qual jogador? (1 a {len(lista_jogadores)}, 999 para parar): '))

    if 1 <= num <= len(lista_jogadores):
        jogador = lista_jogadores[num - 1]        
        print(f'----- Jogador {num} — {jogador["nome"]} -----')
        for j, gols in enumerate(jogador["gols"], 1):
            print(f'  Partida {j}: {gols} gol{"s" if gols != 1 else ""}')
        print(f'  Total: {jogador["total"]} gols')
    elif num == 999:
        break
    else:
        print(f'Opção inválida! Digite entre 1 e {len(lista_jogadores)} ou 999 para parar.')

print('VOLTE SEMPRE!')
