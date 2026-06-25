ano_atual = 2026
ano_nascimento = int(input('Digite o ano de nascimento: '))
idade = ano_atual - ano_nascimento
if idade == 18:
    print(f'Você nasceu no ano de {ano_nascimento} e em {ano_atual}  voce completa 18 anos')
    print('APITO PARA O ALISTAMENTO MILITAR')
elif idade < 18:
    anos_falta = 18 - idade
    ano_alistamento = ano_nascimento + 18
    print(f'VOCE DEVE  SE ALISTAR NO ANO DE  {ano_alistamento}')
    print(f'Ainda faltam {anos_falta} ANOS para voce completar 18 anos')
    print('NÃO APITO PARA O ALISTAMENTO MILITAR')
elif idade > 18:
    anos_falta = 18 - idade
    ano_alistamento = ano_nascimento + 18
    print(f'Sua idade ultrapassou os 18 anos exigidos em {anos_falta} anos')
    print('NÃO APITO PARA O ALISTAMENTO MILITAR')
    print(f'VOCE DEVERIA TER SE ALISTADO NO ANO DE  {ano_alistamento}')

print('FIM')