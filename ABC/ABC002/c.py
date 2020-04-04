def ii():return int(input())
def iim():return map(int,input().split())
def iil():return list(map(int,input().split()))
def ism():return map(str,input().split())
def isl():return list(map(str,input().split()))

a,b,c,d,e,f = iim()
print(abs((c-a)*(f-b)-(d-b)*(e-a))/2)