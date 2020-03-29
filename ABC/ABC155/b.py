def ii():return int(input())
def iim():return map(int,input().split())
def iil():return list(map(int,input().split()))
def ism():return map(str,input().split())
def isl():return list(map(str,input().split()))

n = ii()
A = iil()

for i in A:
    if i%2 == 0:
        if i%3 != 0 and i%5 != 0:
            print('DENIED')
            exit()

print('APPROVED')