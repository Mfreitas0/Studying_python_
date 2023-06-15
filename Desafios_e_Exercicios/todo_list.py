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

todo_list = []
refazer_lista = []

def do_lista(todo_lista):
    print(f'\n{todo_list}\n')

def do_desfazer(todo_list, refazer_lista):
    if len(todo_list) == 0:
        print(f'\nNada a Desfazer')
    else:
        refazer_lista.append(todo_list.pop())

def do_refazer(todo_list, refazer_lista):
    if len(refazer_lista) == 0:
        print(f'\nNada a Refazer')
    else:
        todo_list.append(refazer_lista.pop())

while True:
    todo = input(f'\nDigite uma tarefa ou Lista[1],Desfazer[2] ou Refazer[3].\n')
    
    if todo == '1':
        do_lista(todo_list)
        continue
    elif todo == '2':
        do_desfazer(todo_list, refazer_lista)
        continue
    elif todo == '3':
        do_refazer(todo_list, refazer_lista)
    else:
        todo_list.append(todo)