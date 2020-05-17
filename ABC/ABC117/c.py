def ii():return int(input())
def iim():return map(int,input().split())
def iil():return list(map(int,input().split()))
def ism():return map(str,input().split())
def isl():return list(map(str,input().split()))

n,m = iim()
X = iil()
X.sort()

dif = []
for i in range(1,m):
    dif.append(X[i]-X[i-1])

dif.sort(reverse=True)
#print(dif)
#print(X[-1],X[0],sum(dif[:n-1]))
print(X[-1]-X[0]-sum(dif[:n-1]))
