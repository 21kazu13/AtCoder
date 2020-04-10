import re
def ii():return int(input())
def iim():return map(int,input().split())
def iil():return list(map(int,input().split()))
def ism():return map(str,input().split())
def isl():return list(map(str,input().split()))

a,b = iim()
s = input()
#print(a,b,s[:a],s[a],s[a+1:])
ma = re.match(r'\d{%s}' %a, s[:a])
mb = re.match(r'\d{%s}' %b, s[a+1:])
#print(ma,mb)
if s[a] == '-' and ma and mb:
    print('Yes')
else:
    print('No')