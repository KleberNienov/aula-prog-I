def cinema(p1,p2) :
    ing1 = 0
    ing2 = 0
    if p1 <= 17:
        ing1 = 15
    elif p1 <= 59:
        ing1 = 30
    elif p1 >= 60:
        ing1 = 20
    elif p2 <=17:
        ing2 = 15
    elif p2 <= 59:
        ing2 = 30
    elif p2 >= 60:
        ing2 = 20
    return ing1+ing2
p1 = int(input('Qual sua idade?:'))
p2 = int(input('Qual sua idade?:'))
cinema(p1,p2)
print(f'O ingresso custará R$ {cinema(p1,p2)}')
