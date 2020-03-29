import math
def ii():return int(input())
def iim():return map(int,input().split())
def iil():return list(map(int,input().split()))
n=ii()

for i in range(2,math.ceil(n**0.5)+2):
    if n%i == 0:
        print('NO')
        exit()
print('YES')
