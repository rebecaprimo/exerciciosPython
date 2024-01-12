peso = float(input('Digite seu peso (em KG): '))
altura = float(input('Digite sua altura (em metros): '))

imc = peso / (altura ** 2)

if imc < 18.5:
    print(f'Seu IMC é: {imc:.1f}, você está abaixo do peso.')
elif 18.5 <= imc < 25:
    print(f'Seu IMC é: {imc:.1f}, você está no peso ideal.')
elif 25 <= imc < 30:
    print(f'Seu IMC é: {imc:.1f}, você está com sobrepeso.')
elif 30 <= imc < 40:
    print(f'Seu IMC é: {imc:.1f}, você está com obesidade.')
else:
    print(f'Seu IMC é: {imc:.1f}, você está com obesidade mórbida.')
