def ii():return int(input())
def iim():return map(int,input().split())
def iil():return list(map(int,input().split()))
def ism():return map(str,input().split())
def isl():return list(map(str,input().split()))

s = list(input())
n = ii()

def revLR(lis, left, right):
    L = lis[:left]
    R = lis[right:]
    M = lis[left:right]
#    print(M)
    return L+M[::-1]+R

for i in range(n):
    l,r = iim()
    s = revLR(s,l-1,r)
print(''.join(s))