def ii():return int(input())
def iim():return map(int,input().split())
def iil():return list(map(int,input().split()))
def ism():return map(str,input().split())
def isl():return list(map(str,input().split()))
a,b,c = iim()
count = 0
if a == b == c and a%2 == 0:
    print(-1)
    exit()

while a%2 == 0 and b%2 == 0 and c%2 == 0:
    ta = a
    tb = b
    tc = c
    a = (tb+tc)//2
    b = (tc+ta)//2
    c = (ta+tb)//2
    count += 1

print(count)