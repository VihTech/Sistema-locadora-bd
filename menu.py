import PySimpleGUI as sg
import conect as con
from estoque import*
from table_actor import*
from genero import*
from cliente import*

conexao = con.Connection()

sg.theme('DarkGrey1')

layout = [
    [sg.Text('Menu Locadora', font=(12, 12))],
    [sg.Button('Estoque', size=(25,0), font=(12, 12))],
    [sg.Button('Financeiro', size=(25,0), font=(12, 12))],
    [sg.Button('Atores', size=(25,0), font=(12, 12))],
    [sg.Button('Genêros', size=(25,0), font=(12, 12))],
    [sg.Button('Clientes', size=(25,0), font=(12, 12))]
]

janela = sg.Window('Menu locadora', layout, element_justification='c', size=(300, 220))

while True:
    eventos, valores = janela.read()
    if eventos == 'Estoque':
        janela.hide()
        tabela_estoque()
        janela.un_hide()
    
    elif eventos == 'Atores':
        janela.hide()
        tabela_atores()
        janela.un_hide()

    elif eventos == 'Clientes':
        janela.hide()
        tabela_cliente()
        janela.un_hide()

    elif eventos == 'Genêros':
        janela.hide()
        tabela_genero()
        janela.un_hide()
        
    elif eventos == sg.WIN_CLOSED:
        break
