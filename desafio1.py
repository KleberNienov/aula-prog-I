def tabuada(valor):
    for i in range(0,11):
        print(f'{i} * {valor} = {i*valor}')
valor = int(input('informe o número para a tabuada:'))
tabuada(valor)
