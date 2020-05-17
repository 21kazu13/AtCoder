n = int(input())
l = list(range(1,7))
n = n%30
for i in range(n):
    num = i%5
    tmp = l[num]
    l[num] = l[num+1]
    l[num+1] = tmp
l = ''.join(list(map(str,l)))
print(l)
