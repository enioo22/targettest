import json

fil = open('dados.json')
database = json.load(fil)
dias0 = media = dias_maiores_que_media = 0
menor_faturamento = maior_faturamento = database[0]['valor']

for data in database:
    if(data['valor'] == 0.0):
        dias0 = dias0 + 1 
    
    else:
        if( data['valor'] < menor_faturamento):
            menor_faturamento = data['valor']
        
        elif(data['valor'] > maior_faturamento):
            maior_faturamento = data['valor']
        
        media = media + data['valor']

media = media/30- dias0


for data in database:
    if(data['valor']> media):
        dias_maiores_que_media = dias_maiores_que_media+1
    
print("Menor faturamento: {}".format(menor_faturamento))
print("Maior faturamento: {}".format(maior_faturamento))
print("Dias com faturamento maior que media mensal: {}".format(dias_maiores_que_media))

fil.close()