from random import randint
from time import sleep
from operator import itemgetter
jogo = {'Jogador(1)':randint(1,6),
        'Jogador(2)':randint(1,6),
        'Jogador(3)':randint(1,6),
        'Jogador(4)':randint(1,6)}
ranking = list ()

print('VALORES SORTEADOS')
for k , v in jogo.items():
    print(f'{k} tirou {v} no dado . ')
    sleep(1)
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)

print('==  RANKING  DOS JOGADORE  ==')
for i, v in enumerate(ranking):
    print(f'{i+1} lugar : {v[0]} tirou  {v[1]} no dado. ')
    sleep(1)