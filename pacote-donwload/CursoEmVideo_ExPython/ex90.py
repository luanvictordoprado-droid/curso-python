aluno = dict()
aluno['nome'] = str(input('Nome:  '))
aluno['Media'] = float(input(f'Media de {aluno["nome"]}: '))
if aluno['Media'] >= 7:
    aluno['Situação'] = 'Aprovado'
elif 5 <= aluno['Media'] < 7:
    aluno['Situação'] = 'Recuperação'
else:
    aluno['Situação'] = 'Reprovado'

print('-='*30)

for k , v in aluno.items():
    print(f'{k} = {v}')

