def ii():return int(input())
def iim():return map(int,input().split())
def iil():return list(map(int,input().split()))
def ism():return map(str,input().split())
def isl():return list(map(str,input().split()))

import collections

n,k = iim()
c = collections.Counter(iil())
#print(c)
l = sorted(c.values(),reverse=True)
#print(l)
print(sum(l[k:]))