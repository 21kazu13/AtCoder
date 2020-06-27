def ii():return int(input())
def iim():return map(int,input().split())
def iil():return list(map(int,input().split()))
import re

n = ii()
s = input()
s = s+s[0]
#最初2つがSS/SW/WS/WWの状態で、前から決めてく
#S=1,W=0
l = [[1,1],[1,0],[0,1],[0,0]]
'''
ss = [1,1]
sw = [1,0]
ws = [0,1]
ww = [0,0]
'''

def nextAnimal(lis,st):
    if st == 'o':
        lis.append(lis[-2]^(lis[-1]^1))
    else:
        lis.append(lis[-2]^(lis[-1]))
#    print(lis)


for i in s[1:]:
    for item in l:
        nextAnimal(item,i)

#print(l)
for item in l:
    if item[0] == item[-2] and item[1] == item[-1]:
        ans = ''
        for i in item[:n]:
            if i == 0:
                ans += 'W'
            else:
                ans += 'S'
        print(ans)
        exit()
print(-1)