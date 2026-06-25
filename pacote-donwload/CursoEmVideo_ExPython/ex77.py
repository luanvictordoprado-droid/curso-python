palavras =  ('Vida','Priston','Nega','Bidu', 'Charuto','Cruzeiro', 'Familia')
for p in palavras:
    print(f'\nNa palavra {p.upper()}, temos ', end='')
    for v in p:
        if v.lower() in 'aeiou':
            print(v, end=' ')