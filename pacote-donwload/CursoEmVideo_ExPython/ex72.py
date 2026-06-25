num = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis',
       'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze',
       'catorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito',
       'dezenove', 'vinte')

while True:
    digite = int(input('Digite um número entre 0 e 20: '))

    if 0 <= digite <= 20:               # ✅ dentro do intervalo!
        print(f'Você digitou {num[digite]}')
    else:
        print('Opção inválida!')        # ✅ fora do intervalo!

    perg = input('Quer continuar? [S/N]: ').upper().strip()
    if perg == 'N':
        break