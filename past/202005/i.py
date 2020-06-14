import numpy as np

def ii():return int(input())
def iim():return map(int,input().split())
def iil():return list(map(int,input().split()))

n = ii()
A = np.arange(0,n**2).reshape(n,n)
#print(A)

qq = ii()
ql = []
for _ in range(qq):
    ql.append(iil())

for q in ql:
    if q[0] == 4:
        print(A[q[1]-1][q[2]-1])
    elif q[0] == 3:
        A = A.T
    elif q[0] == 2:
        l = list(range(n))
        l[q[1]-1],l[q[2]-1] = l[q[2]-1],l[q[1]-1]
        A = A[:,l]
    else:
        l = list(range(n))
        l[q[1]-1],l[q[2]-1] = l[q[2]-1],l[q[1]-1]
        A = A[l,:]
