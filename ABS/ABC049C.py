s = input()
d = 'dream'
der = 'dreamer'
e = 'erase'
er = 'eraser'
s = s[::-1]
d = d[::-1]#maerd
der = der[::-1]#remaerd
e = e[::-1]#ecare
er = er[::-1]#recare

while(1):
#    print(s)
    if s[0:3] == 'rem':
#        print(s[0:7])
        if s[0:7] != der:
            print('NO')
            break
        else:
            s = s[7:]
    elif s[0:3] == 'res':
#        print(s[0:6])
        if s[0:6] != er:
            print('NO')
            break
        else:
            s = s[6:]
    elif s[0] == 'm':
#        print(s[0:5])
        if s[0:5] != d:
            print('NO')
            break
        else:
            s = s[5:]
    elif s[0] == 'e':
#        print(s[0:5])
        if s[0:5] != e:
            print('NO')
            break
        else:
            s = s[5:]
    else:
        print('NO')
        break
    if len(s) == 0:
        print('YES')
        break
