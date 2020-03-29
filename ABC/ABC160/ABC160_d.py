import math
n, x, y = map(int,input().split())
dif = y-x
ans = [0]*(n-1)

for i in range(1,n):
    for j in range(i+1,n+1):
        dist = abs(x-i)+abs(y-j)+1
        ans[min(dist,(j-i))-1] += 1

for i in ans:
    print(i)