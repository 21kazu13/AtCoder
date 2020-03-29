def ii():return int(input())
def iim():return map(int,input().split())
def iil():return list(map(int,input().split()))
def ism():return map(str,input().split())
def isl():return list(map(str,input().split()))

def isCont(l):
    return l[0] == l[1] or l[1] == l[2] or l[2] == l[3]

A = []
B = [[0 for i in range(4)] for j in range(4)]
for i in range(4):
    A.append(iil())
    for j in range(4):
        B[j][i] = A[i][j]
    if isCont(A[i]):
        print('CONTINUE')
        exit()
for item in B:
    if isCont(item):
        print('CONTINUE')
        exit()
print('GAMEOVER')