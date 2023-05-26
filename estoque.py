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
        [sg.Text('Filmes alugados')],
        [sg.Table(values=lista_informacoes_estoque,
        headings=['Filmes', 'Quantidade'],
        max_col_width=25,
        auto_size_columns=True,
        justification='center',
        enable_events=True,
        num_rows=20,
        key='-TABLE-',
        tooltip='Atores',)],
        [sg.Button('Voltar')]
    ]

    janela_estoque = sg.Window('Menu locadora', layout, element_justification='c')

    while True:
        eventos, valores = janela_estoque.read()
            
        if eventos == sg.WIN_CLOSED:
            break
        elif eventos == 'Voltar':
            janela_estoque.close()

