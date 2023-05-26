import PySimpleGUI as sg
import conect as con

conexao = con.Connection()
estoque = conexao.query("SELECT (SELECT title f FROM film f WHERE I.film_id = f.film_id), COUNT(film_id) FROM (rental R INNER JOIN inventory I ON R.inventory_id = I.inventory_id) GROUP BY film_id ORDER BY  COUNT(film_id) DESC;")

lista_informacoes_estoque = []
for f, count in estoque:
    lista = []
    lista.append(f)
    lista.append(count)
    lista_informacoes_estoque.append(lista)


def tabela_estoque():
    sg.theme('DarkGrey1')

    layout = [
        [sg.Text('Filmes alugados', font=(12, 12))],
        [sg.Table(values=lista_informacoes_estoque,
        headings=['Filmes', 'Quantidade'],
        max_col_width=50,
        background_color='#474747',
        alternating_row_color='#808080',
        auto_size_columns=True,
        justification='center',
        font=(12, 12),
        enable_events=True,
        num_rows=20,
        key='-TABLE-',
        tooltip='Atores',)],
        [sg.Button('Voltar', font=(12, 12))]
    ]

    janela_estoque = sg.Window('Menu locadora', layout, element_justification='c')

    while True:
        eventos, valores = janela_estoque.read()
            
        if eventos == sg.WIN_CLOSED:
            break
        elif eventos == 'Voltar':
            janela_estoque.close()
