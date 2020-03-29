def ii():return int(input())
def iim():return map(int,input().split())
def iil():return list(map(int,input().split()))

h1,w1 = iim()
h2,w2 = iim()

if h1 == h2 or h1 == w2 or w1 == h2 or w1 == w2:
    print('YES')
else:
    print('NO')