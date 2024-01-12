data = input('Digite algo aqui: ')

print(type(data))
print('É um número? ', data.isnumeric())
print('Tem letras? ', data.isalpha())
print('Tem letras e números? ', data.isalnum())
print('Está em letras maiúsculas? ', data.isupper())