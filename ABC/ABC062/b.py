def ii():return int(input())
def iim():return map(int,input().split())
def iil():return list(map(int,input().split()))
def ism():return map(str,input().split())
def isl():return list(map(str,input().split()))
h,w=iim()
p = []
for i in range(h):
    p.append(input())

print('#'*(w+2))
for i in p:
    print('#'+i+'#')
print('#'*(w+2))