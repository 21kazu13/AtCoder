def ii():return int(input())
def iim():return map(int,input().split())
def iil():return list(map(int,input().split()))
m,d = iim()

if m%d == 0:
    print('YES')
else:
    print('NO')