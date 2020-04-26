import re

def ii():return int(input())
def iim():return map(int,input().split())
def iil():return list(map(int,input().split()))
def ism():return map(str,input().split())
def isl():return list(map(str,input().split()))

s = isl()
n = ii()
for i in range(n):
    nw = input()
    if '*' in nw:
        nw = re.sub('\*','[a-z]',nw)
        for j in range(len(s)):
            m = re.match(nw,s[j])
            if m and m.end() == len(s[j]):
                s[j] = '*'*len(s[j])
    else:
        for j in range(len(s)):
            if s[j] == nw:
                s[j] = '*'*len(nw)
#    print(s)
print(' '.join(s))