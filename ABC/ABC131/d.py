def ii():return int(input())
def iim():return map(int,input().split())
def iil():return list(map(int,input().split()))

n = ii()
l = []
for _ in range(n):
    l.append(iil())

l.sort(key=lambda x:x[1])

time = 0

for item in l:
    time += item[0]
    if time <= item[1]:
        continue
    else:
        print('No')
        exit()

print('Yes')