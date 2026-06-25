expre = input(('Digite a expressão'))
pilha = []
for simb in expre:
    if simb == '(':
        pinha.append('(')
    elif  simb == ')':
        if len (pinha)>0:
            pinha.pop()
        else:
            pinha.append(')')
            break
if len(pilha) == 0:
    print(f'Sua expressão é VALIDA')


else:
    print(f'Sua expressão é INVALIDA')

