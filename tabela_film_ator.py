import PySimpleGUI as sg
import conect as con

conexao = con.Connection()

def pegar_filme(id):
    global lista_informacoes_atores
    filmes_atores_id = conexao.query(f"""SELECT actor.actor_id, film.title
    FROM

    film_actor INNER JOIN actor ON film_actor.actor_id = actor.actor_id
    INNER JOIN film ON film_actor.film_id = film.film_id and film_actor.actor_id = actor.actor_id

    WHERE actor.actor_id = {id}""")

    lista_informacoes_atores = []

    for actor_id, title in filmes_atores_id:
        lista = []

        lista.append(title)
        
        lista_informacoes_atores.append(lista)


def tabela_atores_filme():
    sg.theme('DarkGrey1')

    layout = [
        [sg.Text('Filmes', font=(12, 12))],
        [sg.Table(values=lista_informacoes_atores,
        headings=['        Filmes        '],
        max_col_width=25,
        auto_size_columns=True,
        justification='center',
        background_color='#474747',
        alternating_row_color='#808080',
        font=(12, 12),
        enable_events=True,
        num_rows=20,
        key='-TABLE-',
        tooltip='Atores')],
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
            pass
            #print(lista_id[valores['-TABLE-'][0]]) # Pega a posição
