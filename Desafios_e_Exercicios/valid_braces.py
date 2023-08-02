""" PROPOSTA DE EXERCICIO
Uma sequência de chaves é considerada 
válida se todas as chaves
forem combinadas com a chave correta """

def valid_braces(string):
    while len(string) > 0:
        if "()" in string:
            string = string.replace("()", "")
        elif "[]" in string: 
            string = string.replace("[]", "")
        elif '{}' in string:
            string = string.replace("{}", "")
        else:
            return False
    return True

print(valid_braces('[{(])}]'))
print(valid_braces('[{()}]'))