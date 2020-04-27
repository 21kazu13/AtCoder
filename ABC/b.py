def ii():return int(input())
def iim():return map(int,input().split())
def iil():return list(map(int,input().split()))
def ism():return map(str,input().split())
def isl():return list(map(str,input().split()))
a,b,c,d = iim()
cnt = 0
while a > 0 and c > 0:
    if cnt%2 == 0:
        c -= b
    else:
        a -= d
    cnt += 1

print('Yes' if cnt%2 == 1 else 'No')