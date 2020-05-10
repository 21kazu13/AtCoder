def ii():return int(input())
def iim():return map(int,input().split())
def iil():return list(map(int,input().split()))
def ism():return map(str,input().split())
def isl():return list(map(str,input().split()))
n = ii()
A = iil()

odd = 0
even = 0
mulof4 = 0
for i in A:
    if i%2 == 1:
        odd += 1
    elif i%4 == 2:
        even += 1
    else:
        mulof4 += 1

if odd > mulof4+1:
    print('No')
else:
    if odd < mulof4+1:
        print('Yes')
    else:
        print("Yes" if even == 0 else 'No')