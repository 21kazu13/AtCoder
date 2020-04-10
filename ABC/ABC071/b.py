s = list(input())
if len(set(s)) == 26:
    print('None')
else:
    l = 'abcdefghijklmnopqrstuvwxyz'
    for i in l:
        if i in s:
            continue
        else:
            print(i)
            exit()