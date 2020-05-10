def ii():return int(input())
def iim():return map(int,input().split())
def iil():return list(map(int,input().split()))
def ism():return map(str,input().split())
def isl():return list(map(str,input().split()))

n = ii()
K = iil()

l = [K[0]]
for i in range(1,n-1):
#    print(K[i],K[i-1])
    l.append(min(K[i],K[i-1]))
l.append(K[-1])
print(*l)