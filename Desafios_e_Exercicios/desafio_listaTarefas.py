""" 
PROPOSTA DO DESAFIO
Faça uma lista de tarefas com as seguintes opcoes:
    Adicionar Tarefa
    Lista de tarefas
    Opção de desfazer(a cada vez que chamarmos, desfaz a ultima ação)
    Opção de refazer ( a cada vez que chamarmos, refaz a ultima ação)
    
    ['Tarefa 1', 'Tarefa 2']
    ['Tarefa 1'] <- Defazer
    ['Tarefa 1', 'Tarefa 2'] <- Refazer
"""

tarefas = []
refazer = []    
while True:
    #Só vai aparecer a Opcao [REFAZER] caso tenha sido feito [DESFAZER]
    if not refazer == []:
        print('\n|\tOpções\n| Adicionar Tarefa [1]\n| Lista de Tarefas [2]\n| Desfazer[3]\n| Refazer[4]')
    else:
        #O Primeiro Acesso só tera a opcao [AD. TAREFA] e [LIST. TAREFAS]
        if not tarefas  == []:
            print(f'|\tOpções\n| Adicionar Tarefa [1]\n| Lista de Tarefas [2]\n| Desfazer[3]')

        else:
            print(f'|\tOpções\n| Adicionar Tarefa [1]\n| Lista de Tarefas [2]')
    new = input(f'\n')
    
    #Evita o ERRO caso nao seja escolhida uma das opcoes [1,2,3,4]
    if new.isdigit() == True:

        #Implemta a opcao [DESFAZER] e adiciona o elemento desfeito em [REFAZER]
        if new == '3':
            if tarefas == []:
                print(f'[Não Existe Ação para Ser Desfeita!]')
                pass
            else:
                refazer.append(tarefas.pop())
                
        #Implemeta a opcao [REFAZER]
        if new == '4':
            if refazer == []:
                print(f'[Não Existe Ação para Ser Refeita!]')
                pass
            else:
                tarefas.append(refazer.pop())
            
        if new == '1':
            print('\tNova Tarefa:')
            tarefas.append(input(f'\t'))
            print()
            
        if new == '2':
            print('\tLista de Tarefas:\n')
            for i in tarefas:
                print(f'\t{i}')
            print()
    else:
        print(f'Opção Inválida! Digite um Numero\n')