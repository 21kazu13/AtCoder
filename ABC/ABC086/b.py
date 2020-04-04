def ii():return int(input())
def iim():return map(int,input().split())
def iil():return list(map(int,input().split()))
def ism():return map(str,input().split())
def isl():return list(map(str,input().split()))

a,b = ism()
n = int(a+b)

for i in range(317):
    if i**2 == n:
        print('Yes')
        exit()


print('No')