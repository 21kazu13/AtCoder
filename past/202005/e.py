def ii():return int(input())
def iim():return map(int,input().split())
def iil():return list(map(int,input().split()))

n,m,q = iim()
d = {}
for _ in range(m):
    u,v = iim()
    d[u] = d.get(u,[])+[v]
    d[v] = d.get(v,[])+[u]

#print(d)

cl = [0]+iil()
l = []
for _ in range(q):
    l.append(iil())

for qu in l:
    tmp = cl[qu[1]]
    print(tmp)
    if qu[0] == 1:
        for item in d.get(qu[1],[]):
            cl[item] = tmp
    else:
        cl[qu[1]] = qu[2]

