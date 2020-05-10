from collections import Counter

def ii():return int(input())
def iim():return map(int,input().split())
def iil():return list(map(int,input().split()))
def ism():return map(str,input().split())
def isl():return list(map(str,input().split()))

n = ii()
p = Counter(iil())
m = iil()
t = Counter(iil())

#print(p)
#print(t)
'''
input:
5
3 1 4 1 5
3
5 4 3
Counter:
Counter({1: 2, 3: 1, 4: 1, 5: 1})
Counter({5: 1, 4: 1, 3: 1})
'''

flag = True
for k,v in t.items():
    if p.get(k,0) < v:
        flag = False
print('YES' if flag else 'NO')