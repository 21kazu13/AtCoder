l = []
for i in range(1,10):
    for j in range(1,10):
        l.append(i*j)

if int(input()) in l:
    print('Yes')
else:
    print('No')