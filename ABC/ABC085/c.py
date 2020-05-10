def ii():return int(input())
def iim():return map(int,input().split())
def iil():return list(map(int,input().split()))
def ism():return map(str,input().split())
def isl():return list(map(str,input().split()))

n,y = iim()
for i in range(n+1):
    for j in range(n+1):
        k = n - i - j
        v = 10000*i+5000*j+1000*k
        if k >= 0 and v == y:
            print(i,j,k)
            exit()
print(-1,-1,-1)