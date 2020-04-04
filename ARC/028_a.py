def ii():return int(input())
def iim():return map(int,input().split())
def iil():return list(map(int,input().split()))
def ism():return map(str,input().split())
def isl():return list(map(str,input().split()))

n,a,b = iim()
bag = n
count = 0
while bag > 0:
    if count%2 == 0:
        bag -= a
    else:
        bag -= b
    count += 1

if count%2 == 0:
    print('Bug')
else:
    print('Ant')