import PySimpleGUI as sg
import conect as con

conexao = con.Connection()
genero = conexao.query("""

SELECT
	name AS "Categoria",
	COUNT(rent.inventory_id)
FROM
	film_category fctg
	LEFT JOIN category ctg ON fctg.category_id = ctg.category_id
	LEFT JOIN film flm ON fctg.film_id = flm.film_id
	LEFT JOIN inventory inv ON fctg.film_id = inv.film_id
	LEFT JOIN rental rent ON inv.inventory_id = rent.inventory_id
GROUP BY
	"Categoria"

""")

lista_informacoes_genero = []
for Categoria, count in genero:
    lista = []
    lista.append(Categoria)
    lista.append(count)
    lista_informacoes_genero.append(lista)


def tabela_genero():
    sg.theme('DarkGrey1')

    layout = [
        [sg.Text('Tabela Atores', font=(12, 12))],
        [sg.Table(values=lista_informacoes_genero,
        headings=['    Genero    ', '  Demanda  '],
        max_col_width=25,
        auto_size_columns=True,
        justification='center',
        background_color='#474747',
        alternating_row_color='#808080',
        enable_events=True,
        font=(12, 12),
        num_rows=17,
        key='-TABLE-',
        tooltip='Atores',)],
        [sg.Button('Voltar', font=(12, 12))]
    ]

    janela = sg.Window('Menu locadora', layout, element_justification='c')

    while True:
        eventos, valores = janela.read()
            
        if eventos == sg.WIN_CLOSED:
            break
        elif eventos == 'Voltar':
            janela.close()

