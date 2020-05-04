def ii():return int(input())
def iim():return map(int,input().split())
def iil():return list(map(int,input().split()))
def ism():return map(str,input().split())
def isl():return list(map(str,input().split()))

n = ii()
A = iil()

#ここから解説見る
#j-i = A_i+A_jを変形するだけでどうみても思いつくのに、dpってどうやるんだっけに拘ってしまったのは反省
#詰まったら条件をきちんと式化する
ans = 0
d = {}
for i,item in enumerate(A):
    ans += d.get(i-item,0)
    d[i+item] = d.get(i+item,0)+1
print(ans)