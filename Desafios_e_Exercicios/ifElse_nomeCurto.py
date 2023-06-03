""" 
EXERCICIO ULTILIZANDO IF E ELSE
"""

nome = input('Digite seu primeiro nome: ')
tamanho = len(nome)

if tamanho <= 4:
    print(f'Seu nome é curto, ele possui {tamanho} letras.')
elif tamanho <= 6:
    
    print(f'Seu nome é normal, ele possui {tamanho} letras.')
else:
    print(f'Seu nome é muito grande, ele possui {tamanho} letras.')