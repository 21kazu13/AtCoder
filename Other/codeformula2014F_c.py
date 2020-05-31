import re
s = list(input().split())

l = set()

for i in s:
    if '@' in i:
        m = re.findall('@[a-z]{1,}',i)
        for item in m:
            l.add(item[1:])
ll = sorted(list(l))
for j in ll:
    print(j)