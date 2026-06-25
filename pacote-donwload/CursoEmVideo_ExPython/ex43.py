import random
print(input('''SUAS OPÇOES 
[1]PAPEL
[2]TESOURA
[3] PEDRA'''))
escolha = int(input('QUAL A SUA ESCOLHA'))
pc_escolha = random.randint(1,3)
if escolha == pc_escolha:
    print('EMPATE')
elif  1 == escolha  and  2 == pc_escolha :
    print('PC VENCEU')
elif 2 == escolha and 1 == pc_escolha :
    print('VC VENCEU')
elif  3 == escolha and 1 == pc_escolha :
    print('PC VENCEU')
elif  1 == escolha and 3 == pc_escolha :
    print('VC VENCEU')
elif  2 == escolha and 3 == pc_escolha :
    print('PC VENCEU')

elif  3 == escolha and 2 == pc_escolha :
    print('VC VENCEU')

else:
    print('OPÇÃO INVALIDA')
