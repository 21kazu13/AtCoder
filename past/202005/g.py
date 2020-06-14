def ii():return int(input())
def iim():return map(int,input().split())
def iil():return list(map(int,input().split()))

from collections import deque

def bfs(xg,yg):
    queue = deque([(201,201)])
    while queue:
        x,y = queue.popleft()
        dep = cord[x][y]
        for dx, dy in [[1,1],[0,1],[-1,1],[1,0],[-1,0],[0,-1]]:
            nx = x + dx
            ny = y + dy
            if 0<=nx<403 and 0<=ny<403 and cord[nx][ny] == -1:
                if (nx,ny) == (xg,yg):
                    return dep+1
                else:
                    cord[nx][ny] = dep+1
                    queue.append((nx,ny))
#        print(ans)
    return -1

n,X,Y = iim()
cord = [[-1 for _ in range(403)] for __ in range(403)]
cord[201][201] = 0
for i in range(n):
    x,y = iim()
    cord[x+201][y+201] = -9
print(bfs(X+201,Y+201))

