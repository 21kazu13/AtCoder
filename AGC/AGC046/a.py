def ii():return int(input())
def iim():return map(int,input().split())
def iil():return list(map(int,input().split()))

x = ii()
cnt = 1
tmp = x
while tmp%360 != 0:
    cnt += 1
    tmp += x

print(cnt)