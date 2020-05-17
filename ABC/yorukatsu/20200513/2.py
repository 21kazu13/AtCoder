def ii():return int(input())
def iim():return map(int,input().split())
def iil():return list(map(int,input().split()))
def ism():return map(str,input().split())
def isl():return list(map(str,input().split()))

h,w = iim()
l = []
l.append(['.']*(w+2))
for _ in range(h):
    l.append(['.']+list(input())+['.'])
l.append(['.']*(w+2))

flag = True
for i in range(1,h+1,):
    for j in range(1,w+1):
        if l[i][j] == '#':
            tmp = [l[i-1][j],l[i+1][j],l[i][j-1],l[i][j+1]]
            if '#' not in tmp:
                flag = False
print('Yes' if flag else 'No')