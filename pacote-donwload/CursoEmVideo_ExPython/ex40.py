nota1 = float(input('Digite sua primeira nota: '))
nota2 = float(input('Digite sua segunda nota: '))
media = (nota1 + nota2) / 2

if media < 5:
    print(f'A MÉDIA FOI DE {media:.1f} , ALUNO REPROVADO')
elif 5 <= media <= 6.9:
    print(f'A MÉDIA FOI DE {media:.1f} , ALUNO EM RECUPERAÇÃO')
else:
    print(f'A MÉDIA FOI DE {media:.1f} , ALUNO APROVADO')