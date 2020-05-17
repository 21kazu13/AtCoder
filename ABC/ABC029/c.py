import sys
sys.setrecursionlimit(1000)

n = int(input())
A = ['a','b','c']
cnd = []
def searchPass(li):
    if len(li) == n:
        cnd.append(''.join(li))
        return
    
    for i in A:
        li.append(i)
        searchPass(li)
        li.pop(-1)

    return

searchPass([])
for irem in cnd:
    print(irem)