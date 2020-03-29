from collections import deque

s = input()
n = int(input())
query = [0]*n
rev = 0
for i in range(n):
    query[i] = list(map(str, input().split()))
    if query[i][0] == '1':
        rev = rev + 1

begin = deque()
end = deque()
pal = 0

for i in range(n):
    if int(query[i][0]) == 1:
        pal = (pal+1)%2
    else:
        if pal == 0:
            if int(query[i][1]) == 1:
                begin.appendleft(query[i][2])
            else:
                end.append(query[i][2])
        else:
            if int(query[i][1]) == 1:
                end.append(query[i][2])
            else:
                begin.appendleft(query[i][2])
#    print('--------'+str(i+1)+'th try-----')
#    print(begin)
#    print(end)
#    print('pal:'+str(pal))
#print(s)

if rev%2 == 1:
    print(''.join(deque(reversed(end)))+s[::-1]+''.join(deque(reversed(begin))))
else:
    print(''.join(begin)+s+''.join(end))