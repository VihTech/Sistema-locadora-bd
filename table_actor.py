import PySimpleGUI as sg
import conect as con
from tabela_film_ator import*

conexao = con.Connection()
filmes_atores = conexao.query("""SELECT  actor.actor_id, CONCAT(first_name, ' ', last_name), COUNT(film_actor.film_id)
FROM

film_actor INNER JOIN actor ON film_actor.actor_id = actor.actor_id

GROUP BY
first_name, last_name, actor.actor_id""")

lista_informacoes_atores = []
lista_id = []
for actor_id, concat, count in filmes_atores:
    lista = []
    lista_id.append(actor_id)
    lista.append(concat)
    lista.append(count)
    lista_informacoes_atores.append(lista)

def tabela_atores():
    sg.theme('DarkGrey1')

    layout = [
        [sg.Text('Tabela Atores', font=(12, 12))],
        [sg.Table(values=lista_informacoes_atores,
        headings=['     Nome     ', '   Filmes   '],
        max_col_width=25,
        auto_size_columns=True,
        justification='center',
        enable_events=True,
        background_color='#474747',
        alternating_row_color='#808080',
        num_rows=20,
        key='-TABLE-',
        font=(12, 12),
        tooltip='Ver filmes')],
        [sg.Button('Voltar', font=(12, 12))]
    ]

    janela = sg.Window('Menu locadora', layout, element_justification='c')

    while True:
        eventos, valores = janela.read()
            
        if eventos == sg.WIN_CLOSED:
            break
        elif eventos == 'Voltar':
            janela.close()

        elif eventos == '-TABLE-':
            janela.hide()
            pegar_filme(lista_id[valores['-TABLE-'][0]])
            tabela_atores_filme()
            janela.un_hide()
 
