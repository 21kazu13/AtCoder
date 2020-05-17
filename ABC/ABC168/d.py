def ii():return int(input())
def iim():return map(int,input().split())
def iil():return list(map(int,input().split()))
def ism():return map(str,input().split())
def isl():return list(map(str,input().split()))
from collections import deque


def bfs(u):
    queue = deque([u])
    ans = [0] * (n+1)
    ans[1] = 1
    while queue:
        v = queue.popleft()
#        print(v,d[v])
        for i in d[v]:
            if  ans[i] == 0:
                ans[i] = v
                queue.append(i)
#        print(ans)
    return ans

n,m = iim()
d = {}
for i in range(m):
    a,b = iim()
    la = d.get(a,[])
    la.append(b)
    d[a] = la
    lb = d.get(b,[])
    lb.append(a)
    d[b] = lb
#print(d)
ans = bfs(1)

#print(ans)
if 0 in ans[1:]:
    print('No')
else:
    print('Yes')
    for i in ans[2:]:
        print(i)