def ii():return int(input())
def iim():return map(int,input().split())
def iil():return list(map(int,input().split()))
def ism():return map(str,input().split())
def isl():return list(map(str,input().split()))

n = ii()
count = {}
cmax = 0
for i in range(n):
    s = input()
    c = count.get(s,0)+1
    cmax = max(c,cmax)
    count[s] = c
ans = sorted([kv[0] for kv in count.items() if kv[1] == cmax])
#max_k_list = [kv[0] for kv in d.items() if kv[1] == max(d.values())]
#これだとd.items()の一つ一つでd.values()やってるから遅いイメージ
for item in ans:
    print(item)