import PySimpleGUI as sg
import conect as con

conexao = con.Connection()
cliente= conexao.query("""
SELECT
	cust.customer_id AS "Id",
	CONCAT (cust.first_name, ' ', cust.last_name) AS "Nome",
	adres.address AS "Endereco",
	cust.email AS "Email",
	adress.address AS "Loja",
	cust.create_date AS "DataCriamento",
	cust.last_update AS "Atualizacao",
	CASE
		WHEN cust.active = 1 THEN 'Ativo'
		ELSE 'Desativado'
	END
	AS "Ativo",
	COUNT(re.customer_id)
	
FROM
	
	-- Endereço do cliente
	address adres INNER JOIN customer cust ON
	 adres.address_id = cust.address_id
	
	-- Endereço da loja do cliente
	INNER JOIN store stor ON
	 cust.store_id = stor.store_id
	INNER JOIN address adress ON
		stor.address_id = adress.address_id
	
	-- Número de filmes comprados
	INNER JOIN rental re ON
	 re.customer_id = cust.customer_id
	
GROUP BY

	"Nome", "Endereco", "Email", "DataCriamento", "Ativo", "Loja", "Atualizacao", "Id"
	
ORDER BY

	"Nome"
""")

lista_informacoes_cliente = []
lista_id = []
for Id, Nome, Endereco, Email, Loja, DataCriamento, Atualizacao, Ativo, count in cliente:
    lista = []
    lista_id.append(Id)
    lista.append(Nome)
    lista.append(Endereco)
    lista.append(Email)
    lista.append(Loja)
    lista.append(DataCriamento)
    lista.append(Atualizacao)
    lista.append(Ativo)
    lista.append(count)
    lista_informacoes_cliente.append(lista)


def tabela_cliente():
    sg.theme('DarkGrey1')

    layout = [
        [sg.Text('Clientes', font=(12, 12))],
        [sg.Table(values=lista_informacoes_cliente,
        headings=['Nome', 'Endereço', 'Email', 'Loja', 'DataCriamento', 'Atualização', 'Ativo', 'Filmes'],
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
