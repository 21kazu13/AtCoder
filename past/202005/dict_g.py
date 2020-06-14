def ii():return int(input())
def iim():return map(int,input().split())
def iil():return list(map(int,input().split()))

from collections import deque

def bfs(xg,yg):
    queue = deque([(0,0)])
    while queue:
        x,y = queue.popleft()
        dep = ans[(x,y)]
        for dx, dy in [[1,1],[0,1],[-1,1],[1,0],[-1,0],[0,-1]]:
            nx = x + dx
            ny = y + dy
            i = (nx,ny)
            if ans.get(i,-1) != -1:
                continue
            elif abs(nx)<202 and abs(ny)<202:
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
    ans[(x,y)] = -9
print(bfs(X,Y))

