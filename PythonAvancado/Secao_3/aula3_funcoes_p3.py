def func(*args,**kwargs):
    args = list(args)
    print(args)
    print(args[0])
    print(args[-1])
    args[0] = 20
    print(kwargs)


lista = [1,2,3,4,5]
func(*lista, nome ='enzo', sobrenome = 'caio')
print(*lista, sep ='-')