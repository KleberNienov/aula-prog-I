def partida(p1,p2) :
    if p1 == p2 :
        return 0
    elif p1 >= p2 :
        return 1
    else :
        return 2
p1 = int(input("Gols time 1:"))
p2 = int(input("Gols time 2:"))
print(partida(p1,p2))
