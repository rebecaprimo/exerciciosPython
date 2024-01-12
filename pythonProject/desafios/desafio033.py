num1 = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o segundo número: '))
num3 = int(input('Digite o terceiro número: '))

#verificanfo menor
menor = num1
if num2 < num3 and num2 < num1:
    menor = num2
if num3 < num1 and num3 < num2:
    menor = num3

#verificando maior
maior = num1
if num2 > num1 and num2 > num3:
    maior = num2
if num3 > num1 and num3 > num2:
    maior = num3

print(f'O número {menor} é o menor e o {maior} é o maior entre os três números!')
