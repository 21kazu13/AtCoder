def ii():return int(input())
def iim():return map(int,input().split())
def iil():return list(map(int,input().split()))
def ism():return map(str,input().split())
def isl():return list(map(str,input().split()))

l = []
for i in range(3):
    l.append(iil())


f = True
for i in range(1,3):
    dif0 = l[i][0] - l[i-1][0]
    dif1 = l[i][1] - l[i-1][1]
    dif2 = l[i][2] - l[i-1][2]
    if dif0 == dif1 == dif2:
        continue
    f = False

for i in range(1,3):
    dif0 = l[0][i] - l[0][i-1]
    dif1 = l[1][i] - l[1][i-1]
    dif2 = l[2][i] - l[2][i-1]
    if dif0 == dif1 == dif2:
        continue
    f = False

print('Yes' if f else 'No')
