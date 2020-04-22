def ii():return int(input())
def iim():return map(int,input().split())
def iil():return list(map(int,input().split()))
def ism():return map(str,input().split())
def isl():return list(map(str,input().split()))

h,w = iim()
l = [['.']*(w+2)]
for i in range(h):
    l.append(list('.'+input()+'.'))
l.append(['.']*(w+2))
'''
for i in l:
    print(i)
'''
for row in range(1,h+1):
    for col in range(1,w+1):
        if l[row][col] != '#':
            li = [l[row-1][col-1],l[row-1][col],l[row-1][col+1],l[row][col-1],l[row][col+1],l[row+1][col-1],l[row+1][col],l[row+1][col+1]]
            l[row][col] = li.count('#')

for i in range(1,h+1):
    print(''.join(map(str,l[i][1:w+1])))