def ii():return int(input())
def iim():return map(int,input().split())
def iil():return list(map(int,input().split()))
def ism():return map(str,input().split())
def isl():return list(map(str,input().split()))

n = ii()
s = input()

if n%2 == 0:
    print(-1)
else:
    cnd = (n+1)//2
    if cnd%3 == 0:
        cndstr = 'cab'*(2*(cnd//3)-1)+'ca'
        print(cnd-1 if s == cndstr else -1)
    elif cnd%3 == 1:
        cndstr = 'bca'*(2*(cnd//3))+'b'
        print(cnd-1 if s == cndstr else -1)
    else:
        cndstr = 'abc'*(2*(cnd//3))+'abc'
        print(cnd-1 if s == cndstr else -1)
