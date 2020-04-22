def ii():return int(input())
def iim():return map(int,input().split())
def iil():return list(map(int,input().split()))
def ism():return map(str,input().split())
def isl():return list(map(str,input().split()))

a,b = iim()
if a//100 != 9:
    acnd = 900 + a%100
elif (a%100)//10 != 9:
    acnd = 990 + a%10
else:
    acnd = 999

if b//100 != 1:
    bcnd = 100 + b%100
elif (b%100)//10 != 0:
    bcnd = 100 + b%10
else:
    bcnd = 100

print(max(a-bcnd,acnd-b))