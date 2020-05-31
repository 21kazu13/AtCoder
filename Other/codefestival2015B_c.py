def ii():return int(input())
def iim():return map(int,input().split())
def iil():return list(map(int,input().split()))

n,m = iim()
A = sorted(iil(),reverse=True)
B = sorted(iil(),reverse=True)

if m > n:
    print('NO')
else:
    for x,y in zip(A,B):
#        print(x,y)
        if y <= x:
            continue
        else:
            print('NO')
            exit()
    print('YES')