s = list(input())
t = list(input())
l = set(['a','t','c','o','d','e','r','@'])

flag = True
for x,y in zip(s,t):
    if x == '@':
        if y not in l:
            flag = False
    elif y == '@':
        if x not in l:
            flag = False
    else:
        if x != y:
            flag = False
print('You can win' if flag else 'You will lose')