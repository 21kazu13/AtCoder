def ii():return int(input())
def iim():return map(int,input().split())
def ism():return map(str,input().split())
def iil():return list(map(int,input().split()))
s,t=ism()
a,b=iim()
u=input()

if u == s:
    print(a-1,b)
else:
    print(a,b-1)