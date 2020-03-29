s = input()
n = int(input())
query = [0]*n
rev = 0
for i in range(n):
    query[i] = list(map(str, input().split()))
    if query[i][0] == '1':
        rev = rev + 1

begin = ''
end = ''
pal = 0

for i in range(n):
    if int(query[i][0]) == 1:
        pal = (pal+1)%2
    else:
        if pal == 0:
            if int(query[i][1]) == 1:
                begin = query[i][2] + begin 
            else:
                end = end + query[i][2]
        else:
            if int(query[i][1]) == 1:
                end = end + query[i][2] 
            else:
                begin = query[i][2] + begin
#    print('--------'+str(i+1)+'th try-----')
#    print('begin:'+begin)
#    print('end:'+end)
#    print('pal:'+str(pal))
if rev%2 == 1:
    print(end[::-1]+s[::-1]+begin[::-1])
else:
    print(begin+s+end)