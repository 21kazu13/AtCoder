def ii():return int(input())
def iim():return map(int,input().split())
def iil():return list(map(int,input().split()))
def ism():return map(str,input().split())
def isl():return list(map(str,input().split()))

n,a,b = iim()
cap = a+b
cA = 0
cB = 0

s = input()

for i in s:
    if i == 'a':
        if cA+cB < cap:
            cA += 1
            print('Yes')
        else:
            print('No')
    elif i == 'b':
        if cA+cB < cap and cB < b:
            cB += 1
            print('Yes')
        else:
            print('No')
    else:
        print('No')