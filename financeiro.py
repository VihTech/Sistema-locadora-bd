import PySimpleGUI as sg
import conect as con

conexao = con.Connection()
finaceiro = conexao.query("""
SELECT

	fl.title AS "Titulo",
	endereco.address AS "Loja",
	fl.rental_rate AS "Preço",
	fl.replacement_cost AS "ValorAReport",
	COUNT(re.inventory_id) AS "Alugados"

FROM

	inventory inv INNER JOIN film fl ON
	 inv.film_id = fl.film_id

	INNER JOIN store stor ON
	 inv.store_id = stor.store_id

	INNER JOIN address endereco ON
	 endereco.address_id = stor.address_id

	INNER JOIN rental re ON
	 re.inventory_id = inv.inventory_id

GROUP BY

	"Titulo", "Loja", "ValorAReport", "Preço"
	
ORDER BY

	"Alugados" DESC
""")

lista_informacoes_financas= []

for Titulo, Loja, Preço, ValorAReport, Alugados in finaceiro:
    lista = []
    lista.append(Titulo)
    lista.append(Loja)
    lista.append(Preço)
    lista.append(ValorAReport)
    lista.append(Alugados)
    
    valor_apurado = Preço*Alugados
    lista.append(valor_apurado)
    
    valor_ganho = valor_apurado - ValorAReport
    
    lista.append(valor_ganho)
        
    lista_informacoes_financas.append(lista)


def tabela_financeiro():
    sg.theme('DarkGrey1')

    layout = [
        [sg.Text('Clientes', font=(12, 12))],
        [sg.Table(values=lista_informacoes_financas,
        headings=['Titulo', 'Loja', '  Preço  ', 'ValorAReport', 'Alugados', 'Valor Apurado', 'Valor Ganho'],
        max_col_width=50,
        auto_size_columns=True,
        justification='center',
        enable_events=True,
        background_color='#474747',
        alternating_row_color='#808080',
        font=(12, 12),
        num_rows=40,
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
            