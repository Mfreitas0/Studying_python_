"""
PROPOSTA DO EXERCICIO

Pergunte a hora atual com base no horario o programa vai respoder: Bom dia, boa tarde, boa noite dependendo do horario.
"""

print(f'Informe somente a hora. \nex: 12')
a = 0
while a == 0:

    hora = input("Por favor, informe que horas são? ")
    if hora.isdigit() or hora == 'exit':
        if hora == 'exit':
            break
        hora = float(hora)
        if hora < 0 or hora > 23:
            print("Horário deve estar entre 0 e 23")
        else:
            if hora <= 11:
                print("Bom dia!")
            elif hora <= 17:
                print("Boa tarde!")
            elif hora <= 23:
                print("Boa noite!")

    else:
            print("Hora invalida! Digite 'exit' para sair.")
