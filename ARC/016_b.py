def ii():return int(input())
def iim():return map(int,input().split())
def iil():return list(map(int,input().split()))
def ism():return map(str,input().split())
def isl():return list(map(str,input().split()))

n = ii()
l = [['.']*9]
cnt = 0
for _ in range(n):
    lis = list(input())
    for i,item in enumerate(lis):
        if item == 'x':
            cnt += 1
        elif item == 'o':
            if l[-1][i] != 'o':
                cnt += 1
    l.append(lis)

print(cnt)