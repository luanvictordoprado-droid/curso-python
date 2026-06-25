peso = float(input('Digite seu peso  '))
altura = float(input('Digite sua altura '))
imc = peso / (altura * altura)
if imc < 18.5:
    print(f'Seu indice IMC foi de  {imc:.2f} e vc esta abaixo do peso')
elif 18.5 <= imc < 25:
    print(f'Seu indice IMC foi de  {imc:.2f} e vc esta  com peso  normal ')

elif 25 <= imc < 30:
    print(f'Seu indice IMC foi de  {imc:.2f} e vc esta  com obesidade ')

else:
    print(f'Seu indice IMC foi de  {imc:.2f} e vc esta  com obesidade morbida ')