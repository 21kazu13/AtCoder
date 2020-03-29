import math
def ii():return int(input())
def iim():return map(int,input().split())
def iil():return list(map(int,input().split()))
n = ii()
sn = n*(n+1)//2
if n == 1:
    print('BOWWOW')
    exit()
for i in range(2,math.ceil((sn)**0.5+1)):
    if sn%i == 0:
        print('BOWWOW')
        exit()
print('WANWAN')