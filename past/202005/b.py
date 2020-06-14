def ii():return int(input())
def iim():return map(int,input().split())
def iil():return list(map(int,input().split()))

n,m,q = iim()
quest = [n]*m
score = [[0]*m for _ in range(n)]
ans = []
for i in range(q):
    qu = iil()
    if qu[0] == 2:
        score[qu[1]-1][qu[2]-1] = 1
        quest[qu[2]-1] -= 1
    else:
        s = 0
        for x,y in zip(quest,score[qu[1]-1]):
            s += x*y
        ans.append(s)

for item in ans:
    print(item)
