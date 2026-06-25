contador= 0
jogador = 0
from random import randint
pc = randint(1, 10)

while jogador != pc:
    jogador = int(input('Digite um numero de 1 a 10: '))
    contador += 1
    if jogador == pc:
        print('Você acertou!')
        print(f'Você precisou de {contador} tentativas')
    else:
        print('CONTINUE')