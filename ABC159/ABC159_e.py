#コンテスト後に全探索書いたけどTLE
import copy

def isCont(l):
    return bool(l[-1]+l[-2] <= k)

def cutChoco(l):
    l[-2] += l[-1]
    l.pop(-1)
    

h, w, k = map(int,input().split())
ans = (w-1)*(h-1)+1
s = [[0 for i in range(w)] for j in range(h)]
for i in range(h):
    row = input()
    for j in range(w):
        s[i][j] = int(row[j])
#print(s)

for i in range(2**(h-1)):
#    print('----{}----'.format(str(bin(i))))
    t = copy.deepcopy(s)
    div = 0
    for j in range(h-1):
#        print(j, i>>j, (i>>j)&1, div)
        if ((i >> j) & 1) == 1:
            t[j+1-div] = [x + y for (x,y) in zip(t[j-div], t[j+1-div])]
            t.pop(j-div)
            div += 1
    div = h-1-div
#    print(div,t)
    count = [0]*len(t)
    for n in range(w):
#        print('----{}----'.format(n))
        if len(t[0]) == 1:
#            print(div)
            break
        contflag = 1
        for item in t:
#            print(item)
            contflag *= isCont(item)
        if contflag == 1:
            for item in t:
                cutChoco(item)
        else:
            div += 1
            for item in t:
                item.pop(-1)
    ans = min(ans,div)            

print(ans)

'''
綺麗にやろうとしすぎないこと
rowsum = []
s = []
for i in range(h):
    row = input()
    s.append(row)
    wsum = 0
    for item in row:
        wsum += int(item)
    rowsum.append(wsum)
print(s)
print(rowsum)
if sum(rowsum) <= k:
    print(0)
    exit()
'''


'''
colsum = []
for j in range(w):
    csum = 0
    for k in range(h):
        csum += s[k][j]
    colsum.append(csum)

print(max(rowsum))
print(max(colsum))
'''