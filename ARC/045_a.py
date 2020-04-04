import re

def ii():return int(input())
def iim():return map(int,input().split())
def iil():return list(map(int,input().split()))
def ism():return map(str,input().split())
def isl():return list(map(str,input().split()))

s = isl()
ans = ''
for i in s:
    if i == 'Left':
        ans += '< '
    elif i == 'Right':
        ans += '> '
    else:
        ans += 'A '
print(re.sub(' $','',ans))