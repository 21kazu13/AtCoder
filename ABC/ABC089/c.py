def ii():return int(input())
def iim():return map(int,input().split())
def iil():return list(map(int,input().split()))
n = ii()
sm = set()
sa = set()
sr = set()
sc = set()
sh = set()

for _ in range(n):
    tmp = input()
    d = tmp[0]
    if d == 'M':
        sm.add(tmp)
    elif d == 'A':
        sa.add(tmp)
    elif d == 'R':
        sr.add(tmp)
    elif d == 'C':
        sc.add(tmp)
    elif d == 'H':
        sh.add(tmp)

d = {}
d['m'] = len(sm)
d['a'] = len(sa)
d['r'] = len(sr)
d['c'] = len(sc)
d['h'] = len(sh)
A = 'march'
ans = 0
for i in range(1<<5):
    output = []
    for j in range(5):
        if ((i>>j)&1)==1:
            output.append(A[j])
    if len(output) == 3:
        ans += d[output[0]]*d[output[1]]*d[output[2]]
print(ans)