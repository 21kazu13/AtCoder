def ii():return int(input())
def iim():return map(int,input().split())
def iil():return list(map(int,input().split()))
n=ii()

if n%2 == 0:
    print(1/2)
else:
    print((n+1)//2/n)