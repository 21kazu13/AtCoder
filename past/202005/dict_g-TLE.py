def ii():return int(input())
def iim():return map(int,input().split())
def iil():return list(map(int,input().split()))

from collections import deque

def bfs(xg,yg):
    queue = deque()
    queue.append((0,0))
    while queue:
        v = queue.popleft()
        dep = ans[v]
        for dx, dy in [[1,1],[0,1],[-1,1],[1,0],[-1,0],[0,-1]]:
            nx = v[0] + dx
            ny = v[1] + dy
            i = (nx,ny)
            if ans.get(i,-1) != -1:
                continue
            elif abs(x)<202 and abs(y)<202:#ここがだめ！新しい座標で判断しないと！
                if i == (xg,yg):
                    return dep+1
                else:
                    ans[i] = dep+1
                    queue.append(i)
    return -1

n,X,Y = iim()
ans = {(0,0):0}
for i in range(n):
    x,y = iim()
    ans[(x,y)] = 0
print(bfs(X,Y))

