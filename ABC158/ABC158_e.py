n,p = map(int, input().split())
s = input()
#org = s
col = len(str(p))
ans = 0

for i in range(n,col-1,-1):#[n,n-1,...,col]
#    print('---try of i-col number')
#    print('i:'+str(i))
    for j in range(0,n-i+1):
#        print('---try of j-th number')
#        print('j:'+str(j))
#        print(int(s[j:j+i]))
        if int(s[j:j+i])%p == 0:
            ans = ans + 1

print(ans)
#出せなかったけど出してもTLEと思う、解説見ると方針が良くなかった感じ