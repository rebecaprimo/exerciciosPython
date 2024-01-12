nome = str(input('Digite aqui seu nome completo: ')).strip() #remove espaços no começo e fim

nome = nome.split() #parte a string pelos pedaços
tamanho = len(nome)

print(f'Primeiro nome: {nome[0]}\nÚltimo nome: {nome[tamanho - 1]}')
