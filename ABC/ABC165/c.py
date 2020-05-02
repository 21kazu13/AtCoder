def ii():return int(input())
def iim():return map(int,input().split())
def iil():return list(map(int,input().split()))
def ism():return map(str,input().split())
def isl():return list(map(str,input().split()))
import itertools
n,m,q = iim()

ans = 0
l = []
for i in range(q):
    l.append(iil())

for i in itertools.combinations_with_replacement(list(range(1,m+1)),n):
    sc = 0
    for j in l:
        if i[j[1]-1] - i[j[0]-1] == j[2]:
            sc += j[3]
    ans = max(ans,sc)
print(ans)