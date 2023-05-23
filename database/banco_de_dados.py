import conect as con

conexao = con.Connection()

pessoas = conexao.query('select * from actor')
for actor_id, firs_name, last_name, last_update in pessoas:
	print('%d: %s'%(actor_id, firs_name))
	