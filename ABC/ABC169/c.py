def ii():return int(input())
def iim():return map(int,input().split())
def iil():return list(map(int,input().split()))
a,b = map(str,input().split())
a = int(a)
bint,bdec = b.split('.')
bint = int(bint)
bdec = int(bdec)
ans = a*bint+(a*bdec//100)
print(ans)
'''
999999999999999 9.99

8999999999999991
0899999999999999.1
0089999999999999.91
--------------------
9989999999999990.01
'''