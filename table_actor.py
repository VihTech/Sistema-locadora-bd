import PySimpleGUI as sg
import conect as con

conexao = con.Connection()
filmes_atores = conexao.query("SELECT CONCAT(first_name, ' ', last_name), COUNT(film_actor.film_id) FROM film_actor INNER JOIN actor ON film_actor.actor_id = actor.actor_id GROUP BY first_name, last_name ORDER BY count desc")

lista_informacoes_atores = []
for concat, count in filmes_atores:
    lista = []
    lista.append(concat)
    lista.append(count)
    lista_informacoes_atores.append(lista)


def tabela_atores():
    sg.theme('DarkGrey1')

    layout = [
        [sg.Text('Tabela Atores')],
        [sg.Table(values=lista_informacoes_atores,
        headings=['Nome', 'Filmes'],
        max_col_width=25,
        auto_size_columns=True,
        justification='center',
        enable_events=True,
        num_rows=20,
        key='-TABLE-',
        tooltip='Atores',)],
        [sg.Button('Voltar')]
    ]

    janela = sg.Window('Menu locadora', layout, element_justification='c')

    while True:
        eventos, valores = janela.read()
            
        if eventos == sg.WIN_CLOSED:
            break
        elif eventos == 'Voltar':
            janela.close()
        
