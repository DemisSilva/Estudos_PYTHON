l1 = [1,2,3,4,5,6,7,8,9]

ex1 = [variavel for variavel in l1]
print(ex1)

ex2 = [var * 2 for var in l1]
print(ex2)

l2 = ['Luiz','Mauro', 'Enzo']

exe3 = [v.replace('a', '@') for v in l2]
print(exe3)

tupla =(('chave','valor'),('key','value'))

ex4 =[(y,x) for x,y in tupla]
print(ex4)