pesoMaior = 0
pesoMenor = 0

for c in range(1, 6):
    peso = float(input(f'{c}. Digite seu peso: '))
    if c == 1:
        pesoMaior = peso
        pesoMenor = peso
    else:
        if peso > pesoMaior:
            pesoMaior = peso
        if peso < pesoMenor:
            pesoMenor = peso

print(f'O maior peso foi: {pesoMaior:.1f}kg e o menor peso: {pesoMenor:.1f}kg!')