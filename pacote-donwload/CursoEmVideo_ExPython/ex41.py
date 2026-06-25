ano_atual = 2026
ano_nascimento = int(input('Digite seu ano de nascimento: '))
idade = ano_atual - ano_nascimento

if idade <= 9:
    print('Categoria Mirim')
elif 10 <= idade <= 14:
    print('Categoria Infantil')
elif 15 <= idade <= 19:
    print('Categoria Junior')
elif 20 <= idade <= 25:
    print('Categoria Senior')
else:
    print('CATEGORIA MASTER ')
    print(f'Você possui {idade} anos')