def ii():return int(input())
def iim():return map(int,input().split())
def iil():return list(map(int,input().split()))

from collections import deque
def bfs(u,n,d):
    '''
    BFS:O(N*(# of edges))
    @params
        int u: initial node 
        int n: number of total nodes 
        dict d: graph of all nodes 
            sample 
            d = {0:[1,3],3:[2,4,5]} 
    @returns
        list ans: list of depthes of each node
    '''
    queue = deque([u])
    ans = [-1] * (n+1)
    while queue:
        v = queue.popleft()
        for i in d[v]:
            if ans[i] == -1:
                ans[i] = v
                queue.append(i)
    return ans