def ii():return int(input())
def iim():return map(int,input().split())
def iil():return list(map(int,input().split()))
def ism():return map(str,input().split())
def isl():return list(map(str,input().split()))

h,w = iim()

flag = True

l = []
dx = [0,0,1,-1]
dy = [1,-1,0,0]
for i in range(h):
    l.append(list(input()))

for i in range(h):
    for j in range(w):
        if l[i][j] == '#':
            check = False
            for k in range(4):
                if i+dx[k] < 0 or i+dx[k] >= h:
                    continue
                if j+dy[k] < 0 or j+dy[k] >= w:
                    continue
                if l[i+dx[k]][j+dy[k]] == '#':
                    check = True
            if not check:
                flag = False

print('Yes' if flag else 'No')