""" EXERCICIO DICIONARIO """
print()

pergunta = {
    'Questao 1' : {
        'pergunta': 'Quanto é 2 + 2? ',
        'respostas': {
            'a': '2',
            'b': '4',
            'c': '10',},
        'resposta_certa': 'b',
    },
    'Questao 2' : {
        'pergunta': 'Quanto é 5 * 2? ',
        'respostas': {
            'a': '3',
            'b': '5',
            'c': '10',},
        'resposta_certa': 'c',
    },
}

for pk, pv in pergunta.items():
    print(f'{pk}: {pv["pergunta"]}')
    
    
    print('Escolha uma alternativa: ')
    for rk, rv in pv["respostas"].items():
        print(f'[{rk}]: {rv}')
    
    resposta_escolhida = input('Resposta Escolhida é : ')
    if resposta_escolhida == pv["resposta_certa"]:
        print(f'Você acertou!!!')
    else:
        print(f'Você Errou!!')
    print()    
    
    



