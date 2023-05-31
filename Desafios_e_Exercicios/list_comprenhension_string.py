""" 
PROPOSTA DO EXERCICIO

Percorrer a string transformando em list com elementos entre 0-9:
['0123456789','0123456789'...]

Transformar novante em string, unindo os valores por um '.':
0123456789.0123456789...
"""

string = '012345678901234567890123456789012345678901234567890123456789'

comp = [string[index : index + 10] for index in range(0,len(string), 10)] 
retorno= '.'.join(comp)
print(f'{comp}\n')
print(f'{retorno}')