def ii():return int(input())
def iim():return map(int,input().split())
def iil():return list(map(int,input().split()))
k = ii()

if k%2 == 0 or k%5 == 0:
    print(-1)
else:
    if k%7 == 0:
        k //= 7
    elif k%3 == 0:
        k *= 9
    if k==1:
        print(1)
        exit()
    num = 10
    cnt = 1
    while num != 1:
        num *= 10
        num %= k
        cnt += 1
    print(cnt)
