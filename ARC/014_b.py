n = int(input())

win = ''
l = []
for i in range(n):
    s = input()
    if win == 'DRAW':
#        print(l,s[0],l[-1],l[-1][-1])
        if s[0] != l[-1][-1] or s in l:
            if i%2 == 0:
                win = 'LOSE'
            else:
                win = 'WIN'
        l.append(s)
    elif i == 0:
        win = 'DRAW'
        l.append(s)
#    print(l,win)

print(win)
