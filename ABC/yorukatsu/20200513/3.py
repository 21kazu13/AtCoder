def ii():return int(input())
def iim():return map(int,input().split())
def iil():return list(map(int,input().split()))
def ism():return map(str,input().split())
def isl():return list(map(str,input().split()))

l,r = iim()

if l//2019 != r//2019 or l%2019 == 0 or r%2019 == 0:
    print(0)
else:
    num = float('INF')
    for i in range(l,r+1):
        for j in range(i+1,r+1):
            num = min((i*j)%2019,num)
    print(num)
