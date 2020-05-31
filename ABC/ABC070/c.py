def ii():return int(input())
def iim():return map(int,input().split())
def iil():return list(map(int,input().split()))

from fractions import gcd

n = ii()
l = []
for _ in range(n):
    l.append(ii())

commul = l[0]
for i in l:
    commul = (commul*i)//gcd(commul,i)
print(commul)