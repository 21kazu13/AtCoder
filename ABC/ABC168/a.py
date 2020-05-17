def ii():return int(input())
def iim():return map(int,input().split())
def iil():return list(map(int,input().split()))
def ism():return map(str,input().split())
def isl():return list(map(str,input().split()))

n = ii()

if n%10 == 3:
    print('bon')
elif n%10 in [2,4,5,7,9]:
    print('hon')
else:
    print('pon')