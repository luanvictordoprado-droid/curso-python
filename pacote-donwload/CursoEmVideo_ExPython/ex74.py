from random import randint
num = (randint(1,15),randint(1,15),randint(1,15),randint(1,15),randint(1,15))
print(num)
print(f'Os valores sorteados foram {num}')
print(f'O maior valor sorteado foi {max(num)}')
print(f'O menor valor sorteado foi {min(num)}')