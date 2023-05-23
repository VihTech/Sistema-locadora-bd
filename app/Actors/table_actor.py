import PySimpleGUI as sg
import conect as con

conexao = con.Connection()
pessoas = conexao.query('select * from actor')

lista_informacoes_atores = []
for acotr_id, first_name, last_name, last_update in pessoas:
    lista = []
    lista.append(acotr_id)
    lista.append(first_name)
    lista.append(last_name)
    lista.append(last_update)
    lista_informacoes_atores.append(lista)


def tabela_atores():
    sg.theme('DarkGrey1')

    layout = [
        [sg.Text('Tabela Atores')],
        [sg.Table(values=lista_informacoes_atores,
        headings=['Caixa', 'H. Abertura', 'D. Abertura', 'H. Fechamento', 'D. Fechamento','Dinheiro Inicial','Dinheiro Recebido','Dinheiro Final'],
        max_col_width=25,
        auto_size_columns=True,
        justification='center',
        enable_events=True,
        num_rows=20,
        key='-TABLE-',
        tooltip='This is a table')]
    ]

    janela = sg.Window('Menu locadora', layout)

    while True:
        eventos, valores = janela.read()
            
        if eventos == sg.WIN_CLOSED:
            break
        
tabela_atores()