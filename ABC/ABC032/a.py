def ii():return int(input())
def iim():return map(int,input().split())
def iil():return list(map(int,input().split()))
a=ii()
b=ii()
n = ii()
ans = n
while True:
    if ans%a == 0 and ans%b == 0:
        print(ans)
        exit()
    else:
        ans += 1
