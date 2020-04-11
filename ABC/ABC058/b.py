o = input()
e = input()
a = []
for i in range(len(o)+len(e)):
    if i%2 == 0:
        a.append(o[i//2])
    else:
        a.append(e[i//2])
print(''.join(a))