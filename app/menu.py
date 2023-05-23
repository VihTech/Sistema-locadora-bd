import PySimpleGUI as sg
import conect as con

conexao = con.Connection()

sg.theme('DarkGrey1')

layout = [
    [sg.Text('Menu Locadora')],
    [sg.Button('Atores')]
]

janela = sg.Window('Menu locadora', layout)

while True:
    eventos, valores = janela.read()
    if eventos == 'Atores':
        pessoas = conexao.query('select * from actor')
        for actor_id, firs_name, last_name, last_update in pessoas:
            print('%d: %s'%(actor_id, firs_name))
        
    elif eventos == sg.WIN_CLOSED:
        break