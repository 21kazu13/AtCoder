def ii():return int(input())
def iim():return map(int,input().split())
def iil():return list(map(int,input().split()))

a,b = iim()
if (a*b)%2 == 0:
    print('Even')
else:
    print('Odd')