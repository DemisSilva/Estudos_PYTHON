

from itertools import count, zip_longest

indice = count()
cidades = ['São Paulo','Belo Horizonte','Salvador', 'Monte Belo']
estados = ['SP','MG','BA']

cidades_estados = zip_longest(cidades, estados, fillvalue='ESTADO')

cidades_estados_ind = zip(indice, cidades, estados)

print(list(cidades_estados))

for indice, estado, cidade in cidades_estados_ind:
    print(indice, estado, cidade)