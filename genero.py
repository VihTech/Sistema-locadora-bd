import PySimpleGUI as sg
import conect as con

conexao = con.Connection()
genero = conexao.query("""WITH t1 AS (
  SELECT c.name AS Genre, COUNT(cu.customer_id) AS Total_rent_demand
  FROM category c
  JOIN film_category fc USING (category_id)
  JOIN film f USING (film_id)
  JOIN inventory i USING (film_id)
  JOIN rental r USING (inventory_id)
  JOIN customer cu USING (customer_id)
  GROUP BY 1
  ORDER BY 2 DESC
),
t2 AS (
  SELECT c.name AS Genre, SUM(p.amount) AS total_sales
  FROM category c
  JOIN film_category fc USING (category_id)
  JOIN film f USING (film_id)
  JOIN inventory i USING (film_id)
  JOIN rental r USING (inventory_id)
  JOIN payment p USING (rental_id)
  GROUP BY 1
  ORDER BY 2 DESC
)
SELECT t1.genre, t1.total_rent_demand, t2.total_sales
FROM t1
JOIN t2 ON t1.genre = t2.genre;
""")

lista_informacoes_genero = []
for genre, total_rent_demand, total_sales in genero:
    lista = []
    lista.append(genre)
    lista.append(total_rent_demand)
    lista.append(total_sales)
    lista_informacoes_genero.append(lista)


def tabela_genero():
    sg.theme('DarkGrey1')

    layout = [
        [sg.Text('Tabela Atores', font=(12, 12))],
        [sg.Table(values=lista_informacoes_genero,
        headings=['Genero', 'Demanda', 'Valor Apurado'],
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

