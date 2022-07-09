dados = {
    'sp' : 67836.43,
    'rj' : 36678.66,
    'mg' : 29229.88,
    'es' : 27165.48,
    'outros' : 19849.53,
    }

total = dados['sp'] + dados['rj'] + dados['mg'] + dados['es'] + dados['outros']

estado_selecionado = 'sp' #MUDE AQUI O ESTADO SELECIONADO

print("representacao do estado selecionado nos lucros = {:.2f}%".format((dados[estado_selecionado]/total)*100))