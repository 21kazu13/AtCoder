def ii():return int(input())
def iim():return map(int,input().split())
def iil():return list(map(int,input().split()))
def ism():return map(str,input().split())
def isl():return list(map(str,input().split()))

n = ii()
ans = []
def DFS(head, rest):
    if len(rest) == 0:
        print('hoge')
        ans.append(head)
        rest.append(head.pop(-1))
        return 0
    else:
        print('foo')
        head.append(rest.pop(0))
        DFS(head, rest)
        tmp = head[-1]
        head[-1] = rest[-1]
        rest[-1] = tmp


d = []
DFS(d,list(range(1,n+1)))
print(d)
