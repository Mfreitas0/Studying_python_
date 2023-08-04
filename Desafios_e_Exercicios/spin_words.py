""" 
Escrever uma função que receba uma string de uma ou mais palavras e retorne a mesma string,
mas com todas as palavras de cinco ou mais letras invertidas

As strings passadas consistirão apenas em letras e espaços. Espaços serão incluídos somente
quando houver mais de uma palavra.
"""
spin_words = lambda sentence: ' '.join([i[::-1] if len(i) >= 5 else i for i in sentence.split()])
        
        
        
print(spin_words("Welcome"))#, "emocleW"
print(spin_words("CodeWars"))#, "sraWedoC"
print(spin_words("to"))#, "to"
print(spin_words("Hey fellow warriors"))#, "'Hey wollef sroirraw'"