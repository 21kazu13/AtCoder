def ii():return int(input())
def iim():return map(int,input().split())
def iil():return list(map(int,input().split()))
def ism():return map(str,input().split())
def isl():return list(map(str,input().split()))

a = ii()
b = ii()
c = ii()
x= ii()
ans = 0
for i in range(a+1):
    for j in range(b+1):
        for k in range(c+1):
#            print(i,j,k)
            if x == 500*i+100*j+50*k:
                ans += 1
print(ans)