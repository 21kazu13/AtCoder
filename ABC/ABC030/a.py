def ii():return int(input())
def iim():return map(int,input().split())
def iil():return list(map(int,input().split()))

a,b,c,d = iim()
if b/a > d/c:
    print('TAKAHASHI')
elif b/a < d/c:
    print('AOKI')
else:
    print('DRAW')