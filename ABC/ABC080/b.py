n = int(input())

def colsum(num):
    s = str(num)
    ret = 0
    for i in s:
        ret += int(i)
    return ret

if n%colsum(n)==0:
    print('Yes')
else:
    print('No')