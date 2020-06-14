def ii():return int(input())
def iim():return map(int,input().split())
def iil():return list(map(int,input().split()))

a,v = iim()
b,w = iim()
t = ii()
if v <= w:
    print('NO')
elif abs(a-b) <= (v-w)*t:
    print('YES')
else:
    print('NO')