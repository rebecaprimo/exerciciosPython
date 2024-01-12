nome = str(input('Digite aqui seu nome completo: '))
maius = nome.upper()
minus = nome.lower()
separado = nome.split()
juntos = len(nome) - nome.count(' ')

#print(len(juntos))
print(f'Nome com letras maiúsculas: {maius}\nNome com letras minúsculas: {minus}\nTotal de letras sem espaços: {juntos}\nQuantas letras tem o primeiro nome: {len(separado[0])}')