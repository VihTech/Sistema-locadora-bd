import PySimpleGUI as sg
import conect as con
from tabela_film_ator import*

conexao = con.Connection()
filmes_atores = conexao.query("""

SELECT
	actr.actor_id,
	CONCAT(first_name, ' ', last_name) AS "Ator",
	COUNT(title) AS "NFilmesAtuados",
	COUNT(rent.inventory_id) AS "Vendas"
FROM
	actor actr
	LEFT JOIN film_actor flmactr ON actr.actor_id = flmactr.actor_id
	LEFT JOIN film flm ON flmactr.film_id = flm.film_id
	LEFT JOIN inventory inv ON inv.film_id = flm.film_id
	LEFT JOIN rental rent ON inv.inventory_id = rent.inventory_id
GROUP BY
	"Ator",
	actr.actor_id
ORDER BY
	"Vendas" DESC

""")

lista_informacoes_atores = []
lista_id = []
for actor_id, Ator, NFilmesAtuados, Vendas in filmes_atores:
    lista = []
    lista_id.append(actor_id)
    lista.append(Ator)
    lista.append(NFilmesAtuados)
    lista.append(Vendas)
    lista_informacoes_atores.append(lista)

def tabela_atores():
    sg.theme('DarkGrey1')

    layout = [
        [sg.Text('Tabela Atores', font=(12, 12))],
        [sg.Table(values=lista_informacoes_atores,
        headings=['     Nome     ', 'Filmes Atuados', 'Filmes Alugados'],
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
 
