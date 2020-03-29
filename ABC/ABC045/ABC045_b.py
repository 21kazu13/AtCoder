sa = list(input())
sb = list(input())
sc = list(input())

turn = 'a'

while 1:
    if turn == 'a':
        if len(sa) == 0:
            print("A")
            break
        else:
            turn = sa.pop(0)
    elif turn == 'b':
        if len(sb) == 0:
            print("B")
            break
        else:
            turn = sb.pop(0)
    else:
        if len(sc) == 0:
            print("C")
            break
        else:
            turn = sc.pop(0)
