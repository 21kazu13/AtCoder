def ii():return int(input())
def iim():return map(int,input().split())
def iil():return list(map(int,input().split()))
def ism():return map(str,input().split())
def isl():return list(map(str,input().split()))
from itertools import permutations as pm
a,b,c = iim()
l = iil()
ans = 0
for i in pm(range(3)):
    ans = max(ans,(a//l[i[0]])*(b//l[i[1]])*(c//l[i[2]]))
print(ans)