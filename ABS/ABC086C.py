import math
n = int(input())
t = [0] * n
x = [0] * n
y = [0] * n
for i in range(n):
    t[i], x[i], y[i] = map(int, input().split())
flag = 1

for i in range(0,n):
    #まず偶奇確認
    pality = (x[i]+y[i])%2
    if t[i]%2 == 0 and pality != 0:
        print("No")
        flag = 0
        break
    elif t[i]%2 == 1 and pality != 1:
        print("No")
        flag = 0
        break
    #ここから距離確認
    else:
        if i == 0:
            if abs(x[i])+abs(y[i]) > t[i]:
                print('No')
                flag = 0
                break
        else:
            if abs(x[i]-x[i-1])+abs(y[i]-y[i-1]) > t[i]-t[i-1]:
                print('No')
                flag = 0
                break
if flag == 1:
    print('Yes')