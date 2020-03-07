n, y = map(int, input().split())
flag = 0
for i in range(0,n+1):
    for j in range(0,n+1-i):
        value = 10000*i+5000*j+1000*(n-i-j)
        if y==value:
            flag = 1
            print(i,j,n-i-j)
            break
    if flag == 1:
        break
if flag==0:
    print(-1,-1,-1)