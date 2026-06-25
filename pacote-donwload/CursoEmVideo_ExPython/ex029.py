velocidade = float(input('QUAL A VELOCIDADE DO VEICULO  '))
if velocidade > 80:
    multa = (velocidade - 80) * 7
    print(f'Você ultrassou a velocidade permitida de 80Km sua velocidade foi de {velocidade}Km/h')
    print(f'Você foi multado em R${multa:.2f}')
else:
    print('Você não ultrassou a velocidade permitida')