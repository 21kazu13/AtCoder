def ii():return int(input())
def iim():return map(int,input().split())
def iil():return list(map(int,input().split()))
def ism():return map(str,input().split())
def isl():return list(map(str,input().split()))

n,l = iim()
s = input()

tab = 1
ans = 0
for item in s:
    if item == '-':
        tab -= 1
    else:
        tab += 1
        if tab > l:
            ans += 1
            tab = 1
print(ans)
